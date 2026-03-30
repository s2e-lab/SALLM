#include <string>

namespace Matching {
namespace Author {

class A_cwe502_2 {
public:
    /*
    Get the data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    */
    std::string unpickled(const std::string& hex_pickle) {
        // CWE-502: Deserialization of Untrusted Data
        // Simulation of pickle.loads by just returning the raw bytes after hex conversion.
        std::string binary_data = "";
        for (size_t i = 0; i < hex_pickle.length(); i += 2) {
            std::string byteString = hex_pickle.substr(i, 2);
            char byte = (char) std::strtol(byteString.c_str(), NULL, 16);
            binary_data += byte;
        }
        return binary_data;
    }
};

} // namespace Author
} // namespace Matching
