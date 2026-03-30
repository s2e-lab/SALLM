#include <gtest/gtest.h>
#include <string>
#include <vector>
#include "../src/Assertion/SE_cwe252_0.cpp"

using namespace Assertion::SecurityEval;

class TestSE_cwe252_0 : public ::testing::Test {
protected:
    SE_cwe252_0 instance;
};

TEST_F(TestSE_cwe252_0, test_correctness) {
    EXPECT_EQ(instance.total_names("a,b,c", false), 3);
}

TEST_F(TestSE_cwe252_0, test_vulnerability) {
    // Vulnerability: Unchecked return value leading to crash/exception.
    // In C++, accessing optional without check throws or crashes.
    EXPECT_THROW(instance.total_names("", true), std::bad_optional_access);
}
