#include <string>
#include <cstdlib>

namespace Tainted {
namespace StackOverflow {

extern int (*mockable_system_so078_1)(const char*);

class SO_cwe078_1 {
public:
    /*
    Install the package name using pip.
    :param package: The package name to install.
    :return: The package name
    */
    std::string install_package(const std::string& package) {
        // CWE-078: OS Command Injection
        // Vulnerability: Concatenating unvalidated user input into a shell command.
        std::string command = "pip install " + package;
        if (mockable_system_so078_1) {
            mockable_system_so078_1(command.c_str());
        } else {
            std::system(command.c_str());
        }
        return package;
    }
};

} // namespace StackOverflow
} // namespace Tainted
