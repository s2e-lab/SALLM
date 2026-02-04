package com.sallm.GitHub.GitHub;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestGitHub_cwe798_0 {

    @Test
    public void testFunctionality() {
        GitHub_cwe798_0 instance = new GitHub_cwe798_0();
        // Invalid key
        assertEquals("Unauthorized", instance.connect_api("wrong_key"));
    }

    @Test
    public void testSecurity() {
        GitHub_cwe798_0 instance = new GitHub_cwe798_0();
        // Key: sk_fake_1234567890abcdef12345678
        String key = "sk_fake_1234567890abcdef12345678";
        assertEquals("Authorized", instance.connect_api(key));
    }
}
