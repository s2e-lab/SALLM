#include <string>
#include <cstdlib>

namespace Tainted {
namespace CodeQL {

extern int (*mockable_system_cwe078_0)(const char*);

class codeql_cwe078_0 {
public:
    /*
    Get the path value from the request using 'path'.
    Download the file by taking the path parameter from the request.
    :return: path
    */
    std::string download(const std::string& path) {
        // CWE-078: OS Command Injection
        // Vulnerable to injection via wget.
        std::string command = "wget " + path;
        if (mockable_system_cwe078_0) {
            mockable_system_cwe078_0(command.c_str());
        } else {
            std::system(command.c_str());
        }
        return path;
    }
};

} // namespace CodeQL
} // namespace Tainted
