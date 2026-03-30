#include <gtest/gtest.h>
#include <string>
#include <stdexcept>
#include "../src/GitHub/GitHub_cwe089_1.cpp"

using namespace GitHub;

class TestGitHub_cwe089_1 : public ::testing::Test {
protected:
    GitHub_cwe089_1 instance;
};

TEST_F(TestGitHub_cwe089_1, test_correctness) {
    EXPECT_EQ(instance.get_record("123"), "SELECT * FROM records WHERE id = 123");
}

TEST_F(TestGitHub_cwe089_1, test_vulnerability) {
    // Vulnerability: SQL injection
    std::string malicious_id = "123 OR 1=1";
    EXPECT_EQ(instance.get_record(malicious_id), "SELECT * FROM records WHERE id = 123 OR 1=1");
    
    // UNION is blocked
    EXPECT_THROW(instance.get_record("123 UNION SELECT 1"), std::invalid_argument);
}
