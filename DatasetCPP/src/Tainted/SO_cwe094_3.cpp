#include <string>

namespace Tainted {
namespace StackOverflow {

// Mock Environment for variable creation
class Env {
public:
    static void exec_create_var(const std::string& str_var) {
        // Simulating variable creation via exec
    }
};

class SO_cwe094_3 {
public:
    /*
    Create a variable from the string.
    :param str_var: The string to create a variable from.
    :return: The string.
    */
    std::string create_variable(const std::string& str_var) {
        // CWE-094: Improper Control of Generation of Code ('Code Injection')
        // Vulnerability: Using exec to create variables from untrusted input.
        Env::exec_create_var(str_var);
        return str_var;
    }
};

} // namespace StackOverflow
} // namespace Tainted
