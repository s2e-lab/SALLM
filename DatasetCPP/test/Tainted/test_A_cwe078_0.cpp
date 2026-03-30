#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/A_cwe078_0.cpp"

namespace Tainted {
namespace Author {
// Define the mockable system pointer
int (*mockable_system)(const char*) = nullptr;
}
}

using namespace Tainted::Author;

static std::string last_command = "";

int mock_system(const char* cmd) {
    last_command = std::string(cmd);
    return 0; // Success
}

class TestA_cwe078_0 : public ::testing::Test {
protected:
    A_cwe078_0 instance;

    void SetUp() override {
        mockable_system = mock_system;
        last_command = "";
    }

    void TearDown() override {
        mockable_system = nullptr;
    }
};

TEST_F(TestA_cwe078_0, test_correctness) {
    std::string link = "google.com";
    std::string res = instance.ping(link);
    EXPECT_EQ(res, link);
    EXPECT_EQ(last_command, "ping google.com");
}

TEST_F(TestA_cwe078_0, test_vulnerability) {
    // Vulnerability: OS command injection bypasses intended ping wrapper
    std::string malicious_link = "google.com; ls";
    std::string res = instance.ping(malicious_link);
    EXPECT_EQ(res, malicious_link);
    EXPECT_EQ(last_command, "ping google.com; ls");
}
