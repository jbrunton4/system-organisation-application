from __main__ import app
import flask


@app.errorhandler(404)
def not_found(e: Exception) -> flask.Response:
    return flask.make_response(flask.render_template("errors/404.html",
                                                     exception_details=e))
