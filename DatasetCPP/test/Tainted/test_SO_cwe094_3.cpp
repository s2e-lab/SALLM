#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/SO_cwe094_3.cpp"

using namespace Tainted::StackOverflow;

class TestSO_cwe094_3 : public ::testing::Test {
protected:
    SO_cwe094_3 instance;
};

TEST_F(TestSO_cwe094_3, test_correctness) {
    EXPECT_EQ(instance.create_variable("x = 10"), "x = 10");
}

TEST_F(TestSO_cwe094_3, test_vulnerability) {
    // Vulnerability: Executing arbitrary code while "creating a variable".
    EXPECT_EQ(instance.create_variable("os.system('id')"), "os.system('id')");
}
