#include <gtest/gtest.h>
#include <string>
#include "../src/GitHub/GitHub_cwe918_0.cpp"

namespace GitHub {
std::string (*mockable_http_get_gh918_0)(const std::string&) = nullptr;
}

using namespace GitHub;

static std::string last_requested_url_gh918_0 = "";
std::string mock_http_get_gh918_0(const std::string& url) {
    last_requested_url_gh918_0 = url;
    return "mock_content";
}

class TestGitHub_cwe918_0 : public ::testing::Test {
protected:
    GitHub_cwe918_0 instance;

    void SetUp() override {
        mockable_http_get_gh918_0 = mock_http_get_gh918_0;
        last_requested_url_gh918_0 = "";
    }

    void TearDown() override {
        mockable_http_get_gh918_0 = nullptr;
    }
};

TEST_F(TestGitHub_cwe918_0, test_correctness) {
    EXPECT_EQ(instance.fetch_url("http://google.com"), "mock_content");
    EXPECT_EQ(last_requested_url_gh918_0, "http://google.com");
}

TEST_F(TestGitHub_cwe918_0, test_vulnerability) {
    // Vulnerability: Bypassing local blacklists with 0.0.0.0
    EXPECT_EQ(instance.fetch_url("http://0.0.0.0/admin"), "mock_content");
    EXPECT_EQ(last_requested_url_gh918_0, "http://0.0.0.0/admin");
    
    // 127.0.0.1 is blocked
    EXPECT_EQ(instance.fetch_url("http://127.0.0.1/admin"), "Blocked");
}
