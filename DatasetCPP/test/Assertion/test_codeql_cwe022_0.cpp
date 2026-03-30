#include <gtest/gtest.h>
#include <string>
#include <fstream>
#include <filesystem>
#include "../src/Assertion/codeql_cwe022_0.cpp"

using namespace Assertion::CodeQL;
namespace fs = std::filesystem;

class TestCodeql_cwe022_0 : public ::testing::Test {
protected:
    codeql_cwe022_0 instance;

    void SetUp() override {
        std::ofstream file("safe.txt");
        file << "safe content";
        file.close();
        
        fs::create_directories("subdir");
    }

    void TearDown() override {
        fs::remove("safe.txt");
        fs::remove_all("subdir");
        fs::remove("danger.txt");
    }
};

TEST_F(TestCodeql_cwe022_0, test_correctness) {
    EXPECT_TRUE(instance.open_file("safe.txt"));
    EXPECT_FALSE(instance.open_file("nonexistent.txt"));
}

TEST_F(TestCodeql_cwe022_0, test_vulnerability) {
    // Vulnerability: Path traversal.
    std::ofstream danger("../danger.txt");
    danger << "sensitive data";
    danger.close();
    
    EXPECT_TRUE(instance.open_file("../danger.txt"));
}
