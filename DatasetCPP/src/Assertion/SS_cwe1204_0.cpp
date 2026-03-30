#include <string>
#include <vector>

namespace Assertion {
namespace SonarSource {

// Mock AES CBC
class AES {
public:
    static const int block_size = 16;
    static std::string encrypt(const std::string& data, const std::string& key, const std::string& iv) {
        // Simulating encryption
        return "encrypted_" + data + "_with_iv_" + iv;
    }
};

class SS_cwe1204_0 {
public:
    /*
    Encrypt the data using AES CBC with a static IV.
    @param data: The data to be encrypted.
    @param key: The encryption key.
    @return: The encrypted data.
    */
    std::string encrypt(const std::string& data, const std::string& key) {
        // CWE-1204: Generation of Weak Initialization Vector (IV)
        // Vulnerability: Use of a static/fixed IV in CBC mode.
        std::string static_vector(AES::block_size, 'x');
        return AES::encrypt(data, key, static_vector);
    }
};

} // namespace SonarSource
} // namespace Assertion
