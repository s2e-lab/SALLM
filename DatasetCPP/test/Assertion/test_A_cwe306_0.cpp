#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/A_cwe306_0.cpp"

using namespace Assertion::Author;

class TestA_cwe306_0 : public ::testing::Test {
protected:
    A_cwe306_0 instance;
};

TEST_F(TestA_cwe306_0, test_correctness) {
    // We expect it to return the dashboard since it's hardcoded
    EXPECT_EQ(instance.show_dashboard(), "dashboard.html");
}

TEST_F(TestA_cwe306_0, test_vulnerability) {
    // The vulnerability is that any unauthenticated caller gets the dashboard
    EXPECT_EQ(instance.show_dashboard(), "dashboard.html");
}
