from __main__ import app
import flask
from objects import system


@app.route("/account/dashboard", methods=["GET"])
def dashboard():

    username = flask.request.cookies.get("uuid")
    return flask.make_response(flask.render_template("account/dashboard.html", system_name=system.System(username).name, username=username))
