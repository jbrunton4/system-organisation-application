import flask

app = flask.Flask(__name__)

import objects

from pages.system.member import view
from pages.system import view, edit
from pages.account import signup, welcome
from error_handler import error_404



@app.route("/", methods=["GET", "POST"])
def index():
    return None


app.run(host="0.0.0.0", port=81)
