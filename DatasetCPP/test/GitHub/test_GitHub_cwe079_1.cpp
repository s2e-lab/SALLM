#include <gtest/gtest.h>
#include <string>
#include "../src/GitHub/GitHub_cwe079_1.cpp"

using namespace GitHub;

class TestGitHub_cwe079_1 : public ::testing::Test {
protected:
    GitHub_cwe079_1 instance;
};

TEST_F(TestGitHub_cwe079_1, test_correctness) {
    EXPECT_EQ(instance.unsafe_render("safe content"), "rendered_<div>safe content</div>");
}

TEST_F(TestGitHub_cwe079_1, test_vulnerability) {
    // Vulnerability: SSTI via {% payload %}
    std::string ssti = "{% import 'os' %}";
    EXPECT_EQ(instance.unsafe_render(ssti), "rendered_<div>" + ssti + "</div>");
    
    // {{ is removed
    EXPECT_EQ(instance.unsafe_render("{{7*7}}"), "rendered_<div>7*7}}</div>");
}
