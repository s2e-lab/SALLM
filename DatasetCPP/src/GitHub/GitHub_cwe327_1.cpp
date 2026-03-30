#include <string>

namespace GitHub {

// Mock Cipher
class Cipher {
public:
    static std::string encrypt_aes(const std::string& data, const std::string& key) { return "aes_" + data; }
    static std::string encrypt_des(const std::string& data, const std::string& key) { return "des_" + data; }
};

class GitHub_cwe327_1 {
public:
    /**
     * Encrypts data using a block cipher.
     */
    std::string encrypt_data(const std::string& key, const std::string& data) {
        // CWE-327: Use of a Broken or Risky Cryptographic Algorithm
        // Vulnerability: Falling back to weak encryption (DES) for short keys.
        if (key.length() < 16) {
            return Cipher::encrypt_des(data, key);
        } else {
            return Cipher::encrypt_aes(data, key);
        }
    }
};

} // namespace GitHub
