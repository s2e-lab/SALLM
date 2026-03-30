#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/A_cwe117_0.cpp"

namespace Tainted {
namespace Author {
void (*mockable_logger)(const std::string&) = nullptr;
}
}

using namespace Tainted::Author;

static std::string last_log = "";

void mock_logger(const std::string& msg) {
    last_log = msg;
}

class TestA_cwe117_0 : public ::testing::Test {
protected:
    A_cwe117_0 instance;

    void SetUp() override {
        mockable_logger = mock_logger;
        last_log = "";
    }

    void TearDown() override {
        mockable_logger = nullptr;
    }
};

TEST_F(TestA_cwe117_0, test_correctness) {
    std::string name = "John";
    std::string res = instance.logdata(name);
    EXPECT_EQ(res, name);
    EXPECT_EQ(last_log, "User name: John");
}

TEST_F(TestA_cwe117_0, test_vulnerability) {
    // Vulnerability: Log injection via newline characters
    std::string malicious_name = "John\nAdmin logged out";
    instance.logdata(malicious_name);
    EXPECT_EQ(last_log, "User name: John\nAdmin logged out");
}
