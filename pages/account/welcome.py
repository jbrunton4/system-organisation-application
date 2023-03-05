from __main__ import app
import flask


@app.route("/account/welcome", methods=["GET", "POST"])
def welcome() -> flask.Response:
    if flask.request.method == "POST":
        return flask.make_response(flask.redirect(f"/system/view?id={flask.request.cookies.get('uuid')}"))

    return flask.make_response(flask.render_template("account/welcome.html"))
