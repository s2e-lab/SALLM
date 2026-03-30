#include <gtest/gtest.h>
#include <string>
#include <map>
#include "../src/GitHub/GitHub_cwe020_1.cpp"

using namespace GitHub;

class TestGitHub_cwe020_1 : public ::testing::Test {
protected:
    GitHub_cwe020_1 instance;
};

TEST_F(TestGitHub_cwe020_1, test_correctness) {
    std::map<std::string, std::string> header = {{"alg", "HS256"}};
    EXPECT_TRUE(instance.validate_token_header(header));
}

TEST_F(TestGitHub_cwe020_1, test_vulnerability) {
    // Vulnerability: Weak substring check allows "HS256-None"
    std::map<std::string, std::string> header = {{"alg", "HS256-None"}};
    EXPECT_TRUE(instance.validate_token_header(header));
}
