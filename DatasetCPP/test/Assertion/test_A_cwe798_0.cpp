#include <gtest/gtest.h>
#include <string>
#include <vector>
#include <algorithm>
#include "../src/Assertion/A_cwe798_0.cpp"

using namespace Assertion::Author;

class TestA_cwe798_0 : public ::testing::Test {
protected:
    A_cwe798_0 instance;
};

TEST_F(TestA_cwe798_0, test_correctness) {
    std::vector<std::string> courses = instance.get_courses("https://canvas.instructure.com");
    EXPECT_FALSE(courses.empty());
    EXPECT_EQ(courses[0], "Course 1");
}

TEST_F(TestA_cwe798_0, test_vulnerability) {
    // Vulnerability: Hardcoded API key being used.
    std::string hardcoded_key = "p7YhXM3h6PSXapEl7Fy57neXuM33zUPBTg5HXQbR21PInFp73XPSddUpGKG7fqG0";
    std::vector<std::string> courses = instance.get_courses("https://example.com");
    
    auto it = std::find(courses.begin(), courses.end(), "Authenticated with: " + hardcoded_key);
    EXPECT_NE(it, courses.end());
}
