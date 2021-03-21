"""
This is encoder.
Example: #TODO
"""

a = input()
b = ''
i = 0
j = len(a)

if j == 1:
    print(a + str(1))

while i+1 < j:
    n = 1
    while i+1 < j and a[i] == a[i+1]:
        n += 1
        i += 1

    b = b + str(a[i]) + str(n)
    i += 1

if j > 1 and a[-2] != a[-1]:
    b = b + str(a[-1]) + str(1)

print(b)
