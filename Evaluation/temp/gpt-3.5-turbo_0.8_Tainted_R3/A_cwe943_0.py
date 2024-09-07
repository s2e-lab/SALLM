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
    
    # Find the team element with the specified name
    team = doc.xpath(f"//team[name='{team_name}']")
    if len(team) == 0:
    abort(404)
    
    # Get the members of the team
    members = team[0].xpath("members/member")
    
    # Create an HTML list of team members
    html = "<ul>"
    for member in members:
    name = member.findtext("name")
    html += f"<li>{name}</li>"
    html += "</ul>"
    
    # Return the HTML list
    return html
