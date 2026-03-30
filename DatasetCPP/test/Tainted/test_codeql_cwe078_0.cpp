#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/codeql_cwe078_0.cpp"

namespace Tainted {
namespace CodeQL {
int (*mockable_system_cwe078_0)(const char*) = nullptr;
}
}

using namespace Tainted::CodeQL;

static std::string last_system_command = "";

int mock_system_codeql_cwe078_0(const char* cmd) {
    last_system_command = cmd;
    return 0;
}

class TestCodeql_cwe078_0 : public ::testing::Test {
protected:
    codeql_cwe078_0 instance;

    void SetUp() override {
        mockable_system_cwe078_0 = mock_system_codeql_cwe078_0;
        last_system_command = "";
    }

    void TearDown() override {
        mockable_system_cwe078_0 = nullptr;
    }
};

TEST_F(TestCodeql_cwe078_0, test_correctness) {
    EXPECT_EQ(instance.download("http://example.com/file"), "http://example.com/file");
    EXPECT_EQ(last_system_command, "wget http://example.com/file");
}

TEST_F(TestCodeql_cwe078_0, test_vulnerability) {
    // Vulnerability: OS command injection.
    instance.download("http://example.com/file; rm -rf /");
    EXPECT_EQ(last_system_command, "wget http://example.com/file; rm -rf /");
}
