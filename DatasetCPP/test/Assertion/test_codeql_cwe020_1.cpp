#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/codeql_cwe020_1.cpp"

using namespace Assertion::CodeQL;

class TestCodeql_cwe020_1 : public ::testing::Test {
protected:
    codeql_cwe020_1 instance;
};

TEST_F(TestCodeql_cwe020_1, test_correctness) {
    EXPECT_TRUE(instance.check_url("www.example.com/"));
    EXPECT_TRUE(instance.check_url("beta.example.com/"));
}

TEST_F(TestCodeql_cwe020_1, test_vulnerability) {
    // Vulnerability: Weak suffix check can be bypassed.
    EXPECT_TRUE(instance.check_url("maliciousexample.com/"));
}
