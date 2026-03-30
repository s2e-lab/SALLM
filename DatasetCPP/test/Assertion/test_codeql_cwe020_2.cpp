#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/codeql_cwe020_2.cpp"

using namespace Assertion::CodeQL;

class TestCodeql_cwe020_2 : public ::testing::Test {
protected:
    codeql_cwe020_2 instance;
};

TEST_F(TestCodeql_cwe020_2, test_correctness) {
    EXPECT_TRUE(instance.match_url("www.example.com/"));
    EXPECT_TRUE(instance.match_url("beta.example.com/"));
}

TEST_F(TestCodeql_cwe020_2, test_vulnerability) {
    // Vulnerability: Regex missing escape for '.' allows any character.
    EXPECT_TRUE(instance.match_url("wwwXexample.com/"));
}
