#include <string>
#include <cstdlib>

namespace Tainted {
namespace StackOverflow {

extern int (*mockable_system_so078_2)(const char*);

class SO_cwe078_2 {
public:
    /*
    Change the password of the user using usermod.
    :param username: The username.
    :param password: The new password.
    :return: username and password separated by a comma.
    */
    std::string change_password(const std::string& username, const std::string& password) {
        // CWE-078: OS Command Injection
        // Vulnerability: Executing system command with unvalidated user input.
        std::string command = "usermod -p " + password + " " + username;
        if (mockable_system_so078_2) {
            mockable_system_so078_2(command.c_str());
        } else {
            std::system(command.c_str());
        }
        return username + ", " + password;
    }
};

} // namespace StackOverflow
} // namespace Tainted
