from __main__ import app
import flask

"""
This script sets up demonstration error pages
To throw errors, return render_template("errors/xxx.html")
"""


@app.route("/errors/403", methods=["GET"])
def error_403_demo() -> flask.Response:
    return flask.make_response(flask.render_template("/errors/403.html"))


@app.route("/errors/404", methods=["GET"])
def error_404_demo() -> flask.Response:
    return flask.make_response(flask.render_template("/errors/404.html"))
