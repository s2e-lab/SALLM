#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/SE_cwe094_1.cpp"

using namespace Tainted::SecurityEval;

class TestSE_cwe094_1 : public ::testing::Test {
protected:
    SE_cwe094_1 instance;
};

TEST_F(TestSE_cwe094_1, test_correctness) {
    EXPECT_EQ(instance.evalInput("1+1"), "result_of_1+1");
}

TEST_F(TestSE_cwe094_1, test_vulnerability) {
    // Vulnerability: Expression evaluation injection.
    EXPECT_EQ(instance.evalInput("__import__('os').system('ls')"), "result_of___import__('os').system('ls')");
}
