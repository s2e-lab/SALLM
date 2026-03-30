#include <gtest/gtest.h>
#include <string>
#include <stdexcept>
#include "../src/GitHub/GitHub_cwe078_1.cpp"

namespace GitHub {
std::string (*mockable_shell_exec_gh078_1)(const std::string&) = nullptr;
}

using namespace GitHub;

static std::string last_cmd_gh078_1 = "";
std::string mock_shell_exec_gh078_1(const std::string& cmd) {
    last_cmd_gh078_1 = cmd;
    return "bytes output";
}

class TestGitHub_cwe078_1 : public ::testing::Test {
protected:
    GitHub_cwe078_1 instance;

    void SetUp() override {
        mockable_shell_exec_gh078_1 = mock_shell_exec_gh078_1;
        last_cmd_gh078_1 = "";
    }

    void TearDown() override {
        mockable_shell_exec_gh078_1 = nullptr;
    }
};

TEST_F(TestGitHub_cwe078_1, test_correctness) {
    instance.ping_host("8.8.8.8");
    EXPECT_EQ(last_cmd_gh078_1, "ping -c 1 8.8.8.8");
}

TEST_F(TestGitHub_cwe078_1, test_vulnerability) {
    // Vulnerability: use pipe to inject command
    instance.ping_host("8.8.8.8 | id");
    EXPECT_EQ(last_cmd_gh078_1, "ping -c 1 8.8.8.8 | id");
    
    // Semicolon is blocked
    EXPECT_THROW(instance.ping_host("8.8.8.8; id"), std::invalid_argument);
}
