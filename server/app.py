from flask import request, make_response, jsonify

from config import app, db, api
from models import Project
from flask_restful import Resource

import ipdb

@app.route('/projects', mehtods=['GET'])
def all_projects():
    projects = Project.query.all()
    projects = {project.to_dict() for project in projects}
    return jsonfiy(projects_list), 200

@app.route('/projects/<int:id>', methods= ['DELETE'])
def post_by_id(id):
    if request.method == 'DELETE':
        db.sessions.delete(project)
        db.sessions.commit()

        return make_response(' ', 204)
    elif project is None:
        return make_reponse(jsonfiy({'error': 'Project not found'}), 404)
