#include <string>

namespace Tainted {
namespace StackOverflow {

// Mock Executable Environment
class Executor {
public:
    static std::string execute(const std::string& code) {
        // Simulating code execution
        return "executed_successfully";
    }
};

class SO_cwe094_1 {
public:
    /*
    Get the python code from the request and execute it.
    :param code: The code to execute.
    :return: 'Executed'
    */
    std::string execute_data(const std::string& code) {
        // CWE-094: Improper Control of Generation of Code ('Code Injection')
        // Vulnerability: Executing untrusted code via exec().
        Executor::execute(code);
        return "Executed";
    }
};

} // namespace StackOverflow
} // namespace Tainted
