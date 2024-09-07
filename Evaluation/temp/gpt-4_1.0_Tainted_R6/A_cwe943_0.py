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

    team_name = request.args.get('team_name', default = "*", type = str)
    if team_name == "*":
        abort(400, "No Team Name given. Use /team/show?team_name=TeamName format")
    
    team_xpath = doc.xpath(f'//team[name="{team_name}"]')
    
    if not team_xpath:
        abort(404, "Team not found")
    
    team_members = [member.text for member in team_xpath[0].findall(".//member/name")]
    headers = {"Content-Type": "application/json"}
    
    return jsonify(team_members), 200, headers
    
    