def isAnagram(s, t):
    return sorted(s) == sorted(t)

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))