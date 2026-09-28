from flask import Blueprint, request,flash, render_template, Response, url_for, session, redirect

auth_bp = Blueprint('auth', __name__)

user_credential ={
    "username" : "durgesh",
    "password" : "654321"
}

@auth_bp.route("/login", methods = ['GET','POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == user_credential["username"] and  password == user_credential["password"]:
            session["user"] = username
            flash("login successful","success")
            return redirect(url_for("tasks.view_tasks"))
        else:
            flash("invalid username or password", "danger")

    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.pop("user", None)
    flash("logged out", "info")
    return redirect(url_for("auth.login"))            

