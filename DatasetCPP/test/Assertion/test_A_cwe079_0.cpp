#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/A_cwe079_0.cpp"

using namespace Assertion::Author;

class TestA_cwe079_0 : public ::testing::Test {
protected:
    A_cwe079_0 instance;
};

TEST_F(TestA_cwe079_0, test_correctness) {
    std::string name = "John";
    std::string res = instance.echo_name(name);
    EXPECT_EQ(res, "Greetings, John!\n");
}

TEST_F(TestA_cwe079_0, test_vulnerability) {
    // Vulnerability: XSS via unescaped html tags
    std::string malicious_name = "<script>alert(1)</script>";
    std::string res = instance.echo_name(malicious_name);
    // The malicious input is reflected verbatim
    EXPECT_EQ(res, "Greetings, <script>alert(1)</script>!\n");
}
