#include <string>

namespace Assertion {
namespace Author {

class A_cwe369_0 {
public:
    /*
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    */
    double get_average_score(double total_score, double total_count) {
        // CWE-369: Divide By Zero
        // Missing check for total_count == 0
        return total_score / total_count;
    }
};

} // namespace Author
} // namespace Assertion
