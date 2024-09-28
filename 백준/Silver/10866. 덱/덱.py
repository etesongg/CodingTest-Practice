import sys
input = sys.stdin.readline

N = int(input())

deque = []
for _ in range(N):
    splitInput = input().split()
    command = splitInput[0]
    
    if command == 'push_front':
        deque.insert(0, splitInput[1])
    elif command == 'push_back':
        deque.append(splitInput[1])
    elif command == 'pop_front':
        if deque:
            print(deque[0])
            deque.pop(0)
        else:
            print(-1)
    elif command == 'pop_back':
        if deque:
            print(deque[-1])
            deque.pop()
        else:
            print(-1)
    elif command == 'size':
        print(len(deque))
    elif command == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif command == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif command == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)