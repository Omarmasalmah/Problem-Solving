def isPalindrome(self, s):
    s = s.lower()
    s = [c for c in s if c.isalnum()]
    return s == s[::-1]

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))