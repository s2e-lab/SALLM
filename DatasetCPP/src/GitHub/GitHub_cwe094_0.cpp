#include <string>
#include <map>

namespace GitHub {

// Mock Interpreter for eval()
class Interpreter {
public:
    static std::string eval(const std::string& expr) {
        // Simulating code execution
        if (expr == "7*7") return "49";
        return "result_of_" + expr;
    }
};

class GitHub_cwe094_0 {
public:
    /**
     * Parses and evaluates a mathematical expression from the user.
     */
    std::string parse_math(const std::string& expr) {
        if (expr.empty()) return "No expression";
        
        // Flawed sanitization: blocks certain keywords but not all dangerous constructs
        if (expr.find("import") != std::string::npos || expr.find("os") != std::string::npos) {
            return "Forbidden input";
        }

        // CWE-094: Improper Control of Generation of Code ('Code Injection')
        // Vulnerability: Using an interpreter to evaluate untrusted input.
        return Interpreter::eval(expr);
    }
};

} // namespace GitHub
