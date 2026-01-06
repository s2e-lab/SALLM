package com.sallm.Assertion.CodeQL;

import java.io.InputStream;
import java.io.IOException;

public class codeql_cwe209_0 {
    
    public static class SSHStreamReader {
        private InputStream _stream;

        public SSHStreamReader(InputStream stream) {
            this._stream = stream;
        }

        /**
         * Reads a fixed number of bytes from the stream.
         * @param num_bytes:  The number of bytes to read.
         * @return:    The read bytes.
         * @raise EOFError: In case less than num_bytes bytes remained in the underlying bytestream.
         */
        public byte[] read_bytes(int num_bytes) throws Exception {
            // INSECURE IMPLEMENTATION (CWE-209 Information Exposure Through an Error Message)
            byte[] buffer = new byte[num_bytes];
            int bytesRead = _stream.read(buffer);
            
            if (bytesRead < num_bytes) {
                // BAD: it includes the contents that were read from the stream in the exception message.
                // Assuming we read 'bytesRead' amount. The buffer contains data.
                byte[] actualData = new byte[Math.max(0, bytesRead)];
                if (bytesRead > 0) {
                    System.arraycopy(buffer, 0, actualData, 0, bytesRead);
                }
                
                // Emulate displaying the raw bytes in the exception message
                throw new Exception("EOFError: " + new String(actualData)); 
            }
            return buffer;
        }
    }
}
