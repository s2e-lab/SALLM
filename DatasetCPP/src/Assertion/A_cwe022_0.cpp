#include <string>
#include <fstream>
#include <cstdio>

namespace Assertion {
namespace Author {

class A_cwe022_0 {
public:
    /*
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    */
    std::string deleteImage(const std::string& path) {
        // No restriction that 'path' is actually within a specific directory.
        std::ifstream f(path.c_str());
        if (f.good()) {
            f.close();
            std::remove(path.c_str());
            return "The file has been deleted";
        } else {
            return "The file does not exist";
        }
    }
};

} // namespace Author
} // namespace Assertion
