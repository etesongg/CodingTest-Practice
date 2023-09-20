# if-else one-line으로 표현하기

N = int(input())
print(f"{N} is {'even' if N % 2 == 0 else 'odd'}")

n = int(input())
print(f"{n} is odd" if n % 2 else f"{n} is even")

a = int(input())
print(f'{a} is', 'odd' if a % 2 else 'even')