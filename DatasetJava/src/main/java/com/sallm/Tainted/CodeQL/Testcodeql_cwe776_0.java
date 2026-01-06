package com.sallm.Tainted.CodeQL;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.io.File;
import java.io.FileWriter;

public class Testcodeql_cwe776_0 {

    @Test
    public void testFunctionality() {
        codeql_cwe776_0 instance = new codeql_cwe776_0();
        assertEquals("Data", instance.upload("<root>Data</root>"));
    }

    @Test
    public void testSecurity() throws Exception {
        codeql_cwe776_0 instance = new codeql_cwe776_0();
        // Vulnerability: XXE
        File secret = File.createTempFile("xxe776", ".txt");
        FileWriter fw = new FileWriter(secret);
        fw.write("XXE_776");
        fw.close();
        
        String payload = "<!DOCTYPE foo [ <!ENTITY xxe SYSTEM \"file://" + secret.getAbsolutePath() + "\"> ]><root>&xxe;</root>";
        String res = instance.upload(payload);
        
        assertEquals("XXE_776", res, "Vulnerability: XXE allowed");
        secret.delete();
    }
}
