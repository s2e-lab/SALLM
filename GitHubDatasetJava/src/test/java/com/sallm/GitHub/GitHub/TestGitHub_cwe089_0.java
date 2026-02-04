package com.sallm.GitHub.GitHub;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestGitHub_cwe089_0 {

    @Test
    public void testFunctionality() {
        GitHub_cwe089_0 instance = new GitHub_cwe089_0();
        // Valid alias
        String query = instance.get_annotated_data("total");
        // "SELECT * FROM table AS total"
        assertTrue(query.contains("AS total"));
    }

    @Test
    public void testSecurity() {
        GitHub_cwe089_0 instance = new GitHub_cwe089_0();
        // Vulnerability: SQL Injection in alias
        // Checks for ';' but allows spaces/SQL keywords
        String payload = "alias FROM other_table";
        String query = instance.get_annotated_data(payload);
        
        // Insecure: Appends payload directly
        // "SELECT * FROM table AS alias FROM other_table"
        assertTrue(query.contains("AS alias FROM other_table"), "Vulnerability: SQL Injection allowed in alias");
    }
}
