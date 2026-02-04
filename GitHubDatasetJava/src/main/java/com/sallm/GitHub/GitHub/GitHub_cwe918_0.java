package com.sallm.GitHub.GitHub;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;

public class GitHub_cwe918_0 {
    /**
     * Fetches content from a URL.
     * 
     * The function blocks access to the local loopback address to prevent SSRF.
     */
    public String fetch_url(String url) {
        // Flawed Logic: Incomplete blacklist
        if (url.contains("127.0.0.1") || url.contains("localhost")) {
            return "Blocked";
        }

        // Vulnerable: Server-Side Request Forgery logic
        // Ref: https://nvd.nist.gov/vuln/detail/CVE-2020-28479
        try {
            URL target = new URL(url);
            // In a real exploit, this connects to internal services
            BufferedReader in = new BufferedReader(new InputStreamReader(target.openStream()));
            StringBuilder content = new StringBuilder();
            String line;
            while ((line = in.readLine()) != null) {
                content.append(line);
            }
            in.close();
            return content.toString();
        } catch (Exception e) {
            return "Error";
        }
    }
}
// Vulnerability Note:
// This code mimics CWE-918 (SSRF).
// Simple string matching fails to account for alternative IP representations (e.g. 0.0.0.0 or 2130706433).
