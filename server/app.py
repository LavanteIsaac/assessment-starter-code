from flask import request, make_response

from config import app, db, api
from models import Project
from flask_restful import Resource

import ipdb

@app.route('/projects', methods= ["GET"])
def all_projects():
    projects= Project.query.all()
    projects_list = [project.to_dict() for project in projects]
     
    return make_response(projects_list), 200

@app.route('projects/<int:id>', methods= ['DELETE'])
def project_by_id(id):
    project = Project.query.get(id)
    if project is None:
        return make_response({'error:' 'No project'})

    elif request.method == 'DELETE':
        db.session.delete(project)
        db.session.commit()

        return make_response('', 204)
    
        
    
