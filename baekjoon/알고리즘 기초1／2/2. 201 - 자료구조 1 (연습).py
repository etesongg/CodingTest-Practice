# 17413 단어 뒤집기2 
import sys
input = sys.stdin.readline

words = input().rstrip()
stack = []
flag = 0
res = ''

for word in words:
    if word == "<":
        flag = 1
        for _ in range(len(stack)):
            res += stack.pop()
    stack.append(word)
    
    if word == ">":
        flag = 0
        for _ in range(len(stack)):
            res += stack.pop(0)
     
    if word == " " and flag == 0:
        for i in range(len(stack)):
            if i == 0:
                stack.pop()
                continue
            res += stack.pop()
        res += " "

if stack:
    for _ in range(len(stack)):
        res += stack.pop()
            
print(res)

# 10799 쇠막대기
import sys
input = sys.stdin.readline

laser = input().strip()
stack = []
cnt = 0

for i in range(len(laser)):
    if laser[i] == "(":
        stack.append("(")
    else:
        if i > 0 and laser[i-1] == "(":
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

print(cnt)            
