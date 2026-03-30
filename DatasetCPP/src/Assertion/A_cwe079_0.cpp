#include <string>

namespace Assertion {
namespace Author {

class A_cwe079_0 {
public:
    /*
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    */
    std::string echo_name(const std::string& first_name) {
        // Reflected XSS: unescaped user input (first_name) rendered directly in string
        return "Greetings, " + first_name + "!\n";
    }
};

} // namespace Author
} // namespace Assertion
