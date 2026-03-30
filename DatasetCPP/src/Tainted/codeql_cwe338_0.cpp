#include <string>
#include <cstdlib>

namespace Tainted {
namespace CodeQL {

class codeql_cwe338_0 {
public:
    /*
    Generates a random password of length 8 with numbers.
    :return: A random password.
    */
    std::string generatePassword() {
        // CWE-338: Use of Cryptographically Weak PRNG
        // rand() is not secure for password generation.
        std::string password = "";
        for (int i = 0; i < 8; ++i) {
            password += std::to_string(std::rand() % 10);
        }
        return password;
    }
};

} // namespace CodeQL
} // namespace Tainted
