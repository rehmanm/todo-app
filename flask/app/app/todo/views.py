from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import todo


print ('Adding Todo Routes')
@todo.route('/todo/')
def index():
    #return '<h1>todo app</h1>'
    return render_template('index.html', app_name="todo")




