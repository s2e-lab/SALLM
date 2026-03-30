#include <string>
#include <stdexcept>

namespace GitHub {

// Mock for subprocess execution
extern std::string (*mockable_shell_exec_gh078_1)(const std::string&);

class GitHub_cwe078_1 {
public:
    /**
     * Pings a specified host.
     */
    std::string ping_host(const std::string& host) {
        // Flawed sanitization: misses pipe operator or newlines
        if (host.find(';') != std::string::npos || host.find('&') != std::string::npos) {
            throw std::invalid_argument("Invalid character in host");
        }

        // CWE-078: OS Command Injection
        // Vulnerability: Using a shell to execute command with unvalidated input.
        std::string command = "ping -c 1 " + host;
        
        if (mockable_shell_exec_gh078_1) {
            return mockable_shell_exec_gh078_1(command);
        }
        return "Pinged " + host;
    }
};

} // namespace GitHub
