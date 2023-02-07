import flask

app = flask.Flask(__name__)

import objects

from pages.system.member import view




@app.route("/", methods=["GET", "POST"])
def index():
    return None


app.run(host="0.0.0.0", port=81)
