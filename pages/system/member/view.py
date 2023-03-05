from __main__ import app
from objects.member import Member, MemberNotFoundException

import flask


@app.route("/system/member/view", methods=["GET", "POST"])
def system_member_view() -> flask.Response:
    member_uuid = flask.request.args.get("id")
    try:
        member = Member(member_uuid)
    except MemberNotFoundException:
        return flask.make_response(flask.render_template("errors/404.html"))

    profile_picture_url = member.profile_picture_url
    banner_url = member.banner_url

    if profile_picture_url == "":
        profile_picture_url = flask.url_for("static", filename="images/default_avatar.png")
    if banner_url == "":
        banner_url = flask.url_for("static", filename="images/default_banner.png")
    return flask.make_response(flask.render_template("system/member/view.html",
                                                     system_name="SampleSys",
                                                     member_name="SampleMem",
                                                     name=member.name,
                                                     pronouns=member.pronouns,
                                                     age=member.age,
                                                     age_category=member.age_category,
                                                     role=member.role,
                                                     proxy_tags=flask.Markup(f"{member.start_tag}text{member.end_tag}"),
                                                     typing_quirk=member.typing_quirk,
                                                     description=member.description,
                                                     extra_info=flask.Markup(member.extra_info),
                                                     banner_url=banner_url,
                                                     profile_picture_url=profile_picture_url,
                                                     color_1=member.color_1,
                                                     color_2=member.color_2))
