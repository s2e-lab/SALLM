#include <string>
#include <vector>

namespace Assertion {
namespace Author {

class A_cwe798_0 {
public:
    /*
    Use the Canvas API to obtain all the courses in a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    */
    std::vector<std::string> get_courses(const std::string& canvas_url) {
        // CWE-798: Use of Hard-coded Credentials
        std::string API_KEY = "p7YhXM3h6PSXapEl7Fy57neXuM33zUPBTg5HXQbR21PInFp73XPSddUpGKG7fqG0";
        
        // Simulating API call
        return {"Course 1", "Course 2", "Authenticated with: " + API_KEY};
    }
};

} // namespace Author
} // namespace Assertion
