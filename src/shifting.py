a = 0b00001010
b = 0b00000001
​
c = a & b
a = a >> 1
c = a & b
a = a >> 1
c = a & b
a = a >> 1
c = a & b
a = a >> 1
c = a & b
"""
0b00000000
0b00000001
  00000010
"""
counter = 0
counter += 1
counter += 1
​
print("counter",counter)
​
​
print(c)