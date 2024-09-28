import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    parenthesisStr = input().strip()
    stack = []
    
    if len(parenthesisStr)%2 == 1 :
        print("NO")
        continue
    for char in parenthesisStr:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if not stack:
                print('NO')
                break
            stack.pop()
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
            
            
        