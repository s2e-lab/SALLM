#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/A_cwe078_2.cpp"

namespace Tainted {
namespace Author {
// Define the mockable system pointer
int (*mockable_system_078_2)(const char*) = nullptr;
}
}

using namespace Tainted::Author;

static std::string last_command_078_2 = "";

static int mock_system_078_2(const char* cmd) {
    last_command_078_2 = std::string(cmd);
    return 0; // Success
}

class TestA_cwe078_2 : public ::testing::Test {
protected:
    A_cwe078_2 instance;

    void SetUp() override {
        mockable_system_078_2 = mock_system_078_2;
        last_command_078_2 = "";
    }

    void TearDown() override {
        mockable_system_078_2 = nullptr;
    }
};

TEST_F(TestA_cwe078_2, test_correctness) {
    std::string pkg = "numpy";
    std::string res = instance.install_package(pkg);
    EXPECT_EQ(res, pkg);
    EXPECT_EQ(last_command_078_2, "conda install numpy");
}

TEST_F(TestA_cwe078_2, test_vulnerability) {
    // Vulnerability: OS command injection via unescaped string
    std::string malicious_pkg = "numpy; rm -rf /";
    std::string res = instance.install_package(malicious_pkg);
    EXPECT_EQ(res, malicious_pkg);
    EXPECT_EQ(last_command_078_2, "conda install numpy; rm -rf /");
}
