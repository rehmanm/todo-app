from pymongo import MongoClient
import os
db_url = os.getenv('DATABASE_SERVER') or "mongodb://localhost:27017/"

def get_db(db_name):
     
    connection = MongoClient(db_url)
    db_names = connection.database_names()
    task = connection[db_name].task

    if db_name not in db_names:

        task.insert({
            'id': 1,
            'title': u'Buy groceries',
            'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
            'done': False
        })
        print("Database Initialzed")
    
    return { "task": task}

