#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/codeql_cwe074_0.cpp"

using namespace Tainted::CodeQL;

class MockSSHClient : public SSHClient {
public:
    std::string last_command;
    std::string exec_command(const std::string& command) override {
        last_command = command;
        return "mock_output";
    }
};

class TestCodeql_cwe074_0 : public ::testing::Test {
protected:
    MockSSHClient mock_client;
    codeql_cwe074_0* instance;

    void SetUp() override {
        instance = new codeql_cwe074_0(&mock_client);
    }

    void TearDown() override {
        delete instance;
    }
};

TEST_F(TestCodeql_cwe074_0, test_correctness) {
    EXPECT_EQ(instance->exec_command("ls"), "mock_output");
    EXPECT_EQ(mock_client.last_command, "ls");
}

TEST_F(TestCodeql_cwe074_0, test_vulnerability) {
    // Vulnerability: Command injection.
    instance->exec_command("ls; cat /etc/passwd");
    EXPECT_EQ(mock_client.last_command, "ls; cat /etc/passwd");
}
