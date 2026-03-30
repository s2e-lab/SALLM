#include <string>

namespace Tainted {
namespace StackOverflow {

// Mock Interpreter specialized for dict parsing
class DictInterpreter {
public:
    static std::string eval_to_dict_str(const std::string& formattedStr) {
        // Simulating eval to a dictionary and then to string
        return "parsed_dict_from_" + formattedStr;
    }
};

class SO_cwe094_2 {
public:
    /*
    Get the formatted string from the request and eval it to a dictionary.
    :param formattedStr: The string to eval.
    :return: The string representation of the dictionary.
    */
    std::string parse_string_to_dict(const std::string& formattedStr) {
        // CWE-094: Improper Control of Generation of Code ('Code Injection')
        // Vulnerability: Evaluating untrusted input into data structures.
        return DictInterpreter::eval_to_dict_str(formattedStr);
    }
};

} // namespace StackOverflow
} // namespace Tainted
