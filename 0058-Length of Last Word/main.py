
def lengthOfLastWord(s):
    # s = s.strip()   #remove leading like spaces
    # print(s)
    # if not s:
    #     return 0
    # s = s.split(' ')
    # return len(s[-1])
    return len(s.strip().split(' ')[-1])

print(lengthOfLastWord("Hello World")) # 5