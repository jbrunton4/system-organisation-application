from __main__ import app
import flask
from objects import system


@app.route("/account/signup", methods=["GET", "POST"])
def signup():
    if flask.request.method == "POST":

        if system.exists(flask.request.form["username"]):
            return flask.render_template("account/signup.html",
                                         status=flask.Markup(f"<font style='color: #ff0000;'>Username taken!</font>"))

        if flask.request.form["password"] != flask.request.form["password_repeat"]:
            return flask.render_template("account/signup.html",
                                         status=flask.Markup(
                                             f"<font style='color: #ff0000;'>Passwords don't match!</font>"))

        new_system = system.System()
        new_system.username = flask.request.form["username"]
        new_system.password = flask.request.form["password"]
        new_system.save_data()

        res = flask.make_response(flask.redirect("/system/edit"))
        res.set_cookie("uuid", new_system.get_username(), secure=True)
        res.set_cookie("token", new_system.token, secure=True)
        return res

    return flask.render_template("account/signup.html",
                                 status="")

# @todo: Make member edit page
# @todo: Password change page
