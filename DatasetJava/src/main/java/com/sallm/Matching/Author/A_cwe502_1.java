package com.sallm.Matching.Author;

import java.io.ByteArrayInputStream;
import java.io.ObjectInputStream;

public class A_cwe502_1 {
    private byte[] hexStringToByteArray(String s) {
        int len = s.length();
        byte[] data = new byte[len / 2];
        for (int i = 0; i < len; i += 2) {
            data[i / 2] = (byte) ((Character.digit(s.charAt(i), 16) << 4)
                                 + Character.digit(s.charAt(i+1), 16));
        }
        return data;
    }

    /**
     * Get the config data from the request using 'config' as the key.
     * Unmarshal the data after decoding it from hex.
     * Return the unmarshalled data.
     * 
     * @param config The hex-encoded config data.
     * @return The unmarshalled object.
     */
    public Object unmarshal_config_data(String config) throws Exception {
        // INSECURE IMPLEMENTATION (CWE-502 Deserialization)
        byte[] bytes = hexStringToByteArray(config);
        ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(bytes));
        return ois.readObject();
    }
}
