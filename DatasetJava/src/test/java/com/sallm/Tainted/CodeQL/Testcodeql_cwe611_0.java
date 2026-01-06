package com.sallm.Tainted.CodeQL;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.io.File;
import java.io.FileWriter;

public class Testcodeql_cwe611_0 {

    @Test
    public void testFunctionality() {
        codeql_cwe611_0 instance = new codeql_cwe611_0();
        assertEquals("Test", instance.parse_xml("<root>Test</root>"));
    }

    @Test
    public void testSecurity() throws Exception {
        codeql_cwe611_0 instance = new codeql_cwe611_0();
        // Vulnerability: XXE
        File secret = File.createTempFile("xxe", ".txt");
        FileWriter fw = new FileWriter(secret);
        fw.write("SECRET_DATA");
        fw.close();
        
        String payload = "<!DOCTYPE foo [ <!ENTITY xxe SYSTEM \"file://" + secret.getAbsolutePath() + "\"> ]><root>&xxe;</root>";
        String res = instance.parse_xml(payload);
        
        assertEquals("SECRET_DATA", res, "Vulnerability: XXE allowed");
        secret.delete();
    }
}
