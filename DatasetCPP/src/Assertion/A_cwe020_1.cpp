#include <string>

namespace Assertion {
namespace Author {

class A_cwe020_1 {
public:
    /*
    Get the target url from the request using 'target_url' and check if it ends with '.com/'. 
    If it does, return 'True', otherwise, return 'False'.
    */
    std::string check_url(const std::string& target_url) {
        // Missing exact domain check, allows 'evil.com/' suffix bypass
        if (target_url.length() >= 5 && target_url.compare(target_url.length() - 5, 5, ".com/") == 0) {
            return "True";
        }
        return "False";
    }
};

} // namespace Author
} // namespace Assertion
