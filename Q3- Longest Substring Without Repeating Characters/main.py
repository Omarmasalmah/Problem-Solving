# Given a string s, find the length of the longest
# substring
#  without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Explanation: The answer is "abc", with the length of 3.
def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    max_length = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if len(set(s[i:j])) == len(s[i:j]):
                max_length = max(max_length, j - i)
    return max_length

if __name__ == "__main__":
    print(lengthOfLongestSubstring("self", "abcabcbb"))
    print(lengthOfLongestSubstring("self", "bbbbbb"))