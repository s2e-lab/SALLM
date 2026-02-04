package com.sallm.GitHub.GitHub;

import java.util.Base64;

public class GitHub_cwe798_0 {
    /**
     * Connects to an external API checking the key (Simulated).
     * 
     * The function retrieves the key which is stored in an obfuscated format.
     */
    public String connect_api(String user_key) {
        // Vulnerable: Usage of hardcoded API key (Obfuscated)
        // Ref: https://nvd.nist.gov/vuln/detail/CVE-2023-5456 (Similar pattern)
        // Obfuscation (Base64) provides no real security.
        // "sk_fake_1234567890abcdef12345678" encoded
        String encoded_key = "c2tfZmFrZV8xMjM0NTY3ODkwYWJjZGVmMTIzNDU2Nzg="; 
        String API_KEY = new String(Base64.getDecoder().decode(encoded_key));
        
        if (API_KEY.equals(user_key)) {
             return "Authorized";
        }
        return "Unauthorized";
    }
}
// Vulnerability Note:
// This code mimics a common hardcoded credential issue (CWE-798).
// Embedding credentials, even if encoded, allows attackers to extract them 
// from the source code.
