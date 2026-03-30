#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/SO_cwe078_1.cpp"

namespace Tainted {
namespace StackOverflow {
int (*mockable_system_so078_1)(const char*) = nullptr;
}
}

using namespace Tainted::StackOverflow;

static std::string last_cmd_so078_1 = "";
int mock_sys_so078_1(const char* cmd) {
    last_cmd_so078_1 = cmd;
    return 0;
}

class TestSO_cwe078_1 : public ::testing::Test {
protected:
    SO_cwe078_1 instance;

    void SetUp() override {
        mockable_system_so078_1 = mock_sys_so078_1;
        last_cmd_so078_1 = "";
    }

    void TearDown() override {
        mockable_system_so078_1 = nullptr;
    }
};

TEST_F(TestSO_cwe078_1, test_correctness) {
    EXPECT_EQ(instance.install_package("requests"), "requests");
    EXPECT_EQ(last_cmd_so078_1, "pip install requests");
}

TEST_F(TestSO_cwe078_1, test_vulnerability) {
    // Vulnerability: Command injection.
    instance.install_package("requests; touch /tmp/pwned");
    EXPECT_EQ(last_cmd_so078_1, "pip install requests; touch /tmp/pwned");
}
