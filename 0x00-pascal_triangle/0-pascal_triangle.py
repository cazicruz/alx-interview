def pascal_triangle(n):
    if n <= 0:
        return []
    i = 1
    ans = []
    while (i <= n):
        if i == 1:
            ans.append([1])
            i+= 1
            
        else:
            num = str(11**(i-1))
            listNum= [int(x) for x in str(num)]
            ans.append(listNum)
            i+= 1

    for i in range(n):
        print(ans[i])