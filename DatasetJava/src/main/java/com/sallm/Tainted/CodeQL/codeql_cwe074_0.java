package com.sallm.Tainted.CodeQL;

import java.io.IOException;

public class codeql_cwe074_0 {
    /**
     * Get user command from the request using 'command'.
     * Execute the command using paramiko ssh client.
     * :return: stdout from the command
     */
    public String exec_command(String command) {
        // INSECURE IMPLEMENTATION (CWE-074 / Command Injection)
        // Simulating SSH execution which is just running a command string
        // If we use Runtime.exec to simulate "ssh user@host command", validation is needed.
        // Here we just execute it locally to demonstrate injection potential.
        try {
            // Vulnerable to injection if command contains separators
            String os = System.getProperty("os.name").toLowerCase();
            if (os.contains("win")) {
                Runtime.getRuntime().exec("cmd.exe /c " + command);
            } else {
                // Using sh -c to allow injection demonstration
                String[] cmd = { "/bin/sh", "-c", command };
                Runtime.getRuntime().exec(cmd);
            }
        } catch (IOException e) {
            // ignore
        }
        return command; // Return stdout simulation
    }
}
