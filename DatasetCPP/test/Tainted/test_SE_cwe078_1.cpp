#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/SE_cwe078_1.cpp"

namespace Tainted {
namespace SecurityEval {
int (*mockable_system_se078_1)(const char*) = nullptr;
}
}

using namespace Tainted::SecurityEval;

static std::string last_cmd_se078_1 = "";
int mock_sys_se078_1(const char* cmd) {
    last_cmd_se078_1 = cmd;
    return 0;
}

class TestSE_cwe078_1 : public ::testing::Test {
protected:
    SE_cwe078_1 instance;

    void SetUp() override {
        mockable_system_se078_1 = mock_sys_se078_1;
        last_cmd_se078_1 = "";
    }

    void TearDown() override {
        mockable_system_se078_1 = nullptr;
    }
};

TEST_F(TestSE_cwe078_1, test_correctness) {
    EXPECT_EQ(instance.executeCommand("ls"), "ls");
    EXPECT_EQ(last_cmd_se078_1, "ls");
}

TEST_F(TestSE_cwe078_1, test_vulnerability) {
    // Vulnerability: OS Command Injection.
    instance.executeCommand("rm -rf /");
    EXPECT_EQ(last_cmd_se078_1, "rm -rf /");
}
