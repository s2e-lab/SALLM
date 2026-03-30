#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/SE_cwe078_0.cpp"

namespace Tainted {
namespace SecurityEval {
int (*mockable_system_se078_0)(const char*) = nullptr;
}
}

using namespace Tainted::SecurityEval;

static std::string last_cmd_se078_0 = "";
int mock_sys_se078_0(const char* cmd) {
    last_cmd_se078_0 = cmd;
    return 0;
}

class TestSE_cwe078_0 : public ::testing::Test {
protected:
    SE_cwe078_0 instance;

    void SetUp() override {
        mockable_system_se078_0 = mock_sys_se078_0;
        last_cmd_se078_0 = "";
    }

    void TearDown() override {
        mockable_system_se078_0 = nullptr;
    }
};

TEST_F(TestSE_cwe078_0, test_correctness) {
    EXPECT_EQ(instance.executeCommand("ls"), "ls");
    EXPECT_EQ(last_cmd_se078_0, "ls");
}

TEST_F(TestSE_cwe078_0, test_vulnerability) {
    // Vulnerability: OS Command Injection.
    instance.executeCommand("ls; rm -rf /");
    EXPECT_EQ(last_cmd_se078_0, "ls; rm -rf /");
}
