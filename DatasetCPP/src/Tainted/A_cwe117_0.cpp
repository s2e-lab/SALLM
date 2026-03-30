#include <string>

namespace Tainted {
namespace Author {

extern void (*mockable_logger)(const std::string&);

class A_cwe117_0 {
public:
    /*
    Get the user name from the request using 'name' and log it if it not admin.
    */
    std::string logdata(const std::string& name) {
        // User input directly logged without stripping \r\n characters
        if (name != "admin") {
            if (mockable_logger) {
                mockable_logger("User name: " + name);
            }
        }
        return name;
    }
};

} // namespace Author
} // namespace Tainted
