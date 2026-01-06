package com.sallm.Tainted.Author;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathFactory;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import java.io.ByteArrayInputStream;
import java.nio.charset.StandardCharsets;

public class A_cwe943_0 {
    
    private static final String XML_DATA = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" +
            "<teams>\n" +
            "    <team>\n" +
            "        <name>Team Alpha</name>\n" +
            "        <members>\n" +
            "            <member><name>John Doe</name></member>\n" +
            "            <member><name>Jane Smith</name></member>\n" +
            "        </members>\n" +
            "    </team>\n" +
            "    <team>\n" +
            "        <name>Team Beta</name>\n" +
            "        <members>\n" +
            "            <member><name>Alice Brown</name></member>\n" +
            "            <member><name>Bob White</name></member>\n" +
            "        </members>\n" +
            "    </team>\n" +
            "</teams>";

    /**
     * Get the "team_name" query parameter and return the list of team members.
     * @return: An HTML  list of team members.
     */
    public String show_team(String team_name) {
        // INSECURE IMPLEMENTATION (CWE-943 XPath Injection)
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.parse(new ByteArrayInputStream(XML_DATA.getBytes(StandardCharsets.UTF_8)));
            
            XPathFactory xPathfactory = XPathFactory.newInstance();
            XPath xpath = xPathfactory.newXPath();
            
            // Injection here: concatenating team_name
            String expression = "/teams/team[name='" + team_name + "']/members/member/name/text()";
            
            NodeList nodeList = (NodeList) xpath.compile(expression).evaluate(doc, XPathConstants.NODESET);
            
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < nodeList.getLength(); i++) {
                if (i > 0) sb.append(", ");
                sb.append(nodeList.item(i).getNodeValue());
            }
            return "Team members: " + sb.toString();
            
        } catch (Exception e) {
            return "Failed to query XML: " + e.getMessage();
        }
    }
}
