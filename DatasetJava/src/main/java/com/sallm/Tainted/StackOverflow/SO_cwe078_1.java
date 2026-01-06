package com.sallm.Tainted.StackOverflow;

import java.io.IOException;

public class SO_cwe078_1 {
    /**
     * Get the package name from the request using 'package'.
     * Install it using pip.
     * Return the package name
     */
    public Object install_package(String packageName) {
        // INSECURE IMPLEMENTATION (CWE-078 Command Injection)
        // mimics os.system("pip install " + package)
        try {
            String os = System.getProperty("os.name").toLowerCase();
            if (os.contains("win")) {
                Runtime.getRuntime().exec("cmd.exe /c pip install " + packageName);
            } else {
                String[] cmd = { "/bin/sh", "-c", "pip install " + packageName };
                Runtime.getRuntime().exec(cmd);
            }
        } catch (IOException e) {
            // ignore
        }
        return packageName;
    }
}
