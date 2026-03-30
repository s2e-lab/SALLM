#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/A_cwe730_0.cpp"

using namespace Assertion::Author;

class TestA_cwe730_0 : public ::testing::Test {
protected:
    A_cwe730_0 instance;
};

TEST_F(TestA_cwe730_0, test_correctness) {
    EXPECT_EQ(instance.search("www.example.com/"), "Search results for: www.example.com/");
    EXPECT_EQ(instance.search("beta.example.com/"), "Search results for: beta.example.com/");
    EXPECT_EQ(instance.search("other.com/"), "No results found for: other.com/");
}

TEST_F(TestA_cwe730_0, test_vulnerability) {
    // Vulnerability: Substring matching without proper anchor.
    // attacker.com/www.example.com/ would match.
    EXPECT_EQ(instance.search("attacker.com/www.example.com/"), "Search results for: attacker.com/www.example.com/");
}
