#include <gtest/gtest.h>
#include <string>
#include <fstream>
#include <filesystem>
#include "../src/Assertion/codeql_cwe022_1.cpp"

using namespace Assertion::CodeQL;
namespace fs = std::filesystem;

class TestCodeql_cwe022_1 : public ::testing::Test {
protected:
    codeql_cwe022_1 instance;

    void SetUp() override {
        std::ofstream file("data.txt");
        file << "hello world";
        file.close();
    }

    void TearDown() override {
        fs::remove("data.txt");
        fs::remove("secret.txt");
    }
};

TEST_F(TestCodeql_cwe022_1, test_correctness) {
    EXPECT_EQ(instance.open_file("data.txt"), "hello world");
}

TEST_F(TestCodeql_cwe022_1, test_vulnerability) {
    // Vulnerability: Path traversal to read files outside the intended scope.
    std::ofstream secret("../secret.txt");
    secret << "top secret";
    secret.close();
    
    EXPECT_EQ(instance.open_file("../secret.txt"), "top secret");
}
