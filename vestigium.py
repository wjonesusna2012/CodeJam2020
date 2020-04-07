t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    array = []
    trace = 0
    rows = 0
    columns = 0
    for j in range(1, n + 1):
        array.append(list(map(int, input().split(' '))))
    for k in range (0, n):
        trace += array[k][k]
        rowSet = set(array[k]) 
        colArray = []
        if len(rowSet) != n:
            rows += 1
        for m in range(0, n):
            colArray.append(array[m][k])
        colSet = set(colArray)

        if len(colSet) != n:
            columns += 1
    print("Case #{}: {} {} {}".format(i, trace, rows, columns))