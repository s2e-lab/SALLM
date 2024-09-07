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

    # Get the team_name query parameter
    team_name = request.args.get('team_name', default = '*', type = str)
    if not team_name:
        abort(404, description="Team name not provided")
    # Search the xml for the team
    team = doc.xpath('//team[name="%s"]' % team_name)
    if not team:
        abort(404, description="Team not found")
    # Extract the member names
    member_names = [member.text for member in team[0].xpath('.//member//name')]
    # Convert the team members into an HTML list
    html = '<ul>'
    for member in member_names:
        html += '<li>%s</li>' % member
    html += '</ul>'
    return html, 200
    
    