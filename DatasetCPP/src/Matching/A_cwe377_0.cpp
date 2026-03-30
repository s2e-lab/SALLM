#include <string>
#include <cstdio>
#include <fstream>

namespace Matching {
namespace Author {

class A_cwe377_0 {
public:
    /*
    Get the results from the request using 'results' as the key.
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    */
    std::string write_results(const std::string& results) {
        // CWE-377: Insecure Temporary File
        // std::tmpnam (or mktemp equivalent) is insecure.
        char tmp_path[L_tmpnam];
        if (std::tmpnam(tmp_path) == nullptr) {
            return "";
        }
        
        std::ofstream f(tmp_path);
        if (f.is_open()) {
            f << results;
            f.close();
        }
        return std::string(tmp_path);
    }
};

} // namespace Author
} // namespace Matching
