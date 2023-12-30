from flask import Flask, render_template, request, redirect
from app import app
from apps.crud.models import Todo
from apps import db

# app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def my_todo():
    if request.method == 'POST':
        title = (request.form['title'])
        des = (request.form['des'])
        todo = Todo(title=title, des=des)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)


@app.route('/update')
def update():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'this is products'

@app.route('/delete/<int:sno>')
def delete(sno):
    todo= Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")