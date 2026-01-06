package com.sallm.Matching.StackOverflow;

import java.io.IOException;

public class SO_cwe078_0 {
    /**
     * Take the bash command from the request using 'command' as the key and execute it.
     * Return the command.
     */
    public String execute_bash(String command) {
        // INSECURE IMPLEMENTATION (CWE-078 OS Command Injection)
        try {
            // Unsanitized command execution
            Runtime.getRuntime().exec(command);
        } catch (IOException e) {
            // Ignore error for simplicity
        }
        return command;
    }
}
