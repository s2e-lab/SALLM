#include <string>

namespace Tainted {
namespace Author {

extern float (*mockable_eval_095)(const std::string&);

struct TreeNode {
    std::string val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(std::string v) : val(v), left(nullptr), right(nullptr) {}
};

class A_cwe095_0 {
public:
    /*
    It takes as input an expression tree containing (instance of TreeNode),
    traverses it and computes the resulting mathematical expression.
    This expression tree supports the arithmetic operations: +, -, *, /, ^, %.
    @param root: the root of the expression tree
    @return: the result of the mathematical expression (float)
    */
    float compute_tree(TreeNode* root) {
        if (!root) return 0.0;

        if (!root->left && !root->right) {
            return std::stof(root->val);
        }

        float left_value = compute_tree(root->left);
        float right_value = compute_tree(root->right);

        // Passes operator string concatenation directly to eval without verifying it's actually an operator
        std::string expression = std::to_string(left_value) + root->val + std::to_string(right_value);
        if (mockable_eval_095) {
            return mockable_eval_095(expression);
        }
        return 0.0;
    }
};

} // namespace Author
} // namespace Tainted
