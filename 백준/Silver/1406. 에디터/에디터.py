import sys
input = sys.stdin.readline

basicStr = input().strip()
M = int(input().strip())

left = list(basicStr)
right = []
for _ in range(M):
    splitInput = input().split()
    command = splitInput[0]
    
    if command == "L":
        if left:
            right.append(left.pop())
    elif command == "D":
        if right:
            left.append(right.pop())
    elif command == "B":
        if left:
            left.pop()
    elif command == "P":
        left.append(splitInput[1])
print(''.join(left + right[::-1]))        