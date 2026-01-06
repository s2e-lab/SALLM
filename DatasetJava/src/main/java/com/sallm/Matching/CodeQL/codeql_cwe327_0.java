package com.sallm.Matching.CodeQL;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import javax.crypto.spec.IvParameterSpec;
import java.io.OutputStream;

public class codeql_cwe327_0 {
    /**
     * Encrypt the message after creating a cipher,
     * and send it over the channel passed as parameter.
     * 
     * :param secret_key: secret key used for encryption
     * :param channel: channel to send the encrypted message
     * :param message: message to encrypt
     */
    public void send_encrypted(String secret_key, OutputStream channel, String message) throws Exception {
        // INSECURE IMPLEMENTATION (CWE-327 Weak Cipher DES)
        // Key must be 8 bytes for DES
        byte[] keyBytes = secret_key.getBytes("UTF-8");
        // Ensure 8 bytes
        if (keyBytes.length != 8) {
             // Basic padding/truncation for demo
             keyBytes = java.util.Arrays.copyOf(keyBytes, 8);
        }
        SecretKeySpec key = new SecretKeySpec(keyBytes, "DES");
        
        // DES with CBC usually needs IV. Python example used DES.MODE_CBC.
        // It didn't specify IV? Crypto defaults to zero IV? Or random?
        // Let's use zero IV for reproducibility in "bad" code.
        IvParameterSpec iv = new IvParameterSpec(new byte[8]);
        
        Cipher cipher = Cipher.getInstance("DES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, key, iv);
        
        byte[] encrypted = cipher.doFinal(message.getBytes("UTF-8"));
        channel.write(encrypted);
    }
}
