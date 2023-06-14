def Sum(first, second):
    if first + second == 10:
        print(first, "+", second)

m = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in m:
    for j in m:
        Sum(i, j)
