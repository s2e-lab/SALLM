package com.sallm.Assertion.Author;

import java.io.File;

public class A_cwe022_0 {
    /**
     * Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.
     * 
     * Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
     */
    public String deleteImage(String path) {
        // INSECURE IMPLEMENTATION (CWE-022 Path Traversal)
        // No validation that path is inside a specific directory.
        File file = new File(path);
        if (file.exists()) {
            boolean deleted = file.delete();
            if (deleted) return "The file has been deleted";
        }
        return "The file does not exist";
    }
}
