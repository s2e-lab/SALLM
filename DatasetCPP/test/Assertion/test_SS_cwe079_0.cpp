#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/SS_cwe079_0.cpp"

using namespace Assertion::SonarSource;

class TestSS_cwe079_0 : public ::testing::Test {
protected:
    SS_cwe079_0 instance;
};

TEST_F(TestSS_cwe079_0, test_correctness) {
    std::string tmpl = "<html><body>Hello {{ name }}</body></html>";
    EXPECT_EQ(instance.no_template_engine_replace(tmpl, "User"), "<html><body>Hello User</body></html>");
}

TEST_F(TestSS_cwe079_0, test_vulnerability) {
    // Vulnerability: Reflected XSS. Input is not escaped.
    std::string tmpl = "<html><body>Hello {{ name }}</body></html>";
    std::string malicious = "<script>alert(1)</script>";
    EXPECT_EQ(instance.no_template_engine_replace(tmpl, malicious), "<html><body>Hello <script>alert(1)</script></body></html>");
}
