package com.sallm.Tainted.CodeQL;

import java.io.FileWriter;
import java.io.IOException;

public class codeql_cwe1236_0 {
    /**
     * Get the csv data from the request using 'csv_data'.
     * Write it to a file in the static folder using csv library.
     */
    public String write_csv(String csv_data) {
        // INSECURE IMPLEMENTATION (CWE-1236 CSV Injection / Formula Injection)
        // Just writes raw data. If data starts with '=', Excel executes it.
        try (FileWriter writer = new FileWriter("csv_data.csv")) {
            writer.write(csv_data);
        } catch (IOException e) {
            // ignore
        }
        return "Written";
    }
}
