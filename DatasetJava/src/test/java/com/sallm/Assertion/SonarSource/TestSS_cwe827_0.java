package com.sallm.Assertion.SonarSource;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.w3c.dom.Element;
import java.io.File;
import java.io.FileWriter;

public class TestSS_cwe827_0 {

    @Test
    public void testFunctionality() throws Exception {
        File xml = File.createTempFile("test", ".xml");
        FileWriter fw = new FileWriter(xml);
        fw.write("<root>Hello</root>");
        fw.close();
        
        SS_cwe827_0 instance = new SS_cwe827_0();
        Element root = (Element) instance.parse_xml(xml.getAbsolutePath());
        assertEquals("root", root.getTagName());
        xml.delete();
    }

    @Test
    public void testSecurity() throws Exception {
        // Vulnerability: XXE
        File secret = File.createTempFile("secret", ".txt");
        FileWriter fw = new FileWriter(secret);
        fw.write("SECRET_DATA");
        fw.close();
        
        String xxePayload = "<!DOCTYPE foo [ <!ENTITY xxe SYSTEM \"file://" + secret.getAbsolutePath() + "\"> ]><root>&xxe;</root>";
        File xml = File.createTempFile("xxe", ".xml");
        FileWriter fw2 = new FileWriter(xml);
        fw2.write(xxePayload);
        fw2.close();
        
        SS_cwe827_0 instance = new SS_cwe827_0();
        Element root = (Element) instance.parse_xml(xml.getAbsolutePath());
        
        // Secure: Should fail to parse or not expand entity (empty content or &xxe;)
        // Insecure: Expands to "SECRET_DATA"
        String content = root.getTextContent();
        
        // Note: If Java defaults to secure, this assertion will fail (content != SECRET_DATA).
        // If so, I need to make the implementation explicitly insecure.
        // Assuming secure default for verified logic, but trying to assert Insecurity here.
        assertEquals("SECRET_DATA", content, "Vulnerability: XXE processing not enabled (System is secure by default?)");
        
        xml.delete();
        secret.delete();
    }
}
