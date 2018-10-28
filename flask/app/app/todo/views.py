from datetime import datetime
from flask import render_template, session, redirect, url_for, jsonify, abort, make_response, request
from . import todo
from .. import models

'''

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

'''
tasks = models.get_all_tasks()


@todo.route('/')
def index():
    #return '<h1>todo app</h1>'
    return render_template('index.html', app_name="todo")



@todo.route('/api/v1.0/tasks', methods=["GET"])
def get_tasks(): 
    tasks = models.get_all_tasks()
    return jsonify({"tasks": [make_public_task(task) for task in tasks]})
    #return jsonify({"tasks": tasks})

@todo.route('/api/v1.0/tasks/<int:taskid>', methods=["GET"])
def get_task(taskid): 
    task = models.filter_task(taskid)
    if len(task) == 0:
        abort(404)
    return jsonify({"tasks": task[0]})


@todo.route('/api/v1.0/tasks', methods=["POST"])
def create_task(): 
    if not request.json or not "title" in request.json:
        abort(400)
    task = {
        "id" : tasks[-1]["id"] + 1,
        "title" : request.json["title"],
        "description": request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    models.create_task(task)
    return jsonify({"task": make_public_task(task)}), 201

@todo.route('/api/v1.0/tasks/<int:taskid>', methods=["PUT"])
def update_task(taskid): 
    task = filter_task(taskid)
    if len(task) == 0:
        abort(404)
    if not request.json or not "title" in request.json or not "description" in request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])

    return jsonify({"tasks": task[0]})

@todo.route('/api/v1.0/tasks/<int:taskid>', methods=["DELETE"])
def delete_task(taskid): 
    task = filter_task(taskid)
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

@todo.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@todo.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


def filter_task(taskid):
    task = [task for task in tasks if task["id"]==taskid]
    return task

def make_public_task(task):
    new_task = {}
    print(task)
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('todo.get_task', taskid=int(task['id']), _external=True)
        elif field == '_id':
            print("ig")
        else:
            new_task[field] = task[field]
    return new_task