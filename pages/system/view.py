from __main__ import app
import flask
from objects.system import System, SystemNotFoundException
from objects.member import Member, MemberNotFoundException


@app.route("/system/view", methods=["GET", "POST"])
def system_view():
    system_uuid = flask.request.args.get("id")
    try:
        system = System(system_uuid)
    except SystemNotFoundException:
        return flask.make_response(flask.render_template("errors/400.html"))  # @todo: Make error 400 bad request

    profile_picture_url = system.profile_picture_url
    banner_url = system.banner_url

    if profile_picture_url == "":
        profile_picture_url = flask.url_for("static", filename="images/default_avatar.png")
    if banner_url == "":
        banner_url = flask.url_for("static", filename="images/default_banner.png")

    # get and format member list
    member_list = []
    print(system.get_members())
    for m in system.get_members():
        try:
            member_list.append(Member(m))
        except MemberNotFoundException as e:
            print(e)

    member_list_html = "<ul>"
    for m in member_list:
        member_list_html += f"<li><a href='/system/member/view?id={m.get_uuid()}'>{m.start_tag}{m.name}{m.end_tag}</a></li>"
    member_list_html += "</ul>"

    return flask.make_response(flask.render_template("system/view.html",
                                                     system_name="SampleSys",
                                                     member_name="SampleMem",
                                                     name=system.name,
                                                     system_tag=system.system_tag,
                                                     description=system.description,
                                                     banner_url=banner_url,
                                                     profile_picture_url=profile_picture_url,
                                                     member_list=flask.Markup(member_list_html),
                                                     color_1=system.color_1,
    color_2=system.color_2))

