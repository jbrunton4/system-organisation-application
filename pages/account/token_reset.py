from __main__ import app
import flask
from objects import system


@app.route("/account/reset_token/", methods=["GET", "POST"])
def reset_token():
    print(flask.request.method)
    if flask.request.method == "POST":
        res = flask.make_response(flask.redirect("/account/token_reset_success"))
        res.set_cookie("uuid", "", expires=0, secure=True)
        res.set_cookie("token", "", expires=0, secure=True)
        return res

    if not system.exists(flask.request.cookies.get("uuid")):
        return flask.redirect("/account/login")

    s = system.System(flask.request.cookies.get("uuid"))

    return flask.render_template("account/token-reset.html", system_name=s.name)
