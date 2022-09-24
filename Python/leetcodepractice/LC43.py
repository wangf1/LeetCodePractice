# https://leetcode.com/problems/multiply-strings


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        len1 = len(num1)
        len2 = len(num2)
        # 10*10 = 100, 99*99 = 9801, I can see the max_len of answer is len(num1)+len(num2), the min length is max_len-1
        answer = [0] * (len1 + len2)
        for i in reversed(range(len1)):
            for j in reversed(range(len2)):
                tail_0s = (len1 - 1 - i) + (len2 - 1 - j)
                multi = int(num2[j]) * int(num1[i]) + answer[-tail_0s - 1]
                answer[-tail_0s - 1] = multi % 10
                answer[-tail_0s - 2] += multi // 10

                # element in answer can temporarily greater than 9
                # if answer[-tail_0s - 2] >= 10:
                #     print(
                #         f"Temporarily greater than 9: answer[{-tail_0s - 2}] -> {answer[-tail_0s - 2]}")

        if answer[0] == 0:
            del answer[0]  # May have one redundant leading 0
        return ''.join(str(x) for x in answer)


if __name__ == '__main__':
    result = Solution().multiply("2", "3")
    expected = "6"
    assert result == expected, f"Result should be {expected}, but {result}"

    result = Solution().multiply("123", "456")
    expected = "56088"
    assert result == expected, f"Result should be {expected}, but {result}"

    result = Solution().multiply("999", "999")
    expected = "998001"
    assert result == expected, f"Result should be {expected}, but {result}"

    result = Solution().multiply("999", "0")
    expected = "0"
    assert result == expected, f"Result should be {expected}, but {result}"

    result = Solution().multiply("11", "999999")
    expected = "10999989"
    assert result == expected, f"Result should be {expected}, but {result}"
