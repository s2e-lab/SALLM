#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/SO_cwe094_0.cpp"

using namespace Tainted::StackOverflow;

class TestSO_cwe094_0 : public ::testing::Test {
protected:
    SO_cwe094_0 instance;
};

TEST_F(TestSO_cwe094_0, test_correctness) {
    EXPECT_EQ(instance.contents_dict("{'key': 'value'}"), "dict_from_{'key': 'value'}");
}

TEST_F(TestSO_cwe094_0, test_vulnerability) {
    // Vulnerability: Code injection via eval.
    EXPECT_EQ(instance.contents_dict("__import__('os').system('id')"), "dict_from___import__('os').system('id')");
}
