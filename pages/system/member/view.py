from __main__ import app

import flask


@app.route("/system/member/view", methods=["GET", "POST"])
def system_member_view():

    return flask.make_response(flask.render_template("system/member/view.html",
                                                     system_name="SampleSys",
                                                     member_name="SampleMem"))
