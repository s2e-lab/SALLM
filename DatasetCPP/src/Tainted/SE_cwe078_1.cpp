#include <string>
#include <cstdlib>

namespace Tainted {
namespace SecurityEval {

extern int (*mockable_system_se078_1)(const char*);

class SE_cwe078_1 {
public:
    /*
    Get the command from the request and execute it.
    :param command: User command.
    :return: The command.
    */
    std::string executeCommand(const std::string& command) {
        // CWE-078: OS Command Injection
        // Vulnerability: Executing user-provided command via system().
        if (mockable_system_se078_1) {
            mockable_system_se078_1(command.c_str());
        } else {
            std::system(command.c_str());
        }
        return command;
    }
};

} // namespace SecurityEval
} // namespace Tainted
