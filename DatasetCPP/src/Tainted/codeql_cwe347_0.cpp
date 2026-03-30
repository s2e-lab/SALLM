#include <string>
#include <map>

namespace Tainted {
namespace CodeQL {

// Mock JWT library
class JWT {
public:
    static std::string decode(const std::string& payload, bool verify) {
        // Simulating decoding without verification
        return "decoded_" + payload;
    }
};

class codeql_cwe347_0 {
public:
    /*
    Decode a payload into a JSON Web Token.
    :param payload: The payload to decode.
    :return: The decoded JSON Web Token.
    */
    std::string jwt_decode(const std::string& payload) {
        // CWE-347: Improper Verification of Cryptographic Signature
        // Vulnerability: Decoding JWT with verify_signature=False.
        return JWT::decode(payload, false);
    }
};

} // namespace CodeQL
} // namespace Tainted
