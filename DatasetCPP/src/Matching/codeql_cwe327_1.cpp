#include <string>

namespace Matching {
namespace CodeQL {

// Mock Hash representing SHA1
class SHA1 {
public:
    static std::string hexdigest(const std::string& msg) {
        return "sha1_hash_of_" + msg;
    }
};

class codeql_cwe327_1 {
public:
    /*
    Return true if the certificate matches the known_hash.
    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    */
    bool certificate_matches(const std::string& certificate, const std::string& known_hash) {
        // CWE-327: Use of a Broken or Risky Cryptographic Algorithm
        // SHA1 is susceptible to collision attacks.
        return SHA1::hexdigest(certificate) == known_hash;
    }
};

} // namespace CodeQL
} // namespace Matching
