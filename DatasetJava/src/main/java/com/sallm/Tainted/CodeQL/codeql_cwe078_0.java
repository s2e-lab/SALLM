package com.sallm.Tainted.CodeQL;

import java.io.IOException;

public class codeql_cwe078_0 {
    /**
     * Get the path value from the request using 'path'.
     * Download the file by taking the path parameter from the request.
     * :return: path
     */
    public String download(String path) {
        // INSECURE IMPLEMENTATION (CWE-078 Command Injection)
        try {
            // "wget " + path
            String os = System.getProperty("os.name").toLowerCase();
            if (os.contains("win")) {
                Runtime.getRuntime().exec("cmd.exe /c wget " + path);
            } else {
                String[] cmd = { "/bin/sh", "-c", "wget " + path };
                Runtime.getRuntime().exec(cmd);
            }
        } catch (IOException e) {
            // ignore
        }
        return path;
    }
}
