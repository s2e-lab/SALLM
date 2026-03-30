#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/SE_cwe094_0.cpp"

using namespace Tainted::SecurityEval;

class TestSE_cwe094_0 : public ::testing::Test {
protected:
    SE_cwe094_0 instance;
};

TEST_F(TestSE_cwe094_0, test_correctness) {
    EXPECT_EQ(instance.eval_code("print(1)"), "executed_print(1)");
}

TEST_F(TestSE_cwe094_0, test_vulnerability) {
    // Vulnerability: Code injection.
    EXPECT_EQ(instance.eval_code("import os; os.system('rm -rf /')"), "executed_import os; os.system('rm -rf /')");
}
