#include <gtest/gtest.h>
#include <string>
#include "../src/GitHub/GitHub_cwe434_0.cpp"

using namespace GitHub;

class TestGitHub_cwe434_0 : public ::testing::Test {
protected:
    GitHub_cwe434_0 instance;
};

TEST_F(TestGitHub_cwe434_0, test_correctness) {
    EXPECT_EQ(instance.import_data("image.png", "data"), "File uploaded: image.png");
}

TEST_F(TestGitHub_cwe434_0, test_vulnerability) {
    // Vulnerability: .php is blocked, but .phtml is not
    EXPECT_EQ(instance.import_data("script.phtml", "<?php echo 1; ?>"), "File uploaded: script.phtml");
    EXPECT_EQ(instance.import_data("script.php", "<?php echo 1; ?>"), "Invalid file type");
}
