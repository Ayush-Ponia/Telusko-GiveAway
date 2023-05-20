#pascal using recursion
def pascalRecursive(n):
    if n == 1:
        return [[1]]

    pvTri = pascalRecursive(n - 1)
    previous_row = pvTri[-1]

    row = [1]
    for i in range(len(previous_row) - 1):
        row.append(previous_row[i] + previous_row[i + 1])
    row.append(1)

    pvTri.append(row)
    return pvTri

def printTriangle(n):
    triangle = pascalRecursive(n)

    max_value = triangle[-1][len(triangle[-1]) // 2]
    max_digits = len(str(max_value))

    for i in range(n):
        print(" " * (n - i - 1) * (max_digits + 1), end="")
        for num in triangle[i]:
            spaces = " " * (max_digits - len(str(num)))
            print(f"{num}{spaces}", end=" " * 2)
        print()

printTriangle(5)
