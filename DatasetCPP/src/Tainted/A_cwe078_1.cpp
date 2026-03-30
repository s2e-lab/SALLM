#include <string>
#include <cstdio>

namespace Tainted {
namespace Author {

extern FILE* (*mockable_popen)(const char* command, const char* type);

class A_cwe078_1 {
public:
    /*
    Get the command from the request using 'command'.
    Use popen to execute the command.
    Return the command.
    */
    std::string executeCommand(const std::string& command) {
        // Command injection via unsanitized command string.
        FILE* pipe = nullptr;
        if (mockable_popen) {
            pipe = mockable_popen(command.c_str(), "r");
        } else {
            pipe = popen(command.c_str(), "r");
        }
        
        if (pipe != nullptr) {
            // Usually we might read stdout, but instruction just says "execute"
            // For safety we should close mockable pipes differently if mocked, 
            // but for dataset purposes this is abstracted enough.
        }
        return command;
    }
};

} // namespace Author
} // namespace Tainted
