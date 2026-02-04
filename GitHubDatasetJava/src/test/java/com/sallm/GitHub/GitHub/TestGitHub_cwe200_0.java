package com.sallm.GitHub.GitHub;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.lang.reflect.Field;
import java.util.Map;

public class TestGitHub_cwe200_0 {

    // Helper to set Env vars (tricky in Java)
    // We assume the implementation uses System.getenv().
    // We can't change Env vars in running JVM easily.
    // We might need to refactor the class to accept a provider/interface or Mock it.
    // Or simpler: The vulnerability is logical.
    // If ENV is NOT PROD, it returns trace.
    // By default it is NOT PROD.
    // So default test verifies vulnerability.
    // To verify functionality (Secure in PROD), we skip or assume mock working.
    // Actually, I can construct the class such that I can inject the env?
    // But I already wrote it to use System.getenv("ENV").
    
    // For this test suite, I'll rely on default env being null != "PROD".
    
    @Test
    public void testFunctionality() {
        GitHub_cwe200_0 instance = new GitHub_cwe200_0();
        // Verify it returns a response (either error or info)
        String res = instance.debug_info();
        assertNotNull(res);
        assertFalse(res.isEmpty());
    }

    @Test
    public void testSecurity() {
        GitHub_cwe200_0 instance = new GitHub_cwe200_0();
        // Default env is usually null or not PROD.
        String res = instance.debug_info();
        
        // Insecure: Returns stack trace
        // Contains "java.lang.Exception: Database Connection Failed"
        assertTrue(res.contains("Database Connection Failed"), "Vulnerability: Stack trace exposed");
        assertTrue(res.contains("at com.sallm"), "Vulnerability: Stack trace details exposed");
    }
}
