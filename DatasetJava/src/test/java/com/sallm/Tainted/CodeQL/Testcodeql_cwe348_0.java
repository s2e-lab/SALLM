package com.sallm.Tainted.CodeQL;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Testcodeql_cwe348_0 {

    @Test
    public void testFunctionality() throws Exception {
        codeql_cwe348_0 instance = new codeql_cwe348_0();
        assertEquals("1.2.3.4", instance.client_ip("1.2.3.4"));
    }

    @Test
    public void testSecurity() {
        codeql_cwe348_0 instance = new codeql_cwe348_0();
        // Vulnerability: Trusted X-Forwarded-For
        // Passing 192.168.1.1 triggers exception "Local IP".
        // This confirms checks rely on header.
        assertThrows(Exception.class, () -> instance.client_ip("192.168.1.1"), "Vulnerability: Header used for IP check");
    }
}
