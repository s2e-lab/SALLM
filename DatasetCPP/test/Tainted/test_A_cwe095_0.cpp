#include <gtest/gtest.h>
#include <string>
#include "../src/Tainted/A_cwe095_0.cpp"

namespace Tainted {
namespace Author {
float (*mockable_eval_095)(const std::string&) = nullptr;
}
}

using namespace Tainted::Author;

static std::string last_eval_095 = "";

float mock_eval_095(const std::string& code) {
    last_eval_095 = code;
    return 42.0; // Mock evaluation
}

class TestA_cwe095_0 : public ::testing::Test {
protected:
    A_cwe095_0 instance;

    void SetUp() override {
        mockable_eval_095 = mock_eval_095;
        last_eval_095 = "";
    }

    void TearDown() override {
        mockable_eval_095 = nullptr;
    }
};

TEST_F(TestA_cwe095_0, test_correctness) {
    TreeNode* root = new TreeNode("+");
    root->left = new TreeNode("10");
    root->right = new TreeNode("20");
    float res = instance.compute_tree(root);
    EXPECT_EQ(res, 42.0);
    EXPECT_TRUE(last_eval_095.find("+") != std::string::npos);
    delete root->left;
    delete root->right;
    delete root;
}

TEST_F(TestA_cwe095_0, test_vulnerability) {
    // Vulnerability: Operator is vulnerable to injection
    TreeNode* root = new TreeNode("; system('ls'); ");
    root->left = new TreeNode("10");
    root->right = new TreeNode("20");
    
    instance.compute_tree(root);
    EXPECT_TRUE(last_eval_095.find("system('ls')") != std::string::npos);
    
    delete root->left;
    delete root->right;
    delete root;
}
