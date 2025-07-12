from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# 📘 Modelo de Tarefa
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    status = db.Column(db.String(50), default="Pendente")
    prazo_entrega = db.Column(db.Date)


# 📄 Página Principal com filtro opcional
@app.route("/")
def index():
    status_filter = request.args.get("status")
    tasks = (
        db.session.query(Task).filter_by(status=status_filter).all()
        if status_filter
        else db.session.query(Task).all()
    )
    return render_template("index.html", tasks=tasks)


# ➕ Criar nova tarefa
@app.route("/create", methods=["POST"])
def create():
    title = request.form.get("title")
    description = request.form.get("description", "")
    status = request.form.get("status", "Pendente")
    prazo = request.form.get("prazo_entrega")

    try:
        prazo_date = datetime.strptime(prazo, "%Y-%m-%d").date() if prazo else None
    except ValueError:
        prazo_date = None

    if title:
        new_task = Task(
            title=title,
            description=description,
            status=status,
            prazo_entrega=prazo_date,
        )
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for("index"))


# ✏️ Atualizar tarefa
@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    task = db.session.get(Task, id)
    if not task:
        return "Tarefa não encontrada", 404

    task.title = request.form.get("title", task.title)
    task.description = request.form.get("description", task.description)
    task.status = request.form.get("status", task.status)
    prazo = request.form.get("prazo_entrega")

    try:
        task.prazo_entrega = (
            datetime.strptime(prazo, "%Y-%m-%d").date() if prazo else None
        )
    except ValueError:
        pass

    db.session.commit()
    return redirect(url_for("index"))


# ❌ Deletar tarefa
@app.route("/delete/<int:id>")
def delete(id):
    task = db.session.get(Task, id)
    if not task:
        return "Tarefa não encontrada", 404

    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("index"))


# 🚀 Inicialização
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
