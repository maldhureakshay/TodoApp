from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/todoapp'
mongo = PyMongo(app)

todos_collection = mongo.db.todos

@app.route('/')
def index():
    todos = todos_collection.find().sort("_id",-1)
    return render_template('index.html', todos=todos)

@app.route('/add_todo', methods=['POST'])
def add_todo():
    todo_item = request.form.get('add-todo')
    todos_collection.insert_one({'text' : todo_item})
    return redirect(url_for('index'))

@app.route('/delete_todo/<id>')
def delete_todo(id):
    print(id)
    todos_collection.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))
