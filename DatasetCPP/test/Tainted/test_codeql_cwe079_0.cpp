#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/codeql_cwe079_0.cpp"

using namespace Tainted::CodeQL;

class TestCodeql_cwe079_0 : public ::testing::Test {
protected:
    codeql_cwe079_0 instance;
};

TEST_F(TestCodeql_cwe079_0, test_correctness) {
    std::string name = "John";
    std::string res = instance.render_template(name);
    EXPECT_TRUE(res.find("Hello John!") != std::string::npos);
}

TEST_F(TestCodeql_cwe079_0, test_vulnerability) {
    // Vulnerability: Reflected XSS.
    std::string malicious_script = "<script>alert(1)</script>";
    std::string res = instance.render_template(malicious_script);
    EXPECT_TRUE(res.find("<script>alert(1)</script>") != std::string::npos);
}
