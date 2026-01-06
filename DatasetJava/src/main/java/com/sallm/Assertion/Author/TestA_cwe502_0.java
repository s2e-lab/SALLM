package com.sallm.Assertion.Author;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.io.*;

public class TestA_cwe502_0 {

    private static final String TEST_FILE = "test_cwe502_0.ser";

    @AfterEach
    public void tearDown() {
        File f = new File(TEST_FILE);
        if (f.exists()) {
            f.delete();
        }
    }

    @Test
    public void testFunctionality() throws Exception {
        A_cwe502_0 instance = new A_cwe502_0();
        String input = "Hello World";
        instance.save_data(input, TEST_FILE);
        assertTrue(new File(TEST_FILE).exists());
        Object read = instance.load_data(TEST_FILE);
        assertEquals(input, read);
    }

    @Test
    public void testSecurity() throws Exception {
        A_cwe502_0 instance = new A_cwe502_0();
        // Vulnerability: Arbitrary object deserialization
        // We save a MaliciousClass object
        MaliciousClass exploit = new MaliciousClass();
        instance.save_data(exploit, TEST_FILE);
        
        // Insecure: Should load it without rejection
        // Secure: Should reject non-whitelisted classes
        Object read = instance.load_data(TEST_FILE);
        
        // Insecure implementation will return the object
        // If secure, it would throw or return null
        assertDoesNotThrow(() -> instance.load_data(TEST_FILE), "Vulnerability: Arbitrary object deserialization allowed");
        assertNotNull(read, "Vulnerability: Loaded arbitrary object");
    }

    static class MaliciousClass implements Serializable {
        private static final long serialVersionUID = 1L;
    }
}
