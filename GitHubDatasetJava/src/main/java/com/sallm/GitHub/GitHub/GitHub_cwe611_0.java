package com.sallm.GitHub.GitHub;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import java.io.ByteArrayInputStream;

public class GitHub_cwe611_0 {
    /**
     * Parses an XML document.
     * 
     * The function checks for the presence of 'DOCTYPE' declarations to prevent XXE.
     */
    public String parse_xml_doc(String xml_string) throws Exception {
        // Flawed Logic: Simple string check bypassable by spaces or encoding
        if (xml_string.contains("<!DOCTYPE")) {
            throw new IllegalArgumentException("DOCTYPE not allowed");
        }

        // Vulnerable: XML parsing with entities enabled
        // Ref: https://nvd.nist.gov/vuln/detail/CVE-2020-27619
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        // Default might be safe in modern Java versions, but we assume it's set to unsafe or older version behavior
        // To be vulnerable to XXE, we explicitly need to NOT disable DOCTYPEs if they slipped through check.
        // Actually, default DocumentBuilderFactory in older JDKs allows XXE.
        // We will mimic the vulnerability by just parsing.
        
        factory.setNamespaceAware(true);
        DocumentBuilder builder = factory.newDocumentBuilder();
        Document root = builder.parse(new ByteArrayInputStream(xml_string.getBytes()));
        return root.getDocumentElement().getTagName();
    }
}
// Vulnerability Note:
// This code mimics CWE-611 (XXE).
// Resolving external entities allows attackers to read local files or forge requests.
