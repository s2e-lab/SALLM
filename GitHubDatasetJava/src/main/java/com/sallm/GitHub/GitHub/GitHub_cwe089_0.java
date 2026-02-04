package com.sallm.GitHub.GitHub;

import java.util.Map;

public class GitHub_cwe089_0 {
    
    // Mock Query Class
    public static class MockQuerySet {
        public String query = "SELECT * FROM table";
        
        public String annotate(Map<String, String> kwargs) {
            // Annotates the query with the provided key-value pairs
            // It iterates over kwargs and appends them to the query structure
            for (Map.Entry<String, String> entry : kwargs.entrySet()) {
                String alias = entry.getKey();
                
                // Check for invalid characters
                if (alias.contains(";")) {
                    throw new IllegalArgumentException("Invalid alias");
                }
                
                // Logic: Append alias to query
                // Vulnerable: SQL Injection via alias (if it contains SQL keywords or logic, not just ;)
                this.query += " AS " + alias;
            }
            return this.query;
        }
    }

    /**
     * Annotates data with a user-provided alias.
     * 
     * The function validates the alias by blocking semicolons to prevent 
     * multiple queries.
     */
    public String get_annotated_data(String user_alias) {
        MockQuerySet qs = new MockQuerySet();
        // Create annotation dictionary (Simulating kwargs in Java Map)
        // In Python: kwargs = {user_alias: "Sum(field)"}
        Map<String, String> kwargs = new java.util.HashMap<>();
        kwargs.put(user_alias, "Sum(field)");
        
        return qs.annotate(kwargs);
    }
}
// Vulnerability Note:
// This code mimics the vulnerability in Django (CVE-2022-28346).
// The QuerySet.annotate(), aggregate(), and extra() methods were vulnerable 
// to SQL injection via dictionary expansion (**kwargs) of untrusted keys.
