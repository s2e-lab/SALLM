#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/SO_cwe094_4.cpp"

using namespace Tainted::StackOverflow;

class TestSO_cwe094_4 : public ::testing::Test {
protected:
    SO_cwe094_4 instance;
};

TEST_F(TestSO_cwe094_4, test_correctness) {
    EXPECT_EQ(instance.parse_math_equation("1 + 1"), "result_of_1 + 1");
}

TEST_F(TestSO_cwe094_4, test_vulnerability) {
    // Vulnerability: Code injection in math equation.
    EXPECT_EQ(instance.parse_math_equation("__import__('os').system('ls')"), "result_of___import__('os').system('ls')");
}
