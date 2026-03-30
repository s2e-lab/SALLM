#include <string>

namespace Matching {
namespace StackOverflow {

// Mock system call
extern std::string (*mockable_system_so078_0)(const std::string&);

class SO_cwe078_0 {
public:
    /**
     * Take the bash command from the request and execute it.
     */
    std::string execute_bash(const std::string& command) {
        // CWE-078: OS Command Injection
        // Vulnerability: Executing untrusted command via shell.
        if (mockable_system_so078_0) {
            return mockable_system_so078_0(command);
        }
        return "Executed: " + command;
    }
};

} // namespace StackOverflow
} // namespace Matching
