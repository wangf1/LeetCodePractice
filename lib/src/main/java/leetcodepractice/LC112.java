package leetcodepractice;


import leetcodepractice.datastructure.TreeNode;

public class LC112 {
    class Solution {
        public boolean hasPathSum(TreeNode root, int targetSum) {
            return dfs(root, targetSum);
        }

        private boolean dfs(TreeNode root, int target) {
            if (root == null) {
                return false;
            }
            if (root.left == null && root.right == null) {
                return root.val == target;
            }
            return dfs(root.left, target - root.val) || dfs(root.right, target - root.val);
        }
    }
}
