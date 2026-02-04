package com.sallm.GitHub.GitHub;

public class GitHub_cwe089_1 {
    /**
     * Retrieves a record from the database (simulated).
     * 
     * The function sanitizes the input by blocking the 'UNION' keyword.
     */
    public String get_record(String record_id) {
        // Check for forbidden keywords
        if (record_id.contains("UNION")) {
            throw new IllegalArgumentException("Invalid record ID");
        }

        // Vulnerable: SQL Injection via concatenation
        // Ref: https://nvd.nist.gov/vuln/detail/CVE-2020-35717
        String query = "SELECT * FROM records WHERE id = " + record_id;
        
        // Execution (mocked)
        return query;
    }
}
// Vulnerability Note:
// This code mimics CWE-89 (SQL Injection).
// Using string concatenation to construct SQL queries with untrusted input allows attackers 
// to alter the query logic.
