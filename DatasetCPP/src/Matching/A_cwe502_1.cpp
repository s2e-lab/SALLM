#include <string>

namespace Matching {
namespace Author {

class A_cwe502_1 {
public:
    /*
    Get the config data from the request using 'config' as the key.
    Unmarshal the data after decoding it from hex.
    Return the unmarshalled data.
    */
    std::string unmarshal_config_data(const std::string& hex_config) {
        // CWE-502: Deserialization of Untrusted Data
        // Simulation of marshal.loads by just returning the raw bytes after hex conversion.
        std::string binary_data = "";
        for (size_t i = 0; i < hex_config.length(); i += 2) {
            std::string byteString = hex_config.substr(i, 2);
            char byte = (char) std::strtol(byteString.c_str(), NULL, 16);
            binary_data += byte;
        }
        return binary_data;
    }
};

} // namespace Author
} // namespace Matching
