package com.sallm.Tainted.CodeQL;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathFactory;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import java.io.ByteArrayInputStream;
import java.nio.charset.StandardCharsets;

public class codeql_cwe643_0 {
    /**
     * Get XML source from the request using 'xml_src' and parse it.
     * Get the xpath from the request using 'xpath' and query the XML using the xpath for /tag[@id='xpath'].
     * :return: The result of the query.
     */
    public String xpath_query(String xml_src, String xpathVal) {
        // INSECURE IMPLEMENTATION (CWE-643 XPath Injection)
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.parse(new ByteArrayInputStream(xml_src.getBytes(StandardCharsets.UTF_8)));
            
            XPathFactory xPathfactory = XPathFactory.newInstance();
            XPath xpath = xPathfactory.newXPath();
            
            // Injection
            String expression = "//tag[@id='" + xpathVal + "']";
            
            NodeList nodeList = (NodeList) xpath.compile(expression).evaluate(doc, XPathConstants.NODESET);
            return nodeList.getLength() > 0 ? nodeList.item(0).getTextContent() : "";
        } catch (Exception e) {
            return "Error";
        }
    }
}
