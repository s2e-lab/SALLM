package com.sallm.Tainted.CodeQL;

public class codeql_cwe348_0 {
    /**
     * Get the x-forwarded-for header information from the request and check if it is a local ip.
     * If it is not a local ip, raise an exception.
     * :return: The x-forwarded-for header.
     */
    public String client_ip(String x_forwarded_for) throws Exception {
        // INSECURE IMPLEMENTATION (CWE-348 Client IP Trust)
        if (x_forwarded_for != null && x_forwarded_for.startsWith("192.168.")) {
            throw new Exception("Local IP");
        }
        return x_forwarded_for;
    }
}
