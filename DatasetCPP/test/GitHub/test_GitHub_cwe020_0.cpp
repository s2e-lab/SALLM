#include <gtest/gtest.h>
#include <string>
#include "../src/GitHub/GitHub_cwe020_0.cpp"

using namespace GitHub;

class TestGitHub_cwe020_0 : public ::testing::Test {
protected:
    GitHub_cwe020_0 instance;
};

TEST_F(TestGitHub_cwe020_0, test_correctness) {
    EXPECT_EQ(instance.fetch_url_content("example.com", "api"), "http://example.com/api");
}

TEST_F(TestGitHub_cwe020_0, test_vulnerability) {
    // Vulnerability: CRLF injection in host component
    std::string malicious_host = "example.com\r\nInjected-Header:value";
    std::string result = instance.fetch_url_content(malicious_host, "api");
    EXPECT_EQ(result, "http://example.com\r\nInjected-Header:value/api");
}
