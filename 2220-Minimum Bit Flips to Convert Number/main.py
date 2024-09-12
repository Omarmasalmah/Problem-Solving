
def minBitFlips(start, goal):
    n = len(start)
    flips = 0
    flip = [0] * n
    for i in range(n):
        if start[i] == goal[i]:
            if i + 1 < n:
                flip[i + 1] ^= 1
            flips += 1
    return flips if flip[-1] == 0 else -1


#main function
if __name__ == '__main__':
    print(minBitFlips([0,1,0], [1,0,0])) # 2
    print(minBitFlips([0,0,0], [0,0,0])) # 0
    print(minBitFlips([1,1,1], [1,1,1])) # 0
    print(minBitFlips([1,0,0], [1,0,0])) # 0
    print(minBitFlips([0,1,1], [1,0,0])) # -1
    