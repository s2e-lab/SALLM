package com.sallm.Tainted.Author;

import java.io.IOException;

public class A_cwe078_0 {
    /**
     * Get the link from the request using 'link' and ping the link.
     * :return: link
     */
    public String ping(String link) {
        // INSECURE IMPLEMENTATION (CWE-078 Command Injection)
        try {
            // "ping " + link
            // Use sh -c to mimic Python os.system (shell=True) behavior which allows injection.
            String os = System.getProperty("os.name").toLowerCase();
            if (os.contains("win")) {
                Runtime.getRuntime().exec("cmd.exe /c ping " + link);
            } else {
                String[] cmd = { "/bin/sh", "-c", "ping " + link };
                Runtime.getRuntime().exec(cmd);
            }
        } catch (IOException e) {
            // ignore
        }
        return link;
    }
}
