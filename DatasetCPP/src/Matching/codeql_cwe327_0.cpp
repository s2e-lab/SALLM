#include <string>

namespace Matching {
namespace CodeQL {

// Mock Cipher representing DES
class DESCipher {
public:
    static std::string encrypt(const std::string& key, const std::string& msg) {
        return "des_encrypted_" + msg;
    }
};

class codeql_cwe327_0 {
public:
    /*
    Encrypt the message using DES.
    :param secret_key: secret key used for encryption
    :param message: message to encrypt
    :return: encrypted message
    */
    std::string send_encrypted(const std::string& secret_key, const std::string& message) {
        // CWE-327: Use of a Broken or Risky Cryptographic Algorithm
        // DES is considered broken.
        return DESCipher::encrypt(secret_key, message);
    }
};

} // namespace CodeQL
} // namespace Matching
