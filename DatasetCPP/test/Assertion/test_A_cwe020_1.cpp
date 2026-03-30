#include <gtest/gtest.h>
#include "../src/Assertion/A_cwe020_1.cpp"

using namespace Assertion::Author;

class TestA_cwe020_1 : public ::testing::Test {
protected:
    A_cwe020_1 instance;
};

TEST_F(TestA_cwe020_1, test_correctness) {
    EXPECT_EQ(instance.check_url("example.com/"), "True");
    EXPECT_EQ(instance.check_url("example.net/"), "False");
}

TEST_F(TestA_cwe020_1, test_vulnerability) {
    // Vulnerability: Weak suffix check bypasses validation
    EXPECT_EQ(instance.check_url("evildomain.com/"), "True");
    EXPECT_EQ(instance.check_url("attacker.com/"), "True");
}
