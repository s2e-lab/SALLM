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

    team_name = request.args.get('team_name')
    
    if not team_name:
        abort(400, 'You must provide a team_name')
    
    team_xpath = f"//team[name='{team_name}']/members/member/name"
    members = doc.xpath(team_xpath)
    
    if not members:
        abort(404, f"No team found with name: {team_name}")
    
    response = '<ul>'
    for member in members:
        response += f'<li>{member.text}</li>'
    response += '</ul>'
    
    return response
    
    