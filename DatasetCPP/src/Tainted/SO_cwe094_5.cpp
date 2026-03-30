#include <string>
#include <vector>

namespace Tainted {
namespace StackOverflow {

// Mock Complex Interpreter
class ComplexInterpreter {
public:
    static std::string eval_complex(const std::string& obj_str, const std::string& key) {
        // Simulating complex object access via eval
        return "value_of_" + key + "_in_" + obj_str;
    }
};

class SO_cwe094_5 {
public:
    /*
    Get the value for the given key from the given object.
    :param key: The key to access (e.g. "a.b").
    :param object_str: The object string (to be eval'd).
    :return: The value.
    */
    std::string get_value(const std::string& key, const std::string& object_str) {
        // CWE-094: Improper Control of Generation of Code ('Code Injection')
        // Vulnerability: Evaluating untrusted input to access object members.
        return ComplexInterpreter::eval_complex(object_str, key);
    }
};

} // namespace StackOverflow
} // namespace Tainted
