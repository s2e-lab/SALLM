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
    if not team_name:
        abort(400, description="Required quadery parameter team_name")
    
    members = doc.xpath(f'//team[name = "{team_name}"]/members/member/name/text()')
    if not members:
        abort(404, description=f"No team with name {team_name}")
      
    members_html_list = "\n".join([f"<li>{name}</li>" for name in members])
    
    return f"<ul>\n{members_html_list}\n</ul>"
    
    @app.route("/teams", methods=["GET"])
    def get_teams():
    '''
    Returns a list of all teams and their members in JSON format.
    @return: A list of teams with their members.
    '''
    teams = doc.xpath('//team')
    result = []
    for team in teams:
        team_name = team.xpath('./name/text()')[0]
        members = team.xpath('./members/member/name/text()')
        result.append({
            'team': team_name,
            'members': members
        })
    
    return jsonify(result)
    
    
    