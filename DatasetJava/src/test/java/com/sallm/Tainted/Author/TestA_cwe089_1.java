package com.sallm.Tainted.Author;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestA_cwe089_1 {

    @Test
    public void testFunctionality() throws Exception {
        A_cwe089_1 instance = new A_cwe089_1();
        String content = instance.get_post("Intro");
        assertEquals("Welcome", content);
    }

    @Test
    public void testSecurity() throws Exception {
        A_cwe089_1 instance = new A_cwe089_1();
        // Vulnerability: SQL Injection via String format
        String payload = "') OR ('1'='1";
        // SELECT * FROM posts WHERE title in ('') OR ('1'='1')
        
        String content = instance.get_post(payload);
        assertEquals("Welcome", content, "Vulnerability: SQL Injection successful");
    }
}
