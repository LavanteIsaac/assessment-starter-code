from flask import request, make_response

from config import app, db, api
from models import Project
from flask_restful import Resource

import ipdb

@app.route('/projects', methods= ["GET"])
def all_projects():
    projects= Project.query.all()
    projects_list = [project.to_dict() for projects in projects]
     
    return make_response(project_list), 200

@app.route('projects/<int:id>', methods= ['DELETE'])
def project_by_id(id):
    project = Project.query.all()
    if request.method == 'DELETE':
        db.session.delete(project)
        db.session.commit()

        return make_response('', 204)
    elif project is None:
        return make_response({'error:' 'No project'})
    
