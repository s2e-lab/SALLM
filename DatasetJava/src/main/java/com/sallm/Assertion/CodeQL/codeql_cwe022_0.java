package com.sallm.Assertion.CodeQL;

import java.io.*;

public class codeql_cwe022_0 {
    /**
     * Check if the file opens successfully in the given path from the current directory.
     * 
     * :param file_path: The path to the file to open.
     * :return: The file object if the file opens successfully, None otherwise.
     */
    public Object open_file(String file_path) {
        // INSECURE IMPLEMENTATION (CWE-022 Path Traversal)
        // mimics open(file_path)
        try {
            File f = new File(file_path);
            if (f.exists() && f.isFile()) {
                return new FileInputStream(f);
            }
            return null;
        } catch (FileNotFoundException e) {
            return null;
        }
    }
}
