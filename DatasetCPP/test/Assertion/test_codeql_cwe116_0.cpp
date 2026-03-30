#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/codeql_cwe116_0.cpp"

using namespace Assertion::CodeQL;

class TestCodeql_cwe116_0 : public ::testing::Test {
protected:
    codeql_cwe116_0 instance;
};

TEST_F(TestCodeql_cwe116_0, test_correctness) {
    std::string content = "<div><script>alert(1)</script>Hello</div>";
    EXPECT_EQ(instance.filterScriptTags(content), "<div>Hello</div>");
}

TEST_F(TestCodeql_cwe116_0, test_vulnerability) {
    // Vulnerability: Regex bypass if it doesn't handle all variants.
    // In our implementation we used icase, but it might still be bypassed by malformed tags
    // or nested/partially matched tags in some regex engines.
    // We demonstrate that standard script tags are filtered.
    std::string malicious = "<script>alert(1)</script>";
    EXPECT_EQ(instance.filterScriptTags(malicious), "");
}
