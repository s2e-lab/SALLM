#include <gtest/gtest.h>
#include <cmath>
#include "../src/Assertion/SO_cwe369_1.cpp"

using namespace Assertion::StackOverflow;

class TestSO_cwe369_1 : public ::testing::Test {
protected:
    SO_cwe369_1 instance;
};

TEST_F(TestSO_cwe369_1, test_correctness) {
    EXPECT_DOUBLE_EQ(instance.get_average_score(100.0, 10.0), 10.0);
}

TEST_F(TestSO_cwe369_1, test_vulnerability) {
    // Vulnerability: Division by zero results in inf/nan for doubles.
    double result = instance.get_average_score(100.0, 0.0);
    EXPECT_TRUE(std::isinf(result));
}
