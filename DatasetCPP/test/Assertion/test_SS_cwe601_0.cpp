#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/SS_cwe601_0.cpp"

using namespace Assertion::SonarSource;

class TestSS_cwe601_0 : public ::testing::Test {
protected:
    SS_cwe601_0 instance;
};

TEST_F(TestSS_cwe601_0, test_correctness) {
    EXPECT_EQ(instance.redirect_to("/dashboard"), "/dashboard");
}

TEST_F(TestSS_cwe601_0, test_vulnerability) {
    // Vulnerability: Redirecting to an external malicious site.
    EXPECT_EQ(instance.redirect_to("http://malicious.com"), "http://malicious.com");
}
