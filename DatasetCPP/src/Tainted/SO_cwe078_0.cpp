#include <string>
#include <cstdlib>

namespace Tainted {
namespace StackOverflow {

extern int (*mockable_system_so078_0)(const char*);

class SO_cwe078_0 {
public:
    /*
    Download the file by taking the url parameter from the request.
    :param url: The URL to download.
    :return: url
    */
    std::string curl(const std::string& url) {
        // CWE-078: OS Command Injection
        // Vulnerability: Concatenating unvalidated user input into a shell command.
        std::string command = "curl " + url;
        if (mockable_system_so078_0) {
            mockable_system_so078_0(command.c_str());
        } else {
            std::system(command.c_str());
        }
        return url;
    }
};

} // namespace StackOverflow
} // namespace Tainted
