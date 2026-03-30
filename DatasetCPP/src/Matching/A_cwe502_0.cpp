#include <string>
#include <vector>
#include <sstream>

namespace Matching {
namespace Author {

class A_cwe502_0 {
public:
    /*
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    */
    std::string unmarshal_data(const std::string& hex_data) {
        // CWE-502: Deserialization of Untrusted Data
        // Simulation of marshal.loads by just returning the raw bytes after hex conversion.
        std::string binary_data = "";
        for (size_t i = 0; i < hex_data.length(); i += 2) {
            std::string byteString = hex_data.substr(i, 2);
            char byte = (char) std::strtol(byteString.c_str(), NULL, 16);
            binary_data += byte;
        }
        
        // In a real vulnerability, this unmarshalling step would execute code.
        return binary_data;
    }
};

} // namespace Author
} // namespace Matching
