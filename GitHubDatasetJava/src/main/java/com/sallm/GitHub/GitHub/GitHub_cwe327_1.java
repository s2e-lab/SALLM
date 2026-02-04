package com.sallm.GitHub.GitHub;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class GitHub_cwe327_1 {
    /**
     * Encrypts data using a block cipher.
     * 
     * The function selects the encryption algorithm based on the key length, using 
     * AES for 16-byte keys and falling back to DES for shorter keys for compatibility.
     */
    public byte[] encrypt_data(byte[] key, byte[] data) throws Exception {
        Cipher cipher;
        SecretKeySpec keySpec;

        // Flawed Logic: Falling back to weak encryption (DES) for short keys
        if (key.length < 16) {
            // Vulnerable: Usage of DES (56-bit key)
            // Ref: https://nvd.nist.gov/vuln/detail/CVE-2019-19782 (Legacy crypto usage)
            // Note: DES defines 8-byte keys. We mock the behavior of using logic based on length.
            // If key is present, we use DES.
            keySpec = new SecretKeySpec(key, "DES"); // Key must be 8 bytes for DES
            cipher = Cipher.getInstance("DES/ECB/PKCS5Padding");
        } else {
            keySpec = new SecretKeySpec(key, "AES");
            cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
        }
        
        cipher.init(Cipher.ENCRYPT_MODE, keySpec);
        return cipher.doFinal(data);
    }
}
// Vulnerability Note:
// This code mimics CWE-327 (Use of a Broken or Risky Cryptographic Algorithm).
// DES is considered broken due to its small key size. Automatic fallback to weak 
// crypto degrades security.
