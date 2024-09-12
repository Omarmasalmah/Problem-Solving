def strStr(haystack,needle):
    if needle == "":
        return 0
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
    
#main function
if __name__ == "__main__":
    print(strStr("hello","ll"))
    print(strStr("aaaaa","bba"))
    print(strStr("",""))
    print(strStr("","a"))
    