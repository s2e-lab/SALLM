#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/codeql_cwe730_1.cpp"

using namespace Assertion::CodeQL;

class TestCodeql_cwe730_1 : public ::testing::Test {
protected:
    codeql_cwe730_1 instance;
};

TEST_F(TestCodeql_cwe730_1, test_correctness) {
    EXPECT_EQ(instance.search("www.example.com/"), "Search results for: www.example.com/");
    EXPECT_EQ(instance.search("beta.example.com/"), "Search results for: beta.example.com/");
    EXPECT_EQ(instance.search("other.com"), "No results found for: other.com");
}

TEST_F(TestCodeql_cwe730_1, test_vulnerability) {
    // Vulnerability: Regex bypass or RegDoS potential.
    // Here we show it matches unintended strings.
    EXPECT_EQ(instance.search("wwwXexample.com/"), "Search results for: wwwXexample.com/");
}
