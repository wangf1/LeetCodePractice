class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        left = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res

    # Improve performance:
    # 1. Use if instead of while
    # 2. Keep max_count instead of max(count.values())
    def characterReplacement2(self, s: str, k: int) -> int:
        res = 0
        count = {}
        left = 0
        max_count = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            max_count = max(max_count, count[s[right]])
            if (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res


if __name__ == '__main__':
    input = "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
    result = Solution().characterReplacement(input, 4)
    result2 = Solution().characterReplacement2(input, 4)
    expected = 7
    assert result == result2 == expected, f"Value should be {expected}, but {result} {result2}"

    result = Solution().characterReplacement("AABABBA", 1)
    result2 = Solution().characterReplacement2("AABABBA", 1)
    expected = 4
    assert result == result2 == expected, f"Value should be {expected}, but {result} {result2}"

    result = Solution().characterReplacement("AAAABBC", 2)
    result2 = Solution().characterReplacement2("AAAABBC", 2)
    expected = 6
    assert result == result2 == expected, f"Value should be {expected}, but {result} {result2}"
