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
    team_name = request.args.get("team_name")  # [1]
    if team_name is None:
        return jsonify({"message": "Team name missing"}), 400
    try:
        print("/teams/team[name='" + team_name + "']/members/member/name/text()")
        nodes = doc.xpath(
            "/teams/team[name='" + team_name + "']/members/member/name/text()"
        )  # [2]

        return jsonify({"message": "Team members: " + ", ".join(nodes)}), 200
    except etree.XPathEvalError as e:
        return jsonify({"message": "Failed to query XML: " + str(e)}), 500
