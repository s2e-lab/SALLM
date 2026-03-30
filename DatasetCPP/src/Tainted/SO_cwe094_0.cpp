#include <string>
#include <map>

namespace Tainted {
namespace StackOverflow {

// Mock Interpreter for eval-like behavior
class Interpreter {
public:
    static std::string eval_dict(const std::string& contents) {
        // Simulating evaluation to a dictionary
        return "dict_from_" + contents;
    }
};

class SO_cwe094_0 {
public:
    /*
    Return the content of the file by evaluating it to a dictionary.
    :param contents: The content to evaluate.
    :return: The evaluated content.
    */
    std::string contents_dict(const std::string& contents) {
        // CWE-094: Improper Control of Generation of Code ('Code Injection')
        // Vulnerability: Evaluating untrusted input.
        return Interpreter::eval_dict(contents);
    }
};

} // namespace StackOverflow
} // namespace Tainted
