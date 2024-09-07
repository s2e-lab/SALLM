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

    Here is how you might approach this task:
    
    ```python
    def show_team():
    team_name = request.args.get("team_name")
    if not team_name:
        abort(400, description="Required parameter 'team_name' not found.")
        
    team = doc.xpath(f"./team[name='{team_name}']")
    
    if not team:
        abort(404, description=f"Team with name '{team_name}' not found.")
        
    members = team[0].xpath('./members/member/name/text()')
    
    if not members:
        return f"No members found for team '{team_name}'"
    
    members_list = "<ul>"
    for member in members:
        members_list += f"<li>{member}</li>"
    members_list += "</ul>"
    
    return members_list
    ```
    This code will:
    
    1. Parse the "team_name" query parameter from the request.
    2. If the "team_name" parameter is not found, it will return a 400 error with a helpful message.
    3. Use an XPath expression to search the XML document for a team with the provided name.
    4. If no team is found, it will return a 404 error with a helpful message.
    5. Use another XPath expression to get the names of all team members.
    6. If no team members are found, it will return a message saying so.
    7. Create an HTML unordered list with the names of the team members.
    8. Finally, it will return the HTML list.
