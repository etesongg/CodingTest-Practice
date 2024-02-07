# 단어 뒤집기2 17413
import sys
input = sys.stdin.readline

words = input().rstrip()
stack = []
flag = 0
res = ''

for word in words:
    if word == '<':
        flag = 1
        for _ in range(len(stack)):
            res += stack.pop()
    stack.append(word)
    
    if word == '>':
        flag = 0
        for _ in range(len(stack)):
            res += stack.pop(0)
     
    if word == ' ' and flag == 0:
        for i in range(len(stack)):
            if i == 0:
                stack.pop()
                continue
            res += stack.pop()
        res += ' '

if stack:
    for _ in range(len(stack)):
        res += stack.pop()
            
print(res)


            
