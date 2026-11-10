def reverse(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    return rev

A, B = map(int, input().split())

A = reverse(A)
B = reverse(B)

C = A + B

print(reverse(C), end="")