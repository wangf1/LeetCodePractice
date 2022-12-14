# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        the_map = {}
        for i in range(len(nums)):
            peer = the_map.get(target - nums[i])
            if peer is not None:
                return [i, peer]
            the_map[nums[i]] = i
        return []

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, n in enumerate(nums):
            if (target - n) in num_to_index:
                return [i, num_to_index[target - n]]
            num_to_index[n] = i


if __name__ == '__main__':
    result = Solution().twoSum([3, 3], 6)
    print(result)
