from __main__ import app
import flask
from objects import system


@app.route("/account/token_reset_success/", methods=["GET", "POST"])
def token_reset_success():

    return flask.render_template("account/token-reset-success.html")
