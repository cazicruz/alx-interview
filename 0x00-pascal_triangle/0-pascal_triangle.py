def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [0]*n  

    for i in range (n):
        row = [0] * (i + 1)
        row[0] = 1
        row[-1] = 1
        for j in range(1,i):
            if j > 0 & j < i:
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        triangle[i] = row
    return triangle


print(pascal_triangle(7))