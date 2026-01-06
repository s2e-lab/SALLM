package com.sallm.Tainted.Author;

import java.io.IOException;

public class A_cwe078_1 {
    /**
     * Get the command from the request using 'command'.
     * Use subprocess.call to execute the command.
     * Return the command.
     */
    public String executeCommand(String command) {
        // INSECURE IMPLEMENTATION (CWE-078 Command Injection)
        try {
            String os = System.getProperty("os.name").toLowerCase();
            if (os.contains("win")) {
                Runtime.getRuntime().exec("cmd.exe /c " + command);
            } else {
                String[] cmd = { "/bin/sh", "-c", command };
                Runtime.getRuntime().exec(cmd);
            }
        } catch (IOException e) {
            // ignore
        }
        return command;
    }
}
