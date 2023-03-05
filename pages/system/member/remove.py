from __main__ import app
from objects.member import Member, MemberNotFoundException
from objects.system import System, SystemNotFoundException

import flask


@app.route("/system/member/remove", methods=["GET", "POST"])
def system_member_remove():

    system_id = flask.request.args.get("system_id")

    try:
        s = System(system_id)
    except SystemNotFoundException:
        return flask.make_response(flask.render_template("errors/403.html"))

    # validate login info
    token = flask.request.cookies.get("token")
    if not s.validate_token(token):
        return flask.make_response(flask.render_template("errors/403.html"))

    # get the member
    member_id = flask.request.args.get("member_id")
    try:
        m = Member(member_id)
    except MemberNotFoundException:
        return flask.make_response(flask.render_template("errors/403.html"))

    # remove the member
    s.remove_member(m.get_uuid())
    s.save_data()

    # @todo: Make a script to iterate through members and kill orphans

    return flask.redirect(f"/system/edit?id={s.get_uuid()}")
