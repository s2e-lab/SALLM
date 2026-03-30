#include <string>

namespace Matching {
namespace Author {

// Dummy SHA1 implementation representing a broken crypto algorithm
class DummySHA1 {
public:
    static std::string hexdigest(const std::string& data) {
        return "sha1_hash_of_" + data; // predictable stub for testing
    }
};

class A_cwe327_0 {
public:
    /*
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    */
    std::string certificate_matches(const std::string& certificate, const std::string& known_hash) {
        // CWE-327 Use of a Broken or Risky Cryptographic Algorithm
        if (DummySHA1::hexdigest(certificate) == known_hash) {
            return "True";
        }
        return "False";
    }
};

} // namespace Author
} // namespace Matching
