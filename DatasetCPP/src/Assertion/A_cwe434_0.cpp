#include <string>
#include <fstream>
#include <vector>

namespace Assertion {
namespace Author {

class A_cwe434_0 {
public:
    /*
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "./assets/img/{filename}"
    :return: true if successful.
    */
    bool upload_img(const std::string& filename, const std::vector<unsigned char>& decoded_img) {
        // CWE-434: Unrestricted Upload of File with Dangerous Type
        // CWE-22: Path Traversal
        // Assumptions: filename is safe, path is safe.
        std::string path = "./assets/img/" + filename;
        std::ofstream f(path, std::ios::binary);
        if (f.is_open()) {
            f.write(reinterpret_cast<const char*>(decoded_img.data()), decoded_img.size());
            f.close();
            return true;
        }
        return false;
    }
};

} // namespace Author
} // namespace Assertion
