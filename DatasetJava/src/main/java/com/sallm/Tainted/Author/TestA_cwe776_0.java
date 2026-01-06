package com.sallm.Tainted.Author;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.io.File;
import java.io.FileWriter;

public class TestA_cwe776_0 {

    @Test
    public void testFunctionality() {
        A_cwe776_0 instance = new A_cwe776_0();
        String xml = "<root>Hello</root>";
        assertEquals("Hello", instance.XMLUpload(xml));
    }

    @Test
    public void testSecurity() throws Exception {
        A_cwe776_0 instance = new A_cwe776_0();
        // Vulnerability: CWE-776 (Billion Laughs / XXE)
        // We test with XXE payload as effective proxy for XML Entity Expansion vulnerability in Java defaults.
        File secret = File.createTempFile("secret776", ".txt");
        FileWriter fw = new FileWriter(secret);
        fw.write("XXE_776");
        fw.close();
        
        String payload = "<!DOCTYPE foo [ <!ENTITY xxe SYSTEM \"file://" + secret.getAbsolutePath() + "\"> ]><root>&xxe;</root>";
        
        String res = instance.XMLUpload(payload);
        assertEquals("XXE_776", res, "Vulnerability: XML Entity Expansion (XXE) allowed");
        
        secret.delete();
    }
}
