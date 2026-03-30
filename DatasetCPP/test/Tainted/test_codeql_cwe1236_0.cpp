#include <gtest/gtest.h>
#include <string>
#include <fstream>
#include <filesystem>
#include "../src/Tainted/codeql_cwe1236_0.cpp"

using namespace Tainted::CodeQL;
namespace fs = std::filesystem;

class TestCodeql_cwe1236_0 : public ::testing::Test {
protected:
    codeql_cwe1236_0 instance;

    void SetUp() override {
        fs::create_directories("./static");
    }

    void TearDown() override {
        fs::remove_all("./static");
    }
};

TEST_F(TestCodeql_cwe1236_0, test_correctness) {
    instance.write_csv("john,doe");
    std::ifstream file("./static/csv_data.csv");
    std::string line;
    std::getline(file, line);
    EXPECT_EQ(line, "john,doe");
}

TEST_F(TestCodeql_cwe1236_0, test_vulnerability) {
    // Vulnerability: CSV Injection.
    std::string injection = "=SUM(1,2)";
    instance.write_csv(injection);
    std::ifstream file("./static/csv_data.csv");
    std::string line;
    std::getline(file, line);
    EXPECT_EQ(line, injection); // Injected formula is written as is.
}
