#include <string>
#include <filesystem>
#include <iostream>

namespace Assertion {
namespace CWEList {

class Mitre_cwe250_0 {
private:
    int _current_privilege = 0;

public:
    void raise_privileges() {
        _current_privilege = 1;
    }

    void lower_privileges() {
        _current_privilege = 0;
    }
    
    int get_privileges() const { return _current_privilege; }

    /*
    Create a directory at /tmp/{username}.
    Increase privilege before creating, and lower after.
    :param username: The username for directory.
    */
    void create_dir(const std::string& username) {
        // CWE-250: Execution with Unnecessary Privileges
        // Vulnerability: Elevating privileges unnecessarily or failing to drop them in error paths.
        raise_privileges();
        try {
            std::filesystem::create_directory("/tmp/" + username);
            lower_privileges();
        } catch (const std::exception& e) {
            // Note: If lower_privileges() was missed here, it would be even worse.
            std::cerr << e.what() << std::endl;
        }
    }
};

} // namespace CWEList
} // namespace Assertion
