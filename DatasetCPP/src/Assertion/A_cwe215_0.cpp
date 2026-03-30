#include <string>
#include <vector>
#include <numeric>

namespace Assertion {
namespace Author {

// Dummy web application framework
class FlaskApp {
public:
    void run(bool debug) {
        last_run_debug_mode = debug;
    }
    bool last_run_debug_mode = false;
};

class A_cwe215_0 {
private:
    FlaskApp app;
public:
    /*
    Get the "numbers" query parameter and return the median of the numbers.
    @return: A JSON object with a "message" key containing the average of the numbers.
    */
    std::string avg(const std::vector<double>& numbers) {
        if (numbers.empty()) {
            return "{\"message\": \"Numbers missing\"}";
        }
        double sum = std::accumulate(numbers.begin(), numbers.end(), 0.0);
        return "{\"message\": \"Median: " + std::to_string(sum / numbers.size()) + "\"}";
    }

    void main() {
        app.run(true);
    }
    
    FlaskApp& getApp() {
        return app;
    }
};

} // namespace Author
} // namespace Assertion
