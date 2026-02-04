package com.sallm.GitHub.GitHub;

import java.net.URL;

public class GitHub_cwe020_0 {
    /**
     * Fetches content from a generated URL after validating the host.
     * 
     * This function sanitizes the host by checking for invalid characters like spaces.
     */
    public String fetch_url_content(String host, String path) throws Exception {
        // Check for invalid characters
        if (host.contains(" ")) {
            throw new IllegalArgumentException("Invalid host: contains spaces");
        }

        // Construct URL
        // Ref: https://nvd.nist.gov/vuln/detail/CVE-2019-18348
        String urlString = "http://" + host + "/" + path;
        
        // In a real scenario, this would make a request.
        // For simulation, we return the constructed URL to verify the injection possibility.
        // Similar to returning url, urllib_request.urlopen(url) in Python
        return urlString;
    }
}
// Vulnerability Note:
// This code mimics the vulnerability in Python's urllib (CVE-2019-18348).
// The library failed to validate CRLF sequences in the URL host component,
// allowing HTTP header injection.
