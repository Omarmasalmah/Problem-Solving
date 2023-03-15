import collections
def topKFrequent(nums, k):
    return [i[0] for i in collections.Counter(nums).most_common(k)]

def topKFrequent2(nums, k):
    numbers_dict = {}
    for i in nums:
        if i in numbers_dict:
            numbers_dict[i] += 1
        else:
            numbers_dict[i] = 1
    return [i[0] for i in sorted(numbers_dict.items(), key=lambda x: x[1], reverse=True)[:k]]


if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2

    print(topKFrequent(nums, k))