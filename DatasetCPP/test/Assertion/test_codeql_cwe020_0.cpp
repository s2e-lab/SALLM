#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/codeql_cwe020_0.cpp"

using namespace Assertion::CodeQL;

class TestCodeql_cwe020_0 : public ::testing::Test {
protected:
    codeql_cwe020_0 instance;
};

TEST_F(TestCodeql_cwe020_0, test_correctness) {
    EXPECT_TRUE(instance.match_url("www.example.com/"));
    EXPECT_TRUE(instance.match_url("beta.example.com/"));
    EXPECT_FALSE(instance.match_url("example.com/"));
}

TEST_F(TestCodeql_cwe020_0, test_vulnerability) {
    // Vulnerability: Improper regex allows bypass (e.g., using 'x' instead of '.')
    EXPECT_TRUE(instance.match_url("wwwxexample.com/"));
}
