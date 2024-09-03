package leetcodepractice;

import leetcodepractice.datastructure.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class LC103 {


    class Solution {
        public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
            if (root == null) {
                return List.of();
            }
            ArrayList<List<Integer>> res = new ArrayList<List<Integer>>();
            LinkedList<TreeNode> que = new LinkedList<>();
            que.offer(root);
            boolean leftToRight = true;
            while (!que.isEmpty()) {
                ArrayList<Integer> currRes = new ArrayList<Integer>();
                int currLen = que.size();
                for (int i = 0; i < currLen; i++) {
                    TreeNode node = leftToRight ? que.pollLast() : que.poll();
                    currRes.add(node.val);
                    if (leftToRight) {
                        if (node.left != null) {
                            que.offerFirst(node.left);
                        }
                        if (node.right != null) {
                            que.offerFirst(node.right);
                        }
                    } else {
                        if (node.right != null) {
                            que.offer(node.right);
                        }
                        if (node.left != null) {
                            que.offer(node.left);
                        }
                    }
                }
                res.add(currRes);
                leftToRight = !leftToRight;
            }
            return res;
        }
    }

}
