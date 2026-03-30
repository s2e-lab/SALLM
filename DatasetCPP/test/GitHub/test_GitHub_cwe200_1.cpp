#include <gtest/gtest.h>
#include <string>
#include <map>
#include "../src/GitHub/GitHub_cwe200_1.cpp"

using namespace GitHub;

class TestGitHub_cwe200_1 : public ::testing::Test {
protected:
    GitHub_cwe200_1 instance;
};

TEST_F(TestGitHub_cwe200_1, test_correctness) {
    std::map<std::string, std::string> env = {{"FLASK_ENV", "production"}};
    EXPECT_FALSE(instance.get_debug_mode(env));
}

TEST_F(TestGitHub_cwe200_1, test_vulnerability) {
    // Vulnerability: Defaults to debug mode if environment is missing or different
    std::map<std::string, std::string> empty_env;
    EXPECT_TRUE(instance.get_debug_mode(empty_env));
    
    std::map<std::string, std::string> other_env = {{"FLASK_ENV", "development"}};
    EXPECT_TRUE(instance.get_debug_mode(other_env));
}
