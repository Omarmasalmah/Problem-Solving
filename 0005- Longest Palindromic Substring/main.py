def longestPalindrome(self, s):
    if len(s) < 2:
        return s
    start = 0
    end = 0
    for i in range(len(s)):
        len1 = self.expandAroundCenter(s, i, i)
        len2 = self.expandAroundCenter(s, i, i + 1)
        length = max(len1, len2)
        if length > end - start:
            start = i - (length - 1) // 2
            end = i + length // 2
    return s[start:end + 1]


def expandAroundCenter(self, s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1


if __name__ == "__main__":

    print(longestPalindrome("babad"))
    # print(s.longestPalindrome("cbbd"))
    # print(s.longestPalindrome("a"))
    # print(s.longestPalindrome("ac"))
    # print(s.longestPalindrome("bb"))
    # print(s.longestPalindrome("ccc"))
    # print(s.longestPalindrome("babadada"))
    # print(s.longestPalindrome("babadadab"))
    # print(s.longestPalindrome("babadadabab"))
    # print(s.longestPalindrome("babadadababab"))
    # print(s.longestPalindrome("babadadabababa"))
    # print(s.longestPalindrome("babadadabababab"))
    # print(s.longestPalindrome("babadadababababa"))
    # print(s.longestPalindrome("babadadababababab"))
    # print(s.longestPalindrome("babadadabababababa"))
    # print(s.longestPalindrome("babadadabababababab"))
    # print(s.longestPalindrome("babadadababababababa"))
    # print(s.longestPalindrome("babadadababababababab"))
    # print(s.longestPalindrome("babadadabababababababa"))
    # print(s.longestPalindrome("babadadabababababababab"))
    # print(s.longestPalindrome("babadadababababababababa"))
    # print(s.longestPalindrome("babadadababababababababab"))
    # print(s.longestPalindrome("babadadabababababababababa"))
    #
    #
    #
