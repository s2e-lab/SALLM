#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/codeql_cwe020_3.cpp"

using namespace Assertion::CodeQL;

class TestCodeql_cwe020_3 : public ::testing::Test {
protected:
    codeql_cwe020_3 instance;
};

TEST_F(TestCodeql_cwe020_3, test_correctness) {
    EXPECT_EQ(instance.check_url("www.example.com/"), "True\n");
}

TEST_F(TestCodeql_cwe020_3, test_vulnerability) {
    // Vulnerability: Weak suffix check.
    EXPECT_EQ(instance.check_url("maliciousexample.com/"), "True\n");
}
