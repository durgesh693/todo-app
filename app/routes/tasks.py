from flask import redirect, Blueprint, request, render_template, session, url_for, flash
from app import db
from app.models import task

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route("/")
def view_tasks():
    if "user" not in session:
        return redirect(url_for("auth.login"))
    
    tasks = task.query.all()
    return render_template("task.html", tasks=tasks) 

@tasks_bp.route("/add", methods=["POST"])
def add_task():
    if "user" not in session:
        return redirect(url_for("auth.login"))

    title = request.form.get("title")
    if title:
        new_task = task(title=title, status="pending")
        db.session.add(new_task)
        db.session.commit()
        flash("task added successfully","success")

    return redirect(url_for("tasks.view_tasks"))      

@tasks_bp.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_status(task_id):
    task_obj = task.query.get(task_id)
    if task_obj:
        if task_obj.status == "pending":
            task_obj.status = "working"
        elif task_obj.status == "working":
            task_obj.status = "done"
        else:
            task_obj.status = "pending"
        db.session.commit()
        flash(f"Task status updated to {task_obj.status}", "info")
    else:
        flash("Task not found", "danger")
    return redirect(url_for("tasks.view_tasks"))

@tasks_bp.route("/clear", methods=["POST"])
def clear_tasks():
    task.query.delete()
    db.session.commit()
    flash("all tasks cleared", "info")
    return redirect(url_for("tasks.view_tasks"))

 



