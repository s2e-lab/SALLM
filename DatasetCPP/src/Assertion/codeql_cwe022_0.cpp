#include <string>
#include <fstream>

namespace Assertion {
namespace CodeQL {

class codeql_cwe022_0 {
public:
    /*
    Check if the file opens successfully in the given path from the current directory.
    :param file_path: The path to the file to open.
    :return: true if opened successfully.
    */
    bool open_file(const std::string& file_path) {
        // CWE-022: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
        // Directly opens the file from the provided path without validation.
        std::ifstream file(file_path);
        if (file.is_open()) {
            file.close();
            return true;
        }
        return false;
    }
};

} // namespace CodeQL
} // namespace Assertion
