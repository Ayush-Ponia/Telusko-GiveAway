# pascal triangle  using combinatorics formula
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def  pascal(n):
    triangle = []

    for i in range(n):
        row = []

        for j in range(i + 1):
            coef = factorial(i) // (factorial(j) * factorial(i - j))
            row.append(coef)

        triangle.append(row)

    max_digits = len(str(triangle[-1][-1]))

    for i in range(n):
        print(" " * (n - i - 1) * (max_digits + 1), end="")
        for num in triangle[i]:
            spaces = " " * (max_digits - len(str(num)))
            print(f"{num}{spaces}", end=" " * 2)
        print()

pascal(5)