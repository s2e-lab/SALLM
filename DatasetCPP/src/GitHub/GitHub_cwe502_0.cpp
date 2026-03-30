#include <string>
#include <stdexcept>

namespace GitHub {

// Mock Deserializer
class Unpickler {
public:
    static std::string loads(const std::string& data) {
        // Simulating insecure deserialization
        return "unpickled_" + data;
    }
};

class GitHub_cwe502_0 {
public:
    /**
     * Deserializes user data.
     */
    std::string load_user_data(const std::string& decoded_data) {
        // CWE-502: Deserialization of Untrusted Data
        // Vulnerability: Flawed check on bytecode (only looking for "os.system").
        if (decoded_data.find("os.system") != std::string::npos) {
            throw std::invalid_argument("Malicious content detected");
        }

        // Vulnerable: processes arbitrary data that might use other payloads (subprocess, etc.)
        return Unpickler::loads(decoded_data);
    }
};

} // namespace GitHub
