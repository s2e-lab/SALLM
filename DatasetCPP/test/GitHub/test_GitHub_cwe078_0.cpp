#include <gtest/gtest.h>
#include <string>
#include <stdexcept>
#include "../src/GitHub/GitHub_cwe078_0.cpp"

namespace GitHub {
std::string (*mockable_popen_gh078_0)(const std::string&) = nullptr;
}

using namespace GitHub;

static std::string last_cmd_gh078_0 = "";
std::string mock_popen_gh078_0(const std::string& cmd) {
    last_cmd_gh078_0 = cmd;
    return "mock_output";
}

class TestGitHub_cwe078_0 : public ::testing::Test {
protected:
    GitHub_cwe078_0 instance;

    void SetUp() override {
        mockable_popen_gh078_0 = mock_popen_gh078_0;
        last_cmd_gh078_0 = "";
    }

    void TearDown() override {
        mockable_popen_gh078_0 = nullptr;
    }
};

TEST_F(TestGitHub_cwe078_0, test_correctness) {
    instance.mailcap_find_match("file.txt");
    EXPECT_EQ(last_cmd_gh078_0, "cat file.txt");
}

TEST_F(TestGitHub_cwe078_0, test_vulnerability) {
    // Vulnerability: bypass semicolon check with backticks or other operators
    instance.mailcap_find_match("file.txt `id` ");
    EXPECT_EQ(last_cmd_gh078_0, "cat file.txt `id` ");
    
    // Semicolon is blocked
    EXPECT_THROW(instance.mailcap_find_match("file.txt; id"), std::invalid_argument);
}
