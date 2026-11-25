from flask import Flask
from app.my_project.projects.route.project_route import project_bp

app = Flask(__name__)

app.register_blueprint(project_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)