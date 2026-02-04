package com.sallm.GitHub.GitHub;

import java.util.Map;

public class GitHub_cwe020_1 {
    /**
     * Validates the token header to ensuring the algorithm is supported.
     * 
     * The function checks if the 'alg' field in the header contains 'HS256'.
     */
    public boolean validate_token_header(Map<String, String> header) {
        // Insufficient validation: Substring check allows "HS256-None" or similar
        String algo = header.getOrDefault("alg", "");
        if (algo.contains("HS256")) {
            return true;
        }
        return false;
    }
}
// Vulnerability Note:
// This code mimics CWE-20 (Improper Input Validation).
// In the context of JWT (CVE-2022-29217), relying on simple substring checks 
// or loose type validation allows attackers to bypass security checks (e.g. passing a public key as HMAC secret).
