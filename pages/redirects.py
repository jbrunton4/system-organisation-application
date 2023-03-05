from __main__ import app
import flask


@app.route("/login", methods=["GET"])
def login_redirect():
    return flask.redirect("/account/login")


@app.route("/sys/", defaults={"u_path": ""})
@app.route("/sys/<path:u_path>")
def catchall_system_view(u_path):
    return flask.redirect(f"/system/view?id={u_path}")
