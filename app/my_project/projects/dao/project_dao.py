from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.my_project.projects.domain.project_models import (
    Candidate,
    CandidateVacancy,
    EnglishLevel,
    Interview,
    InterviewResult,
    Project,
    ProjectAuditLog,
    ProjectContact,
    ProjectNote,
    ReqruitmentLevel,
    TechnicalLevel,
    Vacancy,
    projects_contacts,
)
from app.utils.db import session


class ProjectDAO:

    def _get_all(self, model):
        try:
            return session.query(model).all()
        except SQLAlchemyError:
            session.rollback()
            raise

    def get_all_projects(self):
        return self._get_all(Project)

    def get_all_contacts(self):
        return self._get_all(ProjectContact)

    def get_all_vacancies(self):
        return self._get_all(Vacancy)

    def get_all_candidates(self):
        return self._get_all(Candidate)

    def get_all_recruitment_levels(self):
        return self._get_all(ReqruitmentLevel)

    def get_all_technical_levels(self):
        return self._get_all(TechnicalLevel)

    def get_all_english_levels(self):
        return self._get_all(EnglishLevel)

    def get_all_candidate_vacancies(self):
        return self._get_all(CandidateVacancy)

    def get_all_interviews(self):
        return self._get_all(Interview)

    def get_all_interview_results(self):
        return self._get_all(InterviewResult)

    def get_all_project_notes(self):
        return self._get_all(ProjectNote)

    def get_all_project_audit_logs(self):
        return self._get_all(ProjectAuditLog)

    def get_all_project_contact_links(self):
        try:
            rows = session.execute(projects_contacts.select()).fetchall()
            return [
                {
                    "Projects_id": row.Projects_id,
                    "ProjectContacts_id": row.ProjectContacts_id,
                }
                for row in rows
            ]
        except SQLAlchemyError:
            session.rollback()
            raise

    def get_project_by_id(self, project_id):
        try:
            return session.query(Project).filter(Project.id == project_id).first()
        except SQLAlchemyError:
            session.rollback()
            raise

    def create_project(self, project):
        try:
            session.add(project)
            session.commit()
            return project
        except SQLAlchemyError:
            session.rollback()
            raise

    def update_project(self, project_id, data):
        try:
            project = session.query(Project).filter(Project.id == project_id).first()
            if not project:
                return None
            if "project_name" in data:
                project.project_name = data["project_name"]
            if "description" in data:
                project.description = data["description"]
            session.commit()
            return project
        except SQLAlchemyError:
            session.rollback()
            raise

    def delete_project(self, project_id):
        try:
            project = session.query(Project).filter(Project.id == project_id).first()
            if not project:
                return False
            session.delete(project)
            session.commit()
            return True
        except SQLAlchemyError:
            session.rollback()
            raise

    def get_vacancies_by_project(self, project_id):
        try:
            return session.query(Vacancy).filter(Vacancy.Projects_id == project_id).all()
        except SQLAlchemyError:
            session.rollback()
            raise

    def get_contacts_for_project(self, project_id):
        try:
            project = session.query(Project).filter(Project.id == project_id).first()
            return project.contacts if project else []
        except SQLAlchemyError:
            session.rollback()
            raise

    def call_add_project(self, project_name, description=None):
        try:
            session.execute(
                text("CALL `mydb`.`sp_add_project`(:p_name, :p_desc)"),
                {"p_name": project_name, "p_desc": description},
            )
            session.commit()
            return (
                session.query(Project)
                .filter(Project.project_name == project_name)
                .order_by(Project.id.desc())
                .first()
            )
        except SQLAlchemyError:
            session.rollback()
            raise

    def call_link_project_contact(self, project_name, contact_fullname):
        try:
            session.execute(
                text("CALL `mydb`.`sp_link_project_contact_by_fullname`(:p_name, :p_fullname)"),
                {"p_name": project_name, "p_fullname": contact_fullname},
            )
            session.commit()
            return True
        except SQLAlchemyError:
            session.rollback()
            raise

    def call_insert_ten_nonames(self, start_num):
        try:
            session.execute(
                text("CALL `mydb`.`sp_insert_ten_nonames`(:p_start_num)"),
                {"p_start_num": start_num},
            )
            session.commit()
            return True
        except SQLAlchemyError:
            session.rollback()
            raise

    def call_show_max_project_id(self):
        try:
            result = session.execute(text("CALL `mydb`.`sp_show_max_project_id`()"))
            row = result.fetchone()
            return row[0] if row else None
        except SQLAlchemyError:
            session.rollback()
            raise

    def call_split_projects_with_cursor(self):
        try:
            result = session.execute(text("CALL `mydb`.`sp_split_projects_with_cursor`()"))
            row = result.fetchone()
            session.commit()
            if row:
                return {"table_1": row[0], "table_2": row[1]}
            return {}
        except SQLAlchemyError:
            session.rollback()
            raise