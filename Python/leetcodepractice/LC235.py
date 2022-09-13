# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

from leetcodepractice.data_structure_elements import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < q.val:
            small, big = p.val, q.val
        else:
            small, big = q.val, p.val
        current = root
        while current:
            if small <= current.val <= big:
                return current
            elif current.val > big:
                current = current.left
            else:
                current = current.right
        return current
