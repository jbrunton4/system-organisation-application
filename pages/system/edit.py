from __main__ import app
import flask
from objects import system, member


@app.route("/system/edit", methods=["GET", "POST"])
def edit_system():

    system_uuid = flask.request.cookies.get("uuid")  # @todo: Cookie UUID and token on login.
    if not system.System(system_uuid).token == flask.request.cookies.get("token"):
        return flask.make_response(flask.redirect("/account/login"))

    s = system.System(flask.request.cookies.get("uuid"))

    if flask.request.method == "POST":
        if flask.request.form["submit"] == "save":
            s.name = flask.request.form["system_name"]
            s.system_tag = flask.request.form["system_tag"]
            s.color_1 = flask.request.form["color_1"]
            s.color_2 = flask.request.form["color_2"]
            s.profile_picture_url = flask.request.form["avatar_url"]
            s.banner_url = flask.request.form["banner_url"]
            s.save_data()

    table_content = ""
    for m in s.get_members():
        m = member.Member(m)

        table_content += f"<tr><td>{m.start_tag}{m.name}{m.end_tag}</td>" \
                         f"<td style='text-align: right;'><button style='padding: 5px; border-radius: 4px; type='submit' name='edit_{m.get_uuid()}'>Edit</button></td>" \
                         f"<td><button style='padding: 5px; border-radius: 4px; border: 1px solid #f00; color: #f00' type='submit' name='remove_{m.get_uuid()}'>Remove</button></td></tr>"

    return flask.make_response(flask.render_template("system/edit.html",
                                                     system_name=s.name,
                                                     username=s.username,
                                                     system_tag=s.system_tag,
                                                     color_1=s.color_1,
                                                     color_2=s.color_2,
                                                     avatar_url=s.profile_picture_url,
                                                     banner_url=s.banner_url,
                                                     table_content=flask.Markup(table_content)
                                                     ))
