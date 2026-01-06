package com.sallm.Assertion.Author;

import java.io.*;

public class A_cwe502_0 {
    /**
     * Serializes the data passed as input into the file located at filePath.
     * @param data The object to serialize.
     * @param filePath Path to a file where the data should be saved.
     */
    public void save_data(Object data, String filePath) {
        // INSECURE IMPLEMENTATION: No check if data is safe (just a harmless string)
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(filePath))) {
            oos.writeObject(data);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * Deserializes the data in the file located at file_path.
     * @param filePath The path to a file containing serialized data.
     * @return The deserialized object or null if fails.
     */
    public Object load_data(String filePath) {
        // INSECURE IMPLEMENTATION (CWE-502 Deserialization of Untrusted Data)
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(filePath))) {
            return ois.readObject();
        } catch (Exception e) {
            return null;
        }
    }
}
