a = [int(i) for i in input().split()]

if len(a) == 1:
    print(' ')
    
else:
    a.sort()
    b = []
    
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            if a[i] not in b:
                b.append(a[i])
    print(*b)

"""
a, b = [int(i) for i in input().split()], []
for i in a:
    if a.count(i) > 1 and b.count(i) == 0:
        b.append(i)
for i in b:
    print(i, end=" ")
"""
