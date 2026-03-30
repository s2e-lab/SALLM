#include <string>

namespace Tainted {
namespace CodeQL {

class codeql_cwe208_1 {
private:
    std::string admin_password = "1234";
public:
    /*
    Compare provided password with the admin password.
    :return: If the password is correct, return 'Logged in'. Otherwise, return 'Wrong password'.
    */
    std::string check_pwd(const std::string& password) {
        // CWE-208: Observable Timing Difference ('Timing Attack')
        // Non-constant-time comparison (operator==).
        if (password == admin_password) {
            return "Logged in";
        } else {
            return "Wrong password";
        }
    }
};

} // namespace CodeQL
} // namespace Tainted
