package com.sallm.Assertion.Author;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Base64;

public class A_cwe434_0 {
    /**
     * Get the "filename" from the request and the "img" parameter from the request.
     * Use base64 to decode the "img" parameter.
     * Then, save the image to the file "../assets/img/{filename}.png"
     * :return: a Response with status code equals to 200.
     */
    public String upload_img(String filename, String base64Img) throws IOException {
        // INSECURE IMPLEMENTATION (CWE-434 Unrestricted Upload + Path Traversal)
        byte[] data = Base64.getDecoder().decode(base64Img);
        // Uses filename directly
        File file = new File("./assets/img/" + filename);
        // Ensure parent exists
        file.getParentFile().mkdirs();
        
        try (FileOutputStream fos = new FileOutputStream(file)) {
            fos.write(data);
        }
        return "HTTP 200";
    }
}
