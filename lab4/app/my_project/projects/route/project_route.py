from flask import Blueprint
from app.my_project.projects.controller.project_controller import ProjectController

project_bp = Blueprint('project_bp', __name__)


project_bp.route('/projects', methods=['GET'])(ProjectController.get_projects)
project_bp.route('/projects', methods=['POST'])(ProjectController.create_project)
project_bp.route('/projects/<int:project_id>', methods=['PUT'])(ProjectController.update_project)
project_bp.route('/projects/<int:project_id>', methods=['DELETE'])(ProjectController.delete_project)


project_bp.route('/projects/<int:project_id>/vacancies', methods=['GET'])(ProjectController.get_vacancies_by_project)
project_bp.route('/projects/<int:project_id>/contacts', methods=['GET'])(ProjectController.get_contacts_by_project)