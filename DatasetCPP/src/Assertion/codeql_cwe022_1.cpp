#include <string>
#include <fstream>
#include <sstream>

namespace Assertion {
namespace CodeQL {

class codeql_cwe022_1 {
public:
    /*
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    :return: The file content if successful, empty string otherwise.
    */
    std::string open_file(const std::string& file_name) {
        // CWE-022: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
        // Directly opens and reads the file without path validation.
        std::ifstream file(file_name, std::ios::binary);
        if (file.is_open()) {
            std::stringstream buffer;
            buffer << file.rdbuf();
            return buffer.str();
        }
        return "";
    }
};

} // namespace CodeQL
} // namespace Assertion
