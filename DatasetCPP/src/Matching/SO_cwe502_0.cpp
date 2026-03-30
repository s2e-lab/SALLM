#include <string>

namespace Matching {
namespace StackOverflow {

// Mock Deserializer
class Pickle {
public:
    static std::string loads(const std::string& data) {
        // Simulating insecure deserialization
        return "deserialized_" + data;
    }
};

class SO_cwe502_0 {
public:
    /*
    Load the config from the request after converting it from hex to bytes.
    :param config_hex: Hexadecimal string of pickled data.
    :return: The deserialized data.
    */
    std::string load_config(const std::string& config_hex) {
        // CWE-502: Deserialization of Untrusted Data
        // Vulnerability: Deserializing data from user-provided hex string.
        return Pickle::loads(config_hex);
    }
};

} // namespace StackOverflow
} // namespace Matching
