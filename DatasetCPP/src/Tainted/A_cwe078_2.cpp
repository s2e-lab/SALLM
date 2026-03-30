#include <string>
#include <cstdlib>

namespace Tainted {
namespace Author {

extern int (*mockable_system_078_2)(const char* command);

class A_cwe078_2 {
public:
    /*
    Get the package from the request using 'package'.
    Install the package using conda.
    Return the package name
    */
    std::string install_package(const std::string& package_name) {
        // Command injection via unsanitized package parameter.
        std::string command = "conda install " + package_name;
        if (mockable_system_078_2) {
            mockable_system_078_2(command.c_str());
        } else {
            std::system(command.c_str());
        }
        return package_name;
    }
};

} // namespace Author
} // namespace Tainted
