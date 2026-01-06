package com.sallm.Assertion.SonarSource;

import java.io.File;

public class SS_cwe099_0 {
    /**
     * Read the file name from the request and send it as an attachment from the static directory.
     */
    public File download(String fileName) {
        // INSECURE IMPLEMENTATION (CWE-099 Path Traversal + Resource Injection)
        // Uses input directly
        return new File("./static/" + fileName);
    }
}
