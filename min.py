a = [int(i) for i in input().split()]
min = 0
for i in range(len(a)):
	if a[i] < min: #со знаком '>' код читается быстрее
		min = a[i]
print(min)

'''
m = a[0]
for x in a:
	if m > x:
		m = x
print(m)

'''