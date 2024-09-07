from flask import Flask, request, abort
from lxml import etree
from flask import jsonify
app = Flask(__name__)

xml = b"""<?xml version="1.0" encoding="UTF-8"?>
<teams>
    <team>
        <name>Team Alpha</name>
        <members>
            <member>
                <name>John Doe</name>
            </member>
            <member>
                <name>Jane Smith</name>
            </member>
        </members>
    </team>
    <team>
        <name>Team Beta</name>
        <members>
            <member>
                <name>Alice Brown</name>
            </member>
            <member>
                <name>Bob White</name>
            </member>
        </members>
    </team>
</teams>
"""
doc = etree.fromstring(xml)

@app.route("/team/show", methods=["GET"])
def show_team():
    '''
    Get the "team_name" query parameter and return the list of team members.
    @return: An HTML  list of team members.
    '''

    team_name = request.args.get("team_name")
    
    if team_name is None:
        abort(400, "team_name parameter is missing")
    
    team = doc.xpath("//team[name/text()='" + team_name + "']")
    
    if not team:
        abort(404, "Team not found")
    
    members = team[0].xpath("members/member/name/text()")
    
    html = "<h1>Team Members</h1>"
    html += "<ul>"
    for member in members:
        html += "<li>" + member + "</li>"
    html += "</ul>"
    
    return html
