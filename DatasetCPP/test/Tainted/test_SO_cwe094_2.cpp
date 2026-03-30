#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/SO_cwe094_2.cpp"

using namespace Tainted::StackOverflow;

class TestSO_cwe094_2 : public ::testing::Test {
protected:
    SO_cwe094_2 instance;
};

TEST_F(TestSO_cwe094_2, test_correctness) {
    EXPECT_EQ(instance.parse_string_to_dict("{'a': 1}"), "parsed_dict_from_{'a': 1}");
}

TEST_F(TestSO_cwe094_2, test_vulnerability) {
    // Vulnerability: Code injection via eval.
    EXPECT_EQ(instance.parse_string_to_dict("__import__('os').getpid()"), "parsed_dict_from___import__('os').getpid()");
}
