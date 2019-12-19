a = [int(i) for i in input().split()]

lenght = len(a)

if lenght == 1:
    print(a[0])

else:
    b = []
    
    for i in range(lenght):
        if i == 0:
            inter = a[-1] + a[1]
        elif i == lenght - 1:
            inter = a[i - 1] + a[0]
       else:
            inter = a[i - 1] + a[i + 1]
        b.append(inter)
    for i in range(len(b)):
        print(b[i], end = " ")
