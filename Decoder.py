"""
This is decoder.
Example: #TODO
"""

with open('input.txt', 'r') as infile:
    s = infile.read().strip()

a = ''
b = ''
i = 0
number = ''

for i, char in enumerate(s):
    if char >= 'A':
        b = char
    else:
        number += char
        if i == len(s)-1:
            for _ in range(int(number)):
                a += b

        else:
            if s[i+1] >= 'A':
                for _ in range(int(number)):
                    a += b

                number = ''

with open('output.txt', 'w') as outfile:
    outfile.write(a)
