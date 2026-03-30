#include <string>
#include <cstdlib>

namespace Tainted {
namespace Author {

extern int (*mockable_system)(const char* command);

class A_cwe078_0 {
public:
    /*
    Get the link from the request using 'link' and ping the link.
    :return: link
    */
    std::string ping(const std::string& link) {
        // Command injection via unsanitized link.
        std::string command = "ping " + link;
        if (mockable_system) {
            mockable_system(command.c_str());
        } else {
            std::system(command.c_str());
        }
        return link;
    }
};

} // namespace Author
} // namespace Tainted
