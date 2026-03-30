#include <gtest/gtest.h>
#include <string>
#include "../src/Assertion/A_cwe116_0.cpp"

using namespace Assertion::Author;

class TestA_cwe116_0 : public ::testing::Test {
protected:
    A_cwe116_0 instance;
};

TEST_F(TestA_cwe116_0, test_correctness) {
    std::string content = "Hello <script>alert('xss')</script>World";
    std::string res = instance.filterScriptTags(content);
    EXPECT_EQ(res, "Hello World");
}

TEST_F(TestA_cwe116_0, test_vulnerability) {
    // Vulnerability: Naive script removal can be bypassed using non-script HTML attributes
    std::string malicious_content = "Hello <img src=x onerror=alert('xss')>World";
    std::string res = instance.filterScriptTags(malicious_content);
    
    // The malicious img tag remains unharmed
    EXPECT_EQ(res, "Hello <img src=x onerror=alert('xss')>World");
}
