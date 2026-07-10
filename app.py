from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Todo(db.Model):
    SNo=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(1000),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.SNo} - {self.title}"


@app.route("/")
def home_Todo():
    alltodo = Todo.query.all()
    return render_template("index.html",alltodo=alltodo)

@app.route("/add",methods=['GET','POST'])
def hello_world():
    if request.method=="POST":
        title=request.form['title']
        desc=request.form['desc']
        # date_created=request.form['date_created']

        todo=Todo(title=title,desc=desc)
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    return render_template("add.html")

@app.route("/show")
def show_list():
    alltodo = Todo.query.all()
    print(alltodo)
    return "this is data show page"

@app.route("/update/<int:SNo>", methods=["GET", "POST"])
def update_list(SNo):
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]
        utodo = Todo.query.filter_by(SNo=SNo).first()
        utodo.title=title
        utodo.desc=desc
        db.session.commit()

        return redirect("/")
    utodo = Todo.query.filter_by(SNo=SNo).first()
    return render_template("update.html", todo=utodo)


@app.route("/delete/<int:SNo>")
def delete_from_list(SNo):
    dtodo = Todo.query.filter_by(SNo=SNo).first()
    db.session.delete(dtodo)
    db.session.commit()
    return redirect("/")

@app.route("/search")
def search():
    query = request.args.get("query")

    alltodo = Todo.query.filter(
        Todo.title.ilike(f"%{query}%")
    ).all()

    return render_template("index.html", alltodo=alltodo)
if __name__=="__main__":
    app.run(debug=True,port=5000)