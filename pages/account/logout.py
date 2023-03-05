from __main__ import app
import flask
from objects import system


@app.route("/account/logout/", methods=["GET", "POST"])
def logout() -> flask.Response:
    if not system.exists(flask.request.cookies.get("uuid")):
        return flask.make_response(flask.render_template("account/logout-success.html"))

    print(flask.request.method)
    if flask.request.method == "POST":
        res = flask.make_response(flask.render_template("account/logout-success.html"))
        res.set_cookie("uuid", "", expires=0, secure=True)
        res.set_cookie("token", "", expires=0, secure=True)
        return res

    s = system.System(flask.request.cookies.get("uuid"))
    return flask.make_response(flask.render_template("account/logout.html", system_name=s.name))
