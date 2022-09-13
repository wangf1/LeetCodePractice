# https://leetcode.com/problems/flood-fill/
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old_color = image[sr][sc]
        if old_color == color:
            return image
        self._flood_fill(image, sr, sc, old_color, color)
        return image

    def _flood_fill(self, image: List[List[int]], sr: int, sc: int, old_color: int, new_color: int):
        if image[sr][sc] == old_color:
            image[sr][sc] = new_color
            if sr - 1 >= 0:
                self._flood_fill(image, sr - 1, sc, old_color, new_color, )
            if sr + 1 <= len(image) - 1:
                self._flood_fill(image, sr + 1, sc, old_color, new_color, )
            if sc - 1 >= 0:
                self._flood_fill(image, sr, sc - 1, old_color, new_color)
            if sc + 1 <= len(image[0]) - 1:
                self._flood_fill(image, sr, sc + 1, old_color, new_color)


if __name__ == "__main__":
    result = Solution().floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2)
    if result != [[2, 2, 2], [2, 2, 0], [2, 0, 1]]:
        raise ValueError(f"Result should be [[2,2,2],[2,2,0],[2,0,1]], but is {0}", result)

    result = Solution().floodFill(image=[[0, 0, 0], [0, 1, 0]], sr=0, sc=1, color=2)
    if result != [[2, 2, 2], [2, 1, 2]]:
        raise ValueError(f"Result should be [[2, 2, 2], [2, 1, 2]], but is {0}", result)
