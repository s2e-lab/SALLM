#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/codeql_cwe730_0.cpp"

using namespace Assertion::CodeQL;

class TestCodeql_cwe730_0 : public ::testing::Test {
protected:
    codeql_cwe730_0 instance;
};

TEST_F(TestCodeql_cwe730_0, test_correctness) {
    EXPECT_TRUE(instance.search_pattern("abc", "abcdef"));
    EXPECT_FALSE(instance.search_pattern("xyz", "abcdef"));
}

TEST_F(TestCodeql_cwe730_0, test_vulnerability) {
    // Vulnerability: RegDoS or malicious pattern injection.
    // Untrusted pattern is compiled and executed.
    EXPECT_TRUE(instance.search_pattern(".*", "anything"));
}
