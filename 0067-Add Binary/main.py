def addBinary(a,b):
    a=int(a,2)
    b=int(b,2)
    c= a+ b
    return bin(c)[2:]
   #  return bin(int(a,2)+int(b,2))[2:]

print(addBinary("1010","1011"))
print(addBinary("11","1"))
print(addBinary("1","0"))