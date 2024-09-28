import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    line = input().rstrip().split()
    
    for word in line:
        print(word[::-1], end=' ')
    print()