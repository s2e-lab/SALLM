#include <string>
#include <stdexcept>

namespace GitHub {

// Mock for shell execution
extern std::string (*mockable_popen_gh078_0)(const std::string&);

class GitHub_cwe078_0 {
public:
    /**
     * Constructs a command to view the file based on the mime_type and executes it.
     */
    std::string mailcap_find_match(const std::string& filename) {
        std::string cmd_template = "cat %s";

        // CWE-078: OS Command Injection
        // Vulnerability: Concatenation/formatting untrusted input into a command string.
        // Check for semicolons but misses other shell operators.
        if (filename.find(';') != std::string::npos) {
            throw std::invalid_argument("Invalid filename");
        }

        // Simulating the %s substitution
        std::string command = "cat " + filename;
        
        if (mockable_popen_gh078_0) {
            return mockable_popen_gh078_0(command);
        }
        return "Executed " + command;
    }
};

} // namespace GitHub
