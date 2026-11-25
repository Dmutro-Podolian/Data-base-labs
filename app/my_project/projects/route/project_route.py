from flask import Blueprint

from app.my_project.projects.controller.project_controller import ProjectController

project_bp = Blueprint("project_bp", __name__)


project_bp.route("/projects", methods=["GET"])(ProjectController.get_projects)
project_bp.route("/projects", methods=["POST"])(ProjectController.create_project)
project_bp.route("/projects/<int:project_id>", methods=["PUT"])(ProjectController.update_project)
project_bp.route("/projects/<int:project_id>", methods=["DELETE"])(ProjectController.delete_project)

project_bp.route("/contacts", methods=["GET"])(ProjectController.get_contacts)
project_bp.route("/vacancies", methods=["GET"])(ProjectController.get_vacancies)
project_bp.route("/candidates", methods=["GET"])(ProjectController.get_candidates)
project_bp.route("/recruitment-levels", methods=["GET"])(ProjectController.get_recruitment_levels)
project_bp.route("/technical-levels", methods=["GET"])(ProjectController.get_technical_levels)
project_bp.route("/english-levels", methods=["GET"])(ProjectController.get_english_levels)
project_bp.route("/candidate-vacancies", methods=["GET"])(ProjectController.get_candidate_vacancies)
project_bp.route("/interviews", methods=["GET"])(ProjectController.get_interviews)
project_bp.route("/interview-results", methods=["GET"])(ProjectController.get_interview_results)
project_bp.route("/project-notes", methods=["GET"])(ProjectController.get_project_notes)
project_bp.route("/project-audit-logs", methods=["GET"])(ProjectController.get_project_audit_logs)
project_bp.route("/project-contact-links", methods=["GET"])(ProjectController.get_project_contact_links)


project_bp.route("/projects/<int:project_id>/vacancies", methods=["GET"])(ProjectController.get_vacancies_by_project)
project_bp.route("/projects/<int:project_id>/contacts", methods=["GET"])(ProjectController.get_contacts_by_project)


project_bp.route("/projects/procedure", methods=["POST"])(ProjectController.add_project_via_procedure)
project_bp.route("/projects/link-contact", methods=["POST"])(ProjectController.link_project_contact)
project_bp.route("/projects/nonames", methods=["POST"])(ProjectController.insert_ten_nonames)
project_bp.route("/projects/max-id", methods=["GET"])(ProjectController.get_max_project_id)
project_bp.route("/projects/split-cursor", methods=["POST"])(ProjectController.split_projects_with_cursor)