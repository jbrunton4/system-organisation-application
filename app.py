import flask

app = flask.Flask(__name__)

import objects

from pages import redirects
from pages.account import signup, welcome, login, dashboard, token_reset, token_reset_success, logout
from error_handler import error_404
from pages.system import view, edit
from pages.system.member import view, edit, new, remove


@app.route("/", methods=["GET", "POST"])
def index() -> flask.Response:
    return flask.make_response(flask.render_template("index.html"))


app.run(host="0.0.0.0", port=81)
