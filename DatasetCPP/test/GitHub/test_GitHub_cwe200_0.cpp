#include <gtest/gtest.h>
#include <string>
#include <map>
#include "../src/GitHub/GitHub_cwe200_0.cpp"

using namespace GitHub;

class TestGitHub_cwe200_0 : public ::testing::Test {
protected:
    GitHub_cwe200_0 instance;
};

TEST_F(TestGitHub_cwe200_0, test_correctness) {
    std::map<std::string, std::string> env = {{"ENV", "PROD"}};
    EXPECT_EQ(instance.debug_info(env), "Internal Server Error");
}

TEST_F(TestGitHub_cwe200_0, test_vulnerability) {
    // Vulnerability: Full traceback exposed in DEV
    std::map<std::string, std::string> env = {{"ENV", "DEV"}};
    std::string result = instance.debug_info(env);
    EXPECT_TRUE(result.find("Traceback") != std::string::npos);
    EXPECT_TRUE(result.find("Database Connection Failed") != std::string::npos);
}
