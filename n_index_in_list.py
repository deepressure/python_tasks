#display all indexes in a list that have value n

my_list = [int(i) for i in input().split()]
n = int(input())

if n not in my_list:
    print(f'{n} is not in a list.')
else:
    index = [i for i, val in enumerate(my_list) if val == n]
    for ind in index:
        print(ind, end = ' ')
