from flask import request, jsonify
from app.my_project.projects.service.project_service import ProjectService

class ProjectController:

    @staticmethod
    def get_projects():
        service = ProjectService()
        projects = service.get_all_projects()
        result = [project.put_into_dto() for project in projects]
        return jsonify(result, {"message": "Список усіх проєктів успішно отримано"}), 200

    @staticmethod
    def create_project():
        data = request.json
        service = ProjectService()
        created_project = service.create_project(data)
        return jsonify(created_project.put_into_dto()), 201

    @staticmethod
    def update_project(project_id):
        data = request.json
        service = ProjectService()
        updated_project = service.update_project(project_id, data)
        if updated_project:
            return jsonify(updated_project.put_into_dto()), 200
        return jsonify({"error": "Проєкт не знайдено"}), 404

    @staticmethod
    def delete_project(project_id):
        service = ProjectService()
        success = service.delete_project(project_id)
        if success:
            return jsonify({"message": f"Проєкт з ID {project_id} успішно видалено"}), 200
        return jsonify({"error": "Проєкт не знайдено"}), 404

    @staticmethod
    def get_vacancies_by_project(project_id):
        service = ProjectService()
        vacancies = service.get_project_vacancies(project_id)
        result = [vacancy.put_into_dto() for vacancy in vacancies]
        return jsonify(result), 200

    @staticmethod
    def get_contacts_by_project(project_id):
        service = ProjectService()
        contacts = service.get_project_contacts(project_id)
        result = [contact.put_into_dto() for contact in contacts]
        return jsonify(result), 200