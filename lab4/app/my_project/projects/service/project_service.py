from app.my_project.projects.dao.project_dao import ProjectDAO
from app.my_project.projects.domain.project_models import Project

class ProjectService:
    def __init__(self):
        self.dao = ProjectDAO()

    def get_all_projects(self): 
        return self.dao.get_all_projects()

    def get_project(self, project_id): 
        return self.dao.get_project_by_id(project_id)

    def create_project(self, data): 
        new_project = Project(
            project_name=data.get('project_name'),
            description=data.get('description')
        )
        saved_project = self.dao.create_project(new_project)
        return saved_project

    def update_project(self, project_id, data): 
        return self.dao.update_project(
            project_id, 
            new_name=data.get('project_name'), 
            new_description=data.get('description')
        )

    def delete_project(self, project_id): 
        return self.dao.delete_project(project_id)
    

    def get_project_vacancies(self, project_id):
        return self.dao.get_vacancies_by_project(project_id)

    def get_project_contacts(self, project_id):
        return self.dao.get_contacts_for_project(project_id)