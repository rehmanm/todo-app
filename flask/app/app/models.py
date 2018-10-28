from . import db


def get_all_tasks():

    task_list = []
    for row in db["task"].find():
        task_list.append(row) 

    return task_list


def filter_task(taskid):
    task_list = []
    for row in db["task"].find({"id": taskid}, {"_id": 0}):
        task_list.append(row) 
    return task_list

def create_task(task):
    return db["task"].insert(task)