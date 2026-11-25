from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from app.my_project.projects.service.project_service import ProjectService


class ProjectController:

    @staticmethod
    def _list_response(getter_fn, message):
        try:
            service = ProjectService()
            items = getter_fn(service)
            result = [item.put_into_dto() if hasattr(item, "put_into_dto") else item for item in items]
            return jsonify(result, {"message": message}), 200
        except SQLAlchemyError as e:
            return jsonify({"error": "Database error", "details": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_projects():
        return ProjectController._list_response(
            lambda s: s.get_all_projects(),
            "Список усіх проєктів успішно отримано",
        )

    @staticmethod
    def get_contacts():
        return ProjectController._list_response(
            lambda s: s.get_all_contacts(),
            "Список усіх контактів проєктів успішно отримано",
        )

    @staticmethod
    def get_vacancies():
        return ProjectController._list_response(
            lambda s: s.get_all_vacancies(),
            "Список усіх вакансій успішно отримано",
        )

    @staticmethod
    def get_candidates():
        return ProjectController._list_response(
            lambda s: s.get_all_candidates(),
            "Список усіх кандидатів успішно отримано",
        )

    @staticmethod
    def get_recruitment_levels():
        return ProjectController._list_response(
            lambda s: s.get_all_recruitment_levels(),
            "Список усіх рівнів рекрутингу успішно отримано",
        )

    @staticmethod
    def get_technical_levels():
        return ProjectController._list_response(
            lambda s: s.get_all_technical_levels(),
            "Список усіх технічних рівнів успішно отримано",
        )

    @staticmethod
    def get_english_levels():
        return ProjectController._list_response(
            lambda s: s.get_all_english_levels(),
            "Список усіх рівнів англійської успішно отримано",
        )

    @staticmethod
    def get_candidate_vacancies():
        return ProjectController._list_response(
            lambda s: s.get_all_candidate_vacancies(),
            "Список заявок кандидатів на вакансії успішно отримано",
        )

    @staticmethod
    def get_interviews():
        return ProjectController._list_response(
            lambda s: s.get_all_interviews(),
            "Список усіх співбесід успішно отримано",
        )

    @staticmethod
    def get_interview_results():
        return ProjectController._list_response(
            lambda s: s.get_all_interview_results(),
            "Список усіх результатів співбесід успішно отримано",
        )

    @staticmethod
    def get_project_notes():
        return ProjectController._list_response(
            lambda s: s.get_all_project_notes(),
            "Список усіх нотаток проєктів успішно отримано",
        )

    @staticmethod
    def get_project_audit_logs():
        return ProjectController._list_response(
            lambda s: s.get_all_project_audit_logs(),
            "Список записів журналу аудиту успішно отримано",
        )

    @staticmethod
    def get_project_contact_links():
        return ProjectController._list_response(
            lambda s: s.get_all_project_contact_links(),
            "Список зв'язків проєктів і контактів успішно отримано",
        )

    @staticmethod
    def create_project():
        try:
            data = request.get_json() or {}
            service = ProjectService()
            created_project = service.create_project(data)
            return jsonify(created_project.put_into_dto()), 201
        except SQLAlchemyError as e:
            return jsonify({"error": "Database error", "details": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def update_project(project_id):
        try:
            data = request.get_json() or {}
            service = ProjectService()
            updated_project = service.update_project(project_id, data)
            if updated_project:
                return jsonify(updated_project.put_into_dto()), 200
            return jsonify({"error": "Проєкт не знайдено"}), 404
        except SQLAlchemyError as e:
            return jsonify({"error": "Database error", "details": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def delete_project(project_id):
        try:
            service = ProjectService()
            success = service.delete_project(project_id)
            if success:
                return jsonify({"message": f"Проєкт з ID {project_id} успішно видалено"}), 200
            return jsonify({"error": "Проєкт не знайдено"}), 404
        except SQLAlchemyError as e:
            return jsonify({"error": "Database error", "details": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_vacancies_by_project(project_id):
        try:
            service = ProjectService()
            vacancies = service.get_project_vacancies(project_id)
            result = [vacancy.put_into_dto() for vacancy in vacancies]
            return jsonify(result), 200
        except SQLAlchemyError as e:
            return jsonify({"error": "Database error", "details": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_contacts_by_project(project_id):
        try:
            service = ProjectService()
            contacts = service.get_project_contacts(project_id)
            result = [contact.put_into_dto() for contact in contacts]
            return jsonify(result), 200
        except SQLAlchemyError as e:
            return jsonify({"error": "Database error", "details": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def add_project_via_procedure():
        try:
            data = request.get_json() or {}
            service = ProjectService()
            created_project = service.add_project_via_procedure(data)
            dto = created_project.put_into_dto() if created_project else {"status": "inserted"}
            return jsonify({"message": "Проєкт додано через процедуру", "project": dto}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except SQLAlchemyError as e:
            return jsonify({"error": "Database error", "details": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def link_project_contact():
        try:
            data = request.get_json() or {}
            service = ProjectService()
            service.link_project_contact_by_fullname(data)
            return jsonify({"message": "Зв'язок проєкту та контакту створено через процедуру"}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except SQLAlchemyError as e:
            return jsonify({"error": "Database error", "details": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def insert_ten_nonames():
        try:
            data = request.get_json() or {}
            start_num = data.get("start_num", request.args.get("start_num", 1))
            service = ProjectService()
            service.insert_ten_nonames(start_num)
            return jsonify({"message": f"Додано 10 записів Noname починаючи з {start_num}"}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except SQLAlchemyError as e:
            return jsonify({"error": "Database error", "details": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_max_project_id():
        try:
            service = ProjectService()
            max_id = service.get_max_project_id_via_procedure()
            return jsonify({"max_project_id": max_id}), 200
        except SQLAlchemyError as e:
            return jsonify({"error": "Database error", "details": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def split_projects_with_cursor():
        try:
            service = ProjectService()
            tables = service.split_projects_with_cursor()
            return jsonify({"message": "Таблиці створено та дані розподілено курсором", "tables": tables}), 201
        except SQLAlchemyError as e:
            return jsonify({"error": "Database error", "details": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500