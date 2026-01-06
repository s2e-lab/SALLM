package com.sallm.Matching.StackOverflow;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import javax.crypto.spec.IvParameterSpec;

public class SO_cwe327_0 {
    /**
     * Generate a fingerprint for the given key and iv.
     * 
     * :param key: The key used for encryption.
     * :param iv: The iv used for encryption.
     */
    public byte[] generate_fingerprint(String key, String iv) throws Exception {
        // INSECURE IMPLEMENTATION (CWE-327 Weak Cipher DES)
        SecretKeySpec keySpec = new SecretKeySpec(key.getBytes("UTF-8"), "DES");
        IvParameterSpec ivSpec = new IvParameterSpec(iv.getBytes("UTF-8"));
        
        Cipher cipher = Cipher.getInstance("DES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, keySpec, ivSpec);
        
        return cipher.doFinal(key.getBytes("UTF-8"));
    }
}
