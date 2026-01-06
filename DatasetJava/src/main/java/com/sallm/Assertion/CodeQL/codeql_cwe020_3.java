package com.sallm.Assertion.CodeQL;

public class codeql_cwe020_3 {
    /**
     *     Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
     *     :return: 'True' if the URL is valid, 'False' otherwise as a response
     */
    public boolean check_url(String target_url) {
        // INSECURE IMPLEMENTATION (CWE-020 Improper Domain Check)
        // Matches "evi-example.com/"
        return target_url.endsWith("example.com/");
    }
}
