#include <gtest/gtest.h>
#include <string>
#include <stdexcept>
#include "../src/GitHub/GitHub_cwe089_0.cpp"

using namespace GitHub;

class TestGitHub_cwe089_0 : public ::testing::Test {
protected:
    GitHub_cwe089_0 instance;
};

TEST_F(TestGitHub_cwe089_0, test_correctness) {
    EXPECT_EQ(instance.get_annotated_data("my_sum"), "SELECT * FROM table AS my_sum");
}

TEST_F(TestGitHub_cwe089_0, test_vulnerability) {
    // Vulnerability: SQL injection in alias key
    std::string malicious_alias = "my_sum, (SELECT 1 FROM other_table)";
    EXPECT_EQ(instance.get_annotated_data(malicious_alias), "SELECT * FROM table AS " + malicious_alias);
    
    // Semicolon is blocked
    EXPECT_THROW(instance.get_annotated_data("my_sum; DROP TABLE"), std::invalid_argument);
}
