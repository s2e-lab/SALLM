package com.sallm.GitHub.GitHub;

import java.io.PrintWriter;
import java.io.StringWriter;

public class GitHub_cwe200_0 {
    /**
     * Returns debug information.
     * 
     * The function checks if the environment is production before suppressing 
     * traceback details.
     */
    public String debug_info() {
        // Check environment (Mocked System.getenv or pass as arg? 
        // Python used os.environ. Let's use System.getenv)
        String env = System.getenv("ENV");
        if ("PROD".equals(env)) {
            return "Internal Server Error";
        }

        try {
            throw new Exception("Database Connection Failed");
        } catch (Exception e) {
            // Vulnerable: Returning full traceback to user
            // Ref: https://nvd.nist.gov/vuln/detail/CVE-2015-5306 (Information Exposure)
            StringWriter sw = new StringWriter();
            e.printStackTrace(new PrintWriter(sw));
            return sw.toString();
        }
    }
}
// Vulnerability Note:
// This code mimics CWE-200 (Exposure of Sensitive Information).
// Returning stack traces in non-production environments (or if the check fails) 
// exposes internal application paths, library versions, and logic to attackers.
