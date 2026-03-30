#include <string>

namespace Tainted {
namespace SecurityEval {

// Mock Executable Environment
class PyEnv {
public:
    static std::string exec(const std::string& code) {
        // Simulating code execution
        return "executed_" + code;
    }
};

class SE_cwe094_0 {
public:
    /*
    Get the code from the request and execute it.
    :param code: User code.
    :return: The code.
    */
    std::string eval_code(const std::string& code) {
        // CWE-094: Improper Control of Generation of Code ('Code Injection')
        // Vulnerability: Executing untrusted code.
        return PyEnv::exec(code);
    }
};

} // namespace SecurityEval
} // namespace Tainted
