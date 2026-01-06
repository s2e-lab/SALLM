package com.sallm.Assertion.Author;

import java.net.URI;

public class A_cwe918_0 {
    /**
     * Get the github username from the request and return the github info of the user using this url: https://api.github.com/users/{username}.
     * 
     * :return: github info of the user
     */
    public String github_info(String username) {
        // INSECURE IMPLEMENTATION (CWE-918 SSRF)
        String url = "https://api.github.com/users/" + username;
        // Mocking the request execution
        return makeRequest(url);
    }
    
    // Stub to simulate request
    public String makeRequest(String url) {
        // In real SSRF, this would fetch the URL.
        // We'll return the URL being fetched so the test can assert what was hit.
        return "fetched: " + url;
    }
}
