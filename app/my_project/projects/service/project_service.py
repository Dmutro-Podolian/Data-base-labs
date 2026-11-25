from app.my_project.projects.dao.project_dao import ProjectDAO
from app.my_project.projects.domain.project_models import Project


class ProjectService:
    def __init__(self):
        self.dao = ProjectDAO()

    def get_all_projects(self):
        return self.dao.get_all_projects()

    def get_all_contacts(self):
        return self.dao.get_all_contacts()

    def get_all_vacancies(self):
        return self.dao.get_all_vacancies()

    def get_all_candidates(self):
        return self.dao.get_all_candidates()

    def get_all_recruitment_levels(self):
        return self.dao.get_all_recruitment_levels()

    def get_all_technical_levels(self):
        return self.dao.get_all_technical_levels()

    def get_all_english_levels(self):
        return self.dao.get_all_english_levels()

    def get_all_candidate_vacancies(self):
        return self.dao.get_all_candidate_vacancies()

    def get_all_interviews(self):
        return self.dao.get_all_interviews()

    def get_all_interview_results(self):
        return self.dao.get_all_interview_results()

    def get_all_project_notes(self):
        return self.dao.get_all_project_notes()

    def get_all_project_audit_logs(self):
        return self.dao.get_all_project_audit_logs()

    def get_all_project_contact_links(self):
        return self.dao.get_all_project_contact_links()

    def get_project(self, project_id):
        return self.dao.get_project_by_id(project_id)

    def create_project(self, data):
        new_project = Project(
            project_name=data.get("project_name"),
            description=data.get("description"),
        )
        return self.dao.create_project(new_project)

    def update_project(self, project_id, data):
        return self.dao.update_project(project_id, data)

    def delete_project(self, project_id):
        return self.dao.delete_project(project_id)

    def get_project_vacancies(self, project_id):
        return self.dao.get_vacancies_by_project(project_id)

    def get_project_contacts(self, project_id):
        return self.dao.get_contacts_for_project(project_id)

    def add_project_via_procedure(self, data):
        project_name = data.get("project_name")
        description = data.get("description")
        if not project_name:
            raise ValueError("Поле 'project_name' є обов'язковим")
        return self.dao.call_add_project(project_name, description)

    def link_project_contact_by_fullname(self, data):
        project_name = data.get("project_name")
        contact_fullname = data.get("full_name") or data.get("contact_fullname")
        if not project_name or not contact_fullname:
            raise ValueError("Потрібно передати 'project_name' та 'full_name'")
        return self.dao.call_link_project_contact(project_name, contact_fullname)

    def insert_ten_nonames(self, start_num):
        if start_num is None:
            raise ValueError("Параметр 'start_num' є обов'язковим")
        return self.dao.call_insert_ten_nonames(int(start_num))

    def get_max_project_id_via_procedure(self):
        return self.dao.call_show_max_project_id()

    def split_projects_with_cursor(self):
        return self.dao.call_split_projects_with_cursor()