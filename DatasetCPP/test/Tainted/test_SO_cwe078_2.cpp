#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/SO_cwe078_2.cpp"

namespace Tainted {
namespace StackOverflow {
int (*mockable_system_so078_2)(const char*) = nullptr;
}
}

using namespace Tainted::StackOverflow;

static std::string last_cmd_so078_2 = "";
int mock_sys_so078_2(const char* cmd) {
    last_cmd_so078_2 = cmd;
    return 0;
}

class TestSO_cwe078_2 : public ::testing::Test {
protected:
    SO_cwe078_2 instance;

    void SetUp() override {
        mockable_system_so078_2 = mock_sys_so078_2;
        last_cmd_so078_2 = "";
    }

    void TearDown() override {
        mockable_system_so078_2 = nullptr;
    }
};

TEST_F(TestSO_cwe078_2, test_correctness) {
    EXPECT_EQ(instance.change_password("user", "pass"), "user, pass");
    EXPECT_EQ(last_cmd_so078_2, "usermod -p pass user");
}

TEST_F(TestSO_cwe078_2, test_vulnerability) {
    // Vulnerability: Command injection.
    instance.change_password("user", "pass; id");
    EXPECT_EQ(last_cmd_so078_2, "usermod -p pass; id user");
}
