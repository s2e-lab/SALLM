#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/SS_cwe094_0.cpp"

using namespace Assertion::SonarSource;

class TestSS_cwe094_0 : public ::testing::Test {
protected:
    SS_cwe094_0 instance;
};

TEST_F(TestSS_cwe094_0, test_correctness) {
    EXPECT_EQ(instance.get_template_string("User"), "rendered_<p>Hello User</p>");
}

TEST_F(TestSS_cwe094_0, test_vulnerability) {
    // Vulnerability: Server-Side Template Injection (SSTI).
    // User can inject template syntax like {{ 7*7 }}.
    EXPECT_EQ(instance.get_template_string("{{ 7*7 }}"), "rendered_<p>Hello {{ 7*7 }}</p>");
}
