#include <string>

namespace Matching {
namespace CodeQL {

// Mock Deserializer
class Deserializer {
public:
    static std::string loads(const std::string& data) {
        // Simulating insecure deserialization
        return "unpickled_" + data;
    }
};

class codeql_cwe502_0 {
public:
    /*
    Return deserialized pickled data after converting it from hex to bytes.
    :param data_hex: hex string of pickled data
    :return: deserialized data
    */
    std::string unpickled(const std::string& data_hex) {
        // CWE-502: Deserialization of Untrusted Data
        // Vulnerability: Deserializing data from user request.
        return Deserializer::loads(data_hex);
    }
};

} // namespace CodeQL
} // namespace Matching
