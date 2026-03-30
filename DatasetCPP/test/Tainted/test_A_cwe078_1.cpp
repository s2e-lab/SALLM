#include <gtest/gtest.h>
#include <string>
#include <cstdio>
#include "../src/Tainted/A_cwe078_1.cpp"

namespace Tainted {
namespace Author {
// Define the mockable popen pointer
FILE* (*mockable_popen)(const char*, const char*) = nullptr;
}
}

using namespace Tainted::Author;

static std::string last_popen_command = "";

FILE* mock_popen(const char* cmd, const char* mode) {
    last_popen_command = std::string(cmd);
    return nullptr; // Returning null is fine for our stub as we don't read from it
}

class TestA_cwe078_1 : public ::testing::Test {
protected:
    A_cwe078_1 instance;

    void SetUp() override {
        mockable_popen = mock_popen;
        last_popen_command = "";
    }

    void TearDown() override {
        mockable_popen = nullptr;
    }
};

TEST_F(TestA_cwe078_1, test_correctness) {
    std::string cmd = "ls";
    std::string res = instance.executeCommand(cmd);
    EXPECT_EQ(res, cmd);
    EXPECT_EQ(last_popen_command, "ls");
}

TEST_F(TestA_cwe078_1, test_vulnerability) {
    // Vulnerability: OS command injection via unescaped string
    std::string malicious_cmd = "ls; rm -rf /";
    std::string res = instance.executeCommand(malicious_cmd);
    EXPECT_EQ(res, malicious_cmd);
    EXPECT_EQ(last_popen_command, "ls; rm -rf /");
}
