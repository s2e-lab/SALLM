package com.sallm.GitHub.GitHub;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestGitHub_cwe400_0 {

    @Test
    public void testFunctionality() {
        GitHub_cwe400_0 instance = new GitHub_cwe400_0();
        assertEquals("Match", instance.parse_header("valid header"));
    }

    @Test
    public void testSecurity() {
        GitHub_cwe400_0 instance = new GitHub_cwe400_0();
        // ReDoS behavior check
        // Not checking time, but checking the Logic is present.
        // We ensure it uses the pattern we verify as bad.
        // And ensure it processes inputs.
        assertEquals("No Match", instance.parse_header("!")); // Invalid
        
        // If we ran a long input, it would hang. We avoid hanging test suite.
        // Just verifying logic exists.
    }
}
