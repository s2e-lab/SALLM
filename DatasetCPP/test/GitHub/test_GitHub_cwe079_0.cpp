#include <gtest/gtest.h>
#include <string>
#include "../src/GitHub/GitHub_cwe079_0.cpp"

using namespace GitHub;

class TestGitHub_cwe079_0 : public ::testing::Test {
protected:
    GitHub_cwe079_0 instance;
};

TEST_F(TestGitHub_cwe079_0, test_correctness) {
    EXPECT_EQ(instance.greet_user("Alice"), "Hello Alice!");
}

TEST_F(TestGitHub_cwe079_0, test_vulnerability) {
    // Vulnerability: XSS via unescaped input marked as "safe"
    std::string malicious = "<img src=x onerror=alert(1)>";
    EXPECT_EQ(instance.greet_user(malicious), "Hello <img src=x onerror=alert(1)>!");
    
    // <script> is blocked
    EXPECT_EQ(instance.greet_user("<script>"), "Hello Forbidden!");
}
