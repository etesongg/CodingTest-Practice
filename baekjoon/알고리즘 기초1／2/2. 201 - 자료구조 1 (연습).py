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

# 17298 오큰수
# 크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.
# 예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
NGE = [-1] * N
stack = [0]

for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()] = A[i]
    stack.append(i)

print(*NGE)

# 17299 오등큰수
from collections import Counter # 각각의 데이터 개수를 셀 수 있음 Counter({1: 3, 2: 2, 3: 1, 4: 1, 5: 1})
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
count = Counter(A)
stack = [0]
res = [-1] * N

for i in range(N):
    while stack and count[A[stack[-1]]] < count[A[i]]:
        res[stack.pop()] = A[i]
    stack.append(i)

res_str = map(str, res) # join()은 문자열만을 합치기 때문에 str 형태로 변환 해야 함
print(' '.join(res_str))     