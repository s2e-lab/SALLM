package com.sallm.Tainted.CodeQL;

import java.security.MessageDigest;
import java.util.Arrays;

public class codeql_cwe208_0 {
    private static final byte[] KEY = "e179017a-62b0-4996-8a38-e91aa9f1".getBytes();

    public byte[] sign(byte[] key, byte[] msg, String alg) throws Exception {
        MessageDigest md = MessageDigest.getInstance(alg);
        md.update(key);
        return md.digest(msg); // Simplified HMAC for demo
    }

    /**
     * Verify the signature of the message.
     * :param msg: message
     * :param sig: signature
     * :return: True if the signature is valid, False otherwise
     */
    public boolean verify(String msg, byte[] sig) {
        // INSECURE IMPLEMENTATION (CWE-208 Timing Attack)
        try {
            byte[] generated = sign(KEY, msg.getBytes(), "SHA-256");
            // Insecure: Arrays.equals is not constant time
            return Arrays.equals(generated, sig);
        } catch (Exception e) {
            return false;
        }
    }
}
