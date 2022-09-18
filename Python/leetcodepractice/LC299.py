# https://leetcode.com/problems/bulls-and-cows/
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        nums = [0] * 10
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                nums[s] += 1
                nums[g] -= 1
        cows = len(guess) - bulls + sum(n for n in nums if n < 0)
        return f"{bulls}A{cows}B"


if __name__ == '__main__':
    result = Solution().getHint(secret="1807", guess="7810")
    expected = "1A3B"
    assert result == expected, f"Expect {expected} but {result}"

    result = Solution().getHint(secret="1122", guess="2211")
    expected = "0A4B"
    assert result == expected, f"Expect {expected} but {result}"
