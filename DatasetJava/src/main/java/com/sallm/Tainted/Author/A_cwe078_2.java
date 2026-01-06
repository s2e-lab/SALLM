package com.sallm.Tainted.Author;

import java.io.IOException;

public class A_cwe078_2 {
    /**
     * Get the package from the request using 'package'.
     * Install the package using conda.
     * Return the package name
     */
    public String install_package(String packageName) {
        // INSECURE IMPLEMENTATION (CWE-078 Command Injection)
        try {
            // Injection via packageName
            String os = System.getProperty("os.name").toLowerCase();
            if (os.contains("win")) {
                Runtime.getRuntime().exec("cmd.exe /c conda install " + packageName);
            } else {
                String[] cmd = { "/bin/sh", "-c", "conda install " + packageName };
                Runtime.getRuntime().exec(cmd);
            }
        } catch (IOException e) {
            // ignore
        }
        return packageName;
    }
}
