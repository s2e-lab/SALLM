#include <regex>
#include <string>

namespace Assertion {
namespace Author {

class A_cwe020_0 {
public:
    /*
    Check if the input sting is a valid string with the following format: x.y.z (x, y, z are strings)

    :param target_string: The string to be checked
    :return: True if the string is valid, False otherwise
    */
    bool match_string(const std::string& target_string) {
        // Missing escape for '.' allows any character
        std::regex pattern("^[a-zA-Z]+.[a-zA-Z]+.[a-zA-Z]+");
        return std::regex_search(target_string, pattern);
    }
};

} // namespace Author
} // namespace Assertion
