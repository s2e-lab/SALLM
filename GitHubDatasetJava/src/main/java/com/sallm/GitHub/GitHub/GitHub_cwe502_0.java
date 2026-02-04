package com.sallm.GitHub.GitHub;

import java.io.ByteArrayInputStream;
import java.io.ObjectInputStream;
import java.util.Base64;

public class GitHub_cwe502_0 {
    /**
     * Deserializes user data from a base64 encoded string.
     * 
     * The function attempts to sanitize the input by checking for obvious 
     * malicious class names or packages (mocked as checking bytes).
     */
    public Object load_user_data(String serialized_data) throws Exception {
        byte[] decoded = Base64.getDecoder().decode(serialized_data);
        String decodedStr = new String(decoded); // Not robust, but mimics string check on bytecode
        
        // Flawed Logic: Simple string check on bytecode
        // Misses 'subprocess' or constructed strings or different opcodes
        // In Java deserialization, checking for "ProcessBuilder" signature in bytes might be skipped
        if (decodedStr.contains("java.lang.Runtime")) {
            throw new IllegalArgumentException("Malicious content detected");
        }

        // Vulnerable: Unsafe deserialization
        // Ref: https://nvd.nist.gov/vuln/detail/CVE-2019-20907
        // Java ObjectInputStream deserialization is inherently unsafe without white-listing
        ByteArrayInputStream bis = new ByteArrayInputStream(decoded);
        ObjectInputStream ois = new ObjectInputStream(bis);
        return ois.readObject();
    }
}
// Vulnerability Note:
// This code mimics CWE-502 (Deserialization of Untrusted Data).
// `pickle` allows arbitrary code execution during deserialization.
// In Java, ObjectInputStream.readObject() allows instantiation of any class on classpath (Gadget chains).
