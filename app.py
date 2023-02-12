import flask

app = flask.Flask(__name__)

import objects

from pages.system.member import view
from pages.system import view, edit
from pages.account import signup, welcome, login, dashboard, token_reset, token_reset_success, logout
from error_handler import error_404


@app.route("/", methods=["GET", "POST"])
def index():
    return flask.make_response(flask.render_template("index.html"))


# @todo: Make an "about" page - devs, policies, upcoming features, version
# @todo: Make "redirects" under ./pages
app.run(host="0.0.0.0", port=81)
