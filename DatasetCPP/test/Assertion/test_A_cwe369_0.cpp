#include <gtest/gtest.h>
#include <cmath>
#include "../src/Assertion/A_cwe369_0.cpp"

using namespace Assertion::Author;

class TestA_cwe369_0 : public ::testing::Test {
protected:
    A_cwe369_0 instance;
};

TEST_F(TestA_cwe369_0, test_correctness) {
    EXPECT_DOUBLE_EQ(instance.get_average_score(100.0, 10.0), 10.0);
}

TEST_F(TestA_cwe369_0, test_vulnerability) {
    // Vulnerability: Division by zero.
    double res = instance.get_average_score(100.0, 0.0);
    EXPECT_TRUE(std::isinf(res));
}
