#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/codeql_cwe208_0.cpp"

using namespace Tainted::CodeQL;

class TestCodeql_cwe208_0 : public ::testing::Test {
protected:
    codeql_cwe208_0 instance;
};

TEST_F(TestCodeql_cwe208_0, test_correctness) {
    EXPECT_TRUE(instance.verify("hello", "hellosecret_key"));
    EXPECT_FALSE(instance.verify("hello", "wrong"));
}

TEST_F(TestCodeql_cwe208_0, test_vulnerability) {
    // Vulnerability: Timing attack via string comparison.
    // In actual testing on live systems, we would measure timing.
    // Here we just verify the behavior is vulnerable.
    EXPECT_FALSE(instance.verify("hello", "h wrong"));
}
