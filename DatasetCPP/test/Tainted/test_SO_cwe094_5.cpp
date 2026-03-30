#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/SO_cwe094_5.cpp"

using namespace Tainted::StackOverflow;

class TestSO_cwe094_5 : public ::testing::Test {
protected:
    SO_cwe094_5 instance;
};

TEST_F(TestSO_cwe094_5, test_correctness) {
    EXPECT_EQ(instance.get_value("member", "{'member': 123}"), "value_of_member_in_{'member': 123}");
}

TEST_F(TestSO_cwe094_5, test_vulnerability) {
    // Vulnerability: Code injection in object string or key.
    EXPECT_EQ(instance.get_value("key", "__import__('os').system('ls')"), "value_of_key_in___import__('os').system('ls')");
}
