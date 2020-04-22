from app import app, db
from flask import render_template, url_for, redirect, request
from app.models import Todo


@app.route('/')
def index():
	incompletes = Todo.query.filter_by(complete=False).all()
	completes = Todo.query.filter_by(complete=True).all()
	return render_template('index.html', completes=completes, incompletes=incompletes)


@app.route('/add', methods=['POST'])
def add():
	todo = Todo(text=request.form['todoitem'], complete=False)
	db.session.add(todo)
	db.session.commit()
	return redirect(url_for('index'))


@app.route('/complete/<id>')
def complete(id):
	todo = Todo.query.filter_by(id=int(id)).first()
	if todo.complete:
		todo.complete = False
	else:
		todo.complete = True	
	db.session.commit()
	return redirect(url_for('index'))