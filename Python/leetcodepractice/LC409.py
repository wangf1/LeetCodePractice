import collections


class LC409:
    def longestPalindrome(self, s: str) -> int:
        palindrome_length = 0
        has_odd = False
        for v in collections.Counter(s).values():
            if v % 2 == 0:
                palindrome_length += v
            else:
                palindrome_length += (v - 1)
                has_odd = True
        if has_odd:
            palindrome_length += 1
        return palindrome_length


if __name__ == '__main__':
    length = LC409().longestPalindrome(
        'civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiem'
        'ldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatn'
        'ationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecrate'
        'wecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddor'
        'detractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthel'
        'ivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforu'
        'stobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcausef'
        'orwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthis'
        'nationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfro'
        'mtheearth')
    if length != 983:
        raise ValueError("Should be 983")
