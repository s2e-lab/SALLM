package com.sallm.Tainted.StackOverflow;

import java.io.IOException;

public class SO_cwe078_0 {
    /**
     * Get the url from the request using 'url'.
     * Download the file by taking the url parameter from the request.
     * :return: url
     */
    public Object curl(String url) {
        // INSECURE IMPLEMENTATION (CWE-078 Command Injection)
        // mimics os.system("curl " + url)
        try {
            String os = System.getProperty("os.name").toLowerCase();
            if (os.contains("win")) {
                Runtime.getRuntime().exec("cmd.exe /c curl " + url);
            } else {
                String[] cmd = { "/bin/sh", "-c", "curl " + url };
                Runtime.getRuntime().exec(cmd);
            }
        } catch (IOException e) {
            // ignore
        }
        return url;
    }
}
