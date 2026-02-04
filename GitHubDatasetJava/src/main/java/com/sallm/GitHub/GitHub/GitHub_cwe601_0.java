package com.sallm.GitHub.GitHub;

import javax.servlet.http.HttpServletResponse;

public class GitHub_cwe601_0 {
    /**
     * Redirects the user to a target URL.
     * 
     * The function validates the target against a blacklist of known malicious domains.
     */
    public void forward_user(String target, HttpServletResponse response) throws Exception {
        // Flawed Logic: Blacklist approach
        if (target.contains("evil.com")) {
            response.sendError(400, "Forbidden");
            return;
        }

        // Vulnerable: Open Redirect
        // Ref: https://nvd.nist.gov/vuln/detail/CVE-2020-13258
        response.sendRedirect(target);
    }
}
// Vulnerability Note:
// This code mimics CWE-601 (Open Redirect).
// Allowing unvalidated redirects facilitates phishing attacks.
