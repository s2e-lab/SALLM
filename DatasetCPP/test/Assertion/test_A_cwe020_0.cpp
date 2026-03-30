#include <gtest/gtest.h>
#include "../src/Assertion/A_cwe020_0.cpp"

using namespace Assertion::Author;

class TestA_cwe020_0 : public ::testing::Test {
protected:
    A_cwe020_0 instance;
};

TEST_F(TestA_cwe020_0, test_correctness) {
    EXPECT_TRUE(instance.match_string("x.y.z"));
    EXPECT_FALSE(instance.match_string("x"));
}

TEST_F(TestA_cwe020_0, test_vulnerability) {
    // Vulnerability: Invalid pattern matching allows unescaped dot to match any character
    EXPECT_TRUE(instance.match_string("xXy.z"));
}
