def groupAnagrams(strs):

    dict = {}
    for i in strs:
        key = ''.join(sorted(i))
        if key in dict:
            dict[key].append(i)
        else:
            dict[key] = [i]
    return list(dict.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))