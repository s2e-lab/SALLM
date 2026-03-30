#include <gtest/gtest.h>
#include <string>
#include <fstream>
#include <filesystem>
#include "../src/Matching/codeql_cwe377_0.cpp"

using namespace Matching::CodeQL;
namespace fs = std::filesystem;

class TestCodeql_cwe377_0 : public ::testing::Test {
protected:
    codeql_cwe377_0 instance;
    std::string created_file;

    void TearDown() override {
        if (!created_file.empty()) {
            fs::remove(created_file);
        }
    }
};

TEST_F(TestCodeql_cwe377_0, test_correctness) {
    created_file = instance.write_results("some results");
    EXPECT_FALSE(created_file.empty());
    
    std::ifstream file(created_file);
    std::string content;
    std::getline(file, content);
    EXPECT_EQ(content, "some results");
}

TEST_F(TestCodeql_cwe377_0, test_vulnerability) {
    // Vulnerability: Predictable/insecure temp file name (race condition).
    // tmpnam() is marked dangerous.
    created_file = instance.write_results("secret");
    EXPECT_FALSE(created_file.empty());
}
