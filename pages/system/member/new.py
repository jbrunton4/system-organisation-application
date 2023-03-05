from __main__ import app
from objects.member import Member
from objects.system import System, SystemNotFoundException

import flask


@app.route("/system/member/new", methods=["GET", "POST"])
def system_member_new():
    system_id = flask.request.args.get("system_id")

    try:
        s = System(system_id)
    except SystemNotFoundException:
        return flask.make_response(flask.render_template("errors/403.html"))

    # validate login info
    token = flask.request.cookies.get("token")
    if not s.validate_token(token):
        return flask.make_response(flask.render_template("errors/403.html"))

    new_member = Member()
    new_member.save_data()
    s.add_member(new_member.get_uuid())
    s.save_data()

    return flask.redirect(f"/system/member/edit?id={new_member.get_uuid()}")
