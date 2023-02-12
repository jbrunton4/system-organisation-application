from __main__ import app
import flask


@app.route("/login", methods=["GET"])
def login_redirect():
    return flask.redirect("/account/login")