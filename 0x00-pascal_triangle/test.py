n=20
triangle = [0]*n


for i in range (n):
    row = [0] * (i + 1)
    row[0] = 1
    row[-1] = 1
    for j in range(i):
        if j > 0 & j < i:
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]

    triangle[i] = row

print(triangle)    