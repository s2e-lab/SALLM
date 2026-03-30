#include <string>

namespace Tainted {
namespace SecurityEval {

// Mock Evaluator
class PyEval {
public:
    static std::string eval(const std::string& expr) {
        // Simulating expression evaluation
        return "result_of_" + expr;
    }
};

class SE_cwe094_1 {
public:
    /*
    Get the inputStr as a python expression and return result.
    :param inputStr: User input string.
    :return: Result of evaluation.
    */
    std::string evalInput(const std::string& inputStr) {
        // CWE-094: Improper Control of Generation of Code ('Code Injection')
        // Vulnerability: Evaluating untrusted expressions.
        return PyEval::eval(inputStr);
    }
};

} // namespace SecurityEval
} // namespace Tainted
