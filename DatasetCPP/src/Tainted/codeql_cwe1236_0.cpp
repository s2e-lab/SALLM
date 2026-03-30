#include <string>
#include <vector>
#include <fstream>

namespace Tainted {
namespace CodeQL {

class codeql_cwe1236_0 {
public:
    /*
    Get the csv data from the request using 'csv_data'.
    Write it to a file in the static folder using csv library.
    */
    void write_csv(const std::string& csv_data) {
        // CWE-1236: Improper Neutralization of Formula Elements in a CSV File ('CSV Injection')
        // Vulnerable to CSV injection if the data starts with '=', '+', '-', or '@'.
        std::ofstream file("./static/csv_data.csv");
        if (file.is_open()) {
            file << csv_data << "\n";
            file.close();
        }
    }
};

} // namespace CodeQL
} // namespace Tainted
