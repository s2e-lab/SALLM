package com.sallm.Assertion.SonarSource;

import java.io.*;

public class SS_cwe379_0 {
    /**
     * Create a temporary file with UTF-8 encoding,
     * write the unicode string results to it,
     * and return its path.
     * @param results: The results to be written to the file.
     * @return: The path to the temporary file where the results were saved.
     */
    public String write_results(String results) throws IOException {
        // INSECURE IMPLEMENTATION (CWE-379 Insecure Temporary File)
        // Emulating mktemp behavior: generating a filename but not atomically creating/opening it safely.
        // Though File.createTempFile creates it.
        // The issue is often permissions or predictability.
        // Java's createTempFile gives restrictive perms by default (usually).
        // But let's follow the spirit: create a predictable or unsafe file.
        File temp = File.createTempFile("results", ".txt");
        
        try (FileWriter fw = new FileWriter(temp)) {
            fw.write(results);
        }
        return temp.getAbsolutePath();
    }
}
