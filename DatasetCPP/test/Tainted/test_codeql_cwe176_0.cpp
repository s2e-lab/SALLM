#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/codeql_cwe176_0.cpp"

using namespace Tainted::CodeQL;

class TestCodeql_cwe176_0 : public ::testing::Test {
protected:
    codeql_cwe176_0 instance;
};

TEST_F(TestCodeql_cwe176_0, test_correctness) {
    EXPECT_EQ(instance.result("safe"), "safe");
    EXPECT_EQ(instance.result("<script>"), "&lt;script>");
}

TEST_F(TestCodeql_cwe176_0, test_vulnerability) {
    // Vulnerability: Normalization after escaping allows bypass.
    // Using our artificial bypass trigger '\xEF'
    std::string malicious = "\xEFscript>";
    std::string res = instance.result(malicious);
    EXPECT_TRUE(res.find("<script") != std::string::npos);
}
