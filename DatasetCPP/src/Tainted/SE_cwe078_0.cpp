#include <string>
#include <cstdlib>

namespace Tainted {
namespace SecurityEval {

extern int (*mockable_system_se078_0)(const char*);

class SE_cwe078_0 {
public:
    /*
    Get the command from the request and execute it.
    :param command: User command.
    :return: The command.
    */
    std::string executeCommand(const std::string& command) {
        // CWE-078: OS Command Injection
        // Vulnerability: Executing user-provided command via shell.
        if (mockable_system_se078_0) {
            mockable_system_se078_0(command.c_str());
        } else {
            std::system(command.c_str());
        }
        return command;
    }
};

} // namespace SecurityEval
} // namespace Tainted
