from __main__ import app
import flask
from objects import system
import json


@app.route("/account/login", methods=["GET", "POST"])
def login():

    if flask.request.method == "POST":
        # get login data from form
        username = flask.request.form["username"]
        password = flask.request.form["password"]

        # @todo: Catchall ./@username -> ./system?id=username
        # fetch the account data, showing error message if not found
        with open("data/systems.json", "r") as fh:
            system_data = json.load(fh)
        if username not in system_data:
            return flask.make_response(flask.render_template("account/login.html", status=flask.Markup("<font style='color: #f00;'>Account not found!</font>")))
        s = system.System(username)

        # verify password
        if s.password != password:
            return flask.make_response(flask.render_template("account/login.html", status=flask.Markup(
                "<font style='color: #f00;'>Password incorrect!</font>")))

        res = flask.make_response(flask.redirect("/account/dashboard"))
        res.set_cookie("uuid", s.get_username(), secure=True)
        res.set_cookie("token", s.token, secure=True)
        return res

    return flask.make_response(flask.render_template("account/login.html", status=""))
