# 10828 스택
'''
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    command = input().split() #1
    
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

# 9093 단어 뒤집기 
# 문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 단, 단어의 순서는 바꿀 수 없다. 단어는 영어 알파벳으로만 이루어져 있다.
import sys
input = sys.stdin.readline
 
N = int(input())
 
for _ in range(N):
  words = input().rstrip().split() # readline은 뒤에 \n 문자가 붙기 때문에 rstrip() 사용하기 
 
  for word in words:
    print(word[::-1], end=' ')
  print()

# 9012 괄호 
# 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 
N = int(input())

for _ in range(N):
    test_case = input()
    stack =[]
    for i in range(len(test_case)):
        if test_case[i] == '(':
            stack.append('(')
        elif test_case[i] == ')':
            if not stack: # 스택에 괄호가 없을 경우
                print('NO')
                break
            stack.pop()
    else: # break 되지 않았을 경우 실행
        if not stack: 
            print("YES")
        else: 
            print("NO")

# 1874
# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.
import sys
input = sys.stdin.readline 

N = int(input())
stack = []
answer = []
flag = 0
cur = 1

for _ in range(N):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        answer.append('+')
        cur += 1
    
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)










# 
# 
