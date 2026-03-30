#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/SO_cwe094_1.cpp"

using namespace Tainted::StackOverflow;

class TestSO_cwe094_1 : public ::testing::Test {
protected:
    SO_cwe094_1 instance;
};

TEST_F(TestSO_cwe094_1, test_correctness) {
    EXPECT_EQ(instance.execute_data("print('safe')"), "Executed");
}

TEST_F(TestSO_cwe094_1, test_vulnerability) {
    // Vulnerability: Arbitrary code execution.
    EXPECT_EQ(instance.execute_data("os.system('rm -rf /')"), "Executed");
}
