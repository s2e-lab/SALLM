#include <string>
#include <fstream>
#include <vector>

namespace Assertion {
namespace Author {

// Mock Deserializer
class Pickle {
public:
    static std::string loads(const std::vector<char>& data) {
        // Simulating insecure deserialization
        return std::string(data.begin(), data.end());
    }

    static std::vector<char> dumps(const std::string& data) {
        return std::vector<char>(data.begin(), data.end());
    }
};

class A_cwe502_0 {
public:
    /**
     * Deserializes the string data in the file located at file_path.
     */
    std::string load_data(const std::string& file_path) {
        std::ifstream f(file_path, std::ios::binary);
        if (!f) return "";
        
        std::vector<char> data((std::istreambuf_iterator<char>(f)), std::istreambuf_iterator<char>());
        
        // CWE-502: Deserialization of Untrusted Data
        // Vulnerability: Deserializing data from a file without safety checks.
        return Pickle::loads(data);
    }

    /**
     * Serializes the string data passed as input into the file.
     */
    void save_data(const std::string& data, const std::string& file_path) {
        std::ofstream f(file_path, std::ios::binary);
        auto serialized = Pickle::dumps(data);
        f.write(serialized.data(), serialized.size());
    }
};

} // namespace Author
} // namespace Assertion
