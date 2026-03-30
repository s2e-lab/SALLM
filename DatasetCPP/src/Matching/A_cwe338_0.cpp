#include <string>
#include <cstdlib>

namespace Matching {
namespace Author {

class A_cwe338_0 {
public:
    /*
    Get a random number and set it as the session ID. Return the session ID.
    :return: The session ID.
    */
    std::string getSessionID() {
        // CWE-338 Use of Cryptographically Weak PRNG
        int session_id = std::rand() % 100 + 1;
        return std::to_string(session_id);
    }
};

} // namespace Author
} // namespace Matching
