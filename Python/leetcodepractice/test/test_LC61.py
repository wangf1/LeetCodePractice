import unittest
from unittest import TestCase

from leetcodepractice.study_plan_leetcode75.LC61 import LC61
from leetcodepractice.test.LCTestUtils import build_node_list, verify_node_list


class TestLC61(TestCase):
    def test_rotate_right(self):
        testee = LC61()
        new_head = testee.rotateRight(build_node_list([0, 1, 2]), -4)
        verify_node_list([1, 2, 0], new_head)


if __name__ == '__main__':
    unittest.main()
