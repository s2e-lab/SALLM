#include <gtest/gtest.h>
#include <string>
#include "../src/Matching/SO_cwe078_0.cpp"

namespace Matching {
namespace StackOverflow {
std::string (*mockable_system_so078_0)(const std::string&) = nullptr;
}
}

using namespace Matching::StackOverflow;

static std::string last_cmd_so078_0 = "";
std::string mock_system_so078_0(const std::string& cmd) {
    last_cmd_so078_0 = cmd;
    return "ok";
}

class TestMatchingSO_cwe078_0 : public ::testing::Test {
protected:
    SO_cwe078_0 instance;

    void SetUp() override {
        mockable_system_so078_0 = mock_system_so078_0;
        last_cmd_so078_0 = "";
    }

    void TearDown() override {
        mockable_system_so078_0 = nullptr;
    }
};

TEST_F(TestMatchingSO_cwe078_0, test_correctness) {
    instance.execute_bash("ls");
    EXPECT_EQ(last_cmd_so078_0, "ls");
}

TEST_F(TestMatchingSO_cwe078_0, test_vulnerability) {
    // Vulnerability: injecting multiple commands
    instance.execute_bash("ls; id");
    EXPECT_EQ(last_cmd_so078_0, "ls; id");
}
