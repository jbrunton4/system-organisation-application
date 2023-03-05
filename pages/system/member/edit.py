from __main__ import app
from objects.member import Member, MemberNotFoundException

import flask


@app.route("/system/member/edit", methods=["GET", "POST"])
def system_member_edit() -> flask.Response:
    member_uuid = flask.request.args.get("id")
    try:
        member = Member(member_uuid)
    except MemberNotFoundException:
        return flask.make_response(flask.render_template("errors/404.html"))

    if flask.request.method == "POST":
        member.name = flask.request.form["name"]
        member.pronouns = flask.request.form["pronouns"]
        member.description = flask.request.form["description"]
        member.extra_info = flask.request.form["extra_info"]
        member.role = flask.request.form["role"]
        member.start_tag = flask.request.form["start_tag"]
        member.end_tag = flask.request.form["end_tag"]
        member.typing_quirk = flask.request.form["typing_quirk"]
        member.age = flask.request.form["age"]
        member.age_category = flask.request.form["age_category"]
        member.profile_picture_url = flask.request.form["avatar_url"]
        member.banner_url = flask.request.form["banner_url"]
        member.color_1 = flask.request.form["color_1"]
        member.color_2 = flask.request.form["color_2"]

        member.save_data()

    return flask.make_response(flask.render_template("system/member/edit.html",
                                                     uuid=member.get_uuid(),
                                                     color_1=member.color_1,
                                                     color_2=member.color_2,
                                                     name=member.name,
                                                     pronouns=member.pronouns,
                                                     role=member.role,
                                                     start_tag=member.start_tag,
                                                     end_tag=member.end_tag,
                                                     typing_quirk=member.typing_quirk,
                                                     age=member.age,
                                                     age_category=member.age_category,
                                                     avatar_url=member.profile_picture_url,
                                                     banner_url=member.banner_url,
                                                     description=member.description,
                                                     extra_info=member.extra_info))
