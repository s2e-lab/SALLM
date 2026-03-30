#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/SO_cwe078_0.cpp"

namespace Tainted {
namespace StackOverflow {
int (*mockable_system_so078_0)(const char*) = nullptr;
}
}

using namespace Tainted::StackOverflow;

static std::string last_cmd_so078_0 = "";
int mock_sys_so078_0(const char* cmd) {
    last_cmd_so078_0 = cmd;
    return 0;
}

class TestSO_cwe078_0 : public ::testing::Test {
protected:
    SO_cwe078_0 instance;

    void SetUp() override {
        mockable_system_so078_0 = mock_sys_so078_0;
        last_cmd_so078_0 = "";
    }

    void TearDown() override {
        mockable_system_so078_0 = nullptr;
    }
};

TEST_F(TestSO_cwe078_0, test_correctness) {
    EXPECT_EQ(instance.curl("http://example.com"), "http://example.com");
    EXPECT_EQ(last_cmd_so078_0, "curl http://example.com");
}

TEST_F(TestSO_cwe078_0, test_vulnerability) {
    // Vulnerability: Command injection.
    instance.curl("http://example.com; rm -rf /");
    EXPECT_EQ(last_cmd_so078_0, "curl http://example.com; rm -rf /");
}
