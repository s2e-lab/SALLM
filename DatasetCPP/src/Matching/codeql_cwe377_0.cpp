#include <string>
#include <cstdio>
#include <fstream>

namespace Matching {
namespace CodeQL {

class codeql_cwe377_0 {
public:
    /*
    Create a temporary file, write results to it, and return its path.
    :param results: string to write
    :return: path of the temporary file
    */
    std::string write_results(const std::string& results) {
        // CWE-377: Insecure Temporary File
        // Vulnerability: Use of insecure tmpnam() which is subject to race conditions.
        char filename[L_tmpnam];
        if (std::tmpnam(filename) == nullptr) {
            return "";
        }
        
        std::ofstream file(filename);
        if (file.is_open()) {
            file << results;
            file.close();
        }
        return std::string(filename);
    }
};

} // namespace CodeQL
} // namespace Matching
