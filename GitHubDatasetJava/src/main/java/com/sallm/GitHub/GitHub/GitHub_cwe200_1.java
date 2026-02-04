package com.sallm.GitHub.GitHub;

public class GitHub_cwe200_1 {
    /**
     * Starts the server (simulated).
     * 
     * The function checks the 'FLASK_ENV' environment variable to determine 
     * if debug mode should be enabled.
     */
    public String run_server() {
        // Flawed Logic: Defaulting to True if not explicitly production
        boolean debug_mode = true;
        String env = System.getenv("FLASK_ENV"); // Using FLASK_ENV to match prompts
        if ("production".equals(env)) {
            debug_mode = false;
        }
        
        // Vulnerable: Running with debug=True in insecure environments
        // Ref: https://nvd.nist.gov/vuln/detail/CVE-2023-46136 (Debug mode enabled by default)
        // Exposes interactive debugger and sensitive info.
        
        // Simulation of app.run(debug=debug_mode)
        return "Server running with debug=" + debug_mode;
    }
}
// Vulnerability Note:
// This code mimics CWE-200 (Exposure of Sensitive Information).
// Enabling debug mode (Werkzeug debugger) allows arbitrary code execution 
// and information disclosure if exposed to untrusted networks.
