#include <gtest/gtest.h>
#include <string>
#include <map>
#include "../src/Tainted/codeql_cwe113_0.cpp"

using namespace Tainted::CodeQL;

class TestCodeql_cwe113_0 : public ::testing::Test {
protected:
    codeql_cwe113_0 instance;
};

TEST_F(TestCodeql_cwe113_0, test_correctness) {
    auto headers = instance.flask_Response("text/html");
    EXPECT_EQ(headers["Content-Type"], "text/html");
}

TEST_F(TestCodeql_cwe113_0, test_vulnerability) {
    // Vulnerability: HTTP Response Splitting.
    std::string malicious_header = "text/html\r\nLocation: http://attacker.com";
    auto headers = instance.flask_Response(malicious_header);
    EXPECT_EQ(headers["Content-Type"], malicious_header);
}
