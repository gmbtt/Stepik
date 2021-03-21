with open('input.txt', 'r') as inf:
    s = inf.readline().strip()

a = ''
b = ''
i = 0
j = 0
number = ''

for i in range(len(s)):
    if s[i] >= 'A':
        b = s[i]
    elif s[i] < 'A':
        number += s[i]
        if i == len(s)-1:
            while j < int(number):
                    a += b
                    j += 1
        else:
            if s[i+1] >= 'A':
                while j < int(number):
                    a += b
                    j += 1
                number = ''
                j = 0

with open('output.txt', 'w') as ouf:
    ouf.write(a)
