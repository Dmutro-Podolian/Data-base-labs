from app.my_project.projects.domain.project_models import Project, ProjectContact, Vacancy
from app.utils.db import session

class ProjectDAO:
    
    def get_all_projects(self):
        return session.query(Project).all()

    def get_project_by_id(self, project_id):
        return session.query(Project).filter(Project.id == project_id).first()

    def create_project(self, project: Project):
        session.add(project)
        session.commit()
        return project

    def update_project(self, project_id, new_name, new_description=None):
        project = self.get_project_by_id(project_id)
        if project:
            project.project_name = new_name
            if new_description is not None:
                project.description = new_description
            session.commit()
        return project

    def delete_project(self, project_id):
        project = self.get_project_by_id(project_id)
        if project:
            session.delete(project)
            session.commit()
            return True
        return False

    def get_vacancies_by_project(self, project_id):
        return session.query(Vacancy).filter(Vacancy.Projects_id == project_id).all()

    
    def get_contacts_for_project(self, project_id):
        project = self.get_project_by_id(project_id)
        return project.contacts if project else []