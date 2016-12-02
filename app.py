import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient


app = Flask(__name__)
client  = MongoClient(os.environ['DOCKERPYTODO_DB_1_PORT_27017_TCP_ADDR'], 27017)
# client = MongoClient()   # Run app locally
db = client.tododb


@app.route('/')
def todo():
    # return "Hello"
    cursor = db.todo.find()
    items = [item for item in cursor]
    return render_template('todo.html', items = items)


@app.route('/new', methods=['POST'])
def new():
    item_doc ={
        'name': request.form['name'],
        'description' : request.form['description']
    }
    db.todo.insert_one(item_doc)
    return redirect(url_for('todo'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
