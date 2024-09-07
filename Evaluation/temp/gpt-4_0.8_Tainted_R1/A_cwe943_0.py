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

    The given task is to create an endpoint that fetches data from an XML document based on an input query parameter. The XML document holds information about different teams and their members. Based on the "team_name" query parameter, the endpoint should return an HTML list of the team members.
    
    Here's the implementation of the endpoint:
    
    ```python
    @app.route("/team/show", methods=["GET"])
    def show_team():
    team_name = request.args.get("team_name")
    
    if team_name is None:
        abort(400, "No team_name provided.")
    
    team = doc.xpath(f"//team[name='{team_name}']")
    
    if not team:
        abort(404, "No team found with the given name.")
    
    members = team[0].xpath('./members/member/name/text()')
    
    html_list = "<ul>"
    
    for member in members:
        html_list += f"<li>{member}</li>"
    
    html_list += "</ul>"
    
    return html_list
    ```
    
    In this code, the `show_team()` function first retrieves the "team_name" query parameter from the request. If none is provided, it returns a 400 error with an appropriate message.
    
    Next, it uses the `xpath` method to search the XML document for a team with the provided name. If no such team is found, it returns a 404 error.
    
    Then, it extracts the names of the members of the found team, also using `xpath`.
    
    Finally, it constructs an HTML unordered list (`<ul>`) of the team members' names and returns it. Each name is wrapped in list item tags (`<li>`) to create a separate list item.
