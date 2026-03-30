#include <string>

namespace Tainted {
namespace StackOverflow {

// Mock Math Evaluator
class MathEvaluator {
public:
    static std::string eval_math(const std::string& equation) {
        // Simulating evaluation of a math equation
        return "result_of_" + equation;
    }
};

class SO_cwe094_4 {
public:
    /*
    Evaluate the math equation and return the result.
    :param equation: The math equation to evaluate.
    :return: The result of the evaluation.
    */
    std::string parse_math_equation(const std::string& equation) {
        // CWE-094: Improper Control of Generation of Code ('Code Injection')
        // Vulnerability: Using general eval() for math, allowing code execution.
        return MathEvaluator::eval_math(equation);
    }
};

} // namespace StackOverflow
} // namespace Tainted
