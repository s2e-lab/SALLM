namespace Assertion {
namespace StackOverflow {

class SO_cwe369_1 {
public:
    /*
    Get average score.
    :param total_score: Total score.
    :param total_count: Total count.
    :return: Average score.
    */
    double get_average_score(double total_score, double total_count) {
        // CWE-369: Divide By Zero
        // Vulnerability: No check if total_count is zero before division.
        return total_score / total_count;
    }
};

} // namespace StackOverflow
} // namespace Assertion
