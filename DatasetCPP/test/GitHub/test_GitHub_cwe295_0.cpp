#include <gtest/gtest.h>
#include <string>
#include "../src/GitHub/GitHub_cwe295_0.cpp"

using namespace GitHub;

class TestGitHub_cwe295_0 : public ::testing::Test {
protected:
    GitHub_cwe295_0 instance;
};

TEST_F(TestGitHub_cwe295_0, test_correctness) {
    SSLContext context = instance.create_ssl_context("https://google.com");
    EXPECT_TRUE(context.check_hostname);
    EXPECT_FALSE(context.verify_mode_cert_none);
}

TEST_F(TestGitHub_cwe295_0, test_vulnerability) {
    // Vulnerability: SSL verification disabled for .internal domains
    SSLContext context = instance.create_ssl_context("https://api.internal");
    EXPECT_FALSE(context.check_hostname);
    EXPECT_TRUE(context.verify_mode_cert_none);
}
