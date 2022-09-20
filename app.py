from distutils.log import debug
from flask import Flask ,render_template ,request  ,  redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = "False"
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)  
db.create_all()

@app.route("/")
def  index():
    #show all todos
    todo_list = Todo.query.all()
    return render_template("base.html",todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    #add new todo
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))  

    
@app.route("/update/<todo_id>")
def update(todo_id):
    #add new todo
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    # db.session.delete()
    db.session.commit()
    return redirect(url_for("index"))  



@app.route("/delete/<todo_id>")
def delete(todo_id):
    #add new todo
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))  