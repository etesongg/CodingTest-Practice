'''
문제 설명
문자열에 따라 다음과 같이 두 수의 크기를 비교하려고 합니다.

두 수가 n과 m이라면
">", "=" : n >= m
"<", "=" : n <= m
">", "!" : n > m
"<", "!" : n < m
두 문자열 ineq와 eq가 주어집니다. ineq는 "<"와 ">"중 하나고, eq는 "="와 "!"중 하나입니다. 그리고 두 정수 n과 m이 주어질 때, n과 m이 ineq와 eq의 조건에 맞으면 1을 아니면 0을 return하도록 solution 함수를 완성해주세요.

입출력 예
ineq	eq	n	m	result
"<"	"="	20	50	1
">"	"!"	41	78	0
'''

def solution(ineq, eq, n, m):
    inequality = ineq + eq
    if inequality == ">=":
        answer = 1 if n >= m else 0
    if inequality == ">!":
        answer = 1 if n > m else 0
    if inequality == "<=":
        answer = 1 if n <= m else 0
    if inequality == "<!":
        answer = 1 if n < m else 0
    return answer


# 다른 사람 풀이
def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))

def solution(ineq, eq, n, m):
    if eq == '=':
        return 1 if eval(str(n) + ineq + eq + str(m)) else 0
    else:
        return 1 if eval(str(n) + ineq + str(m)) else 0
    
def solution(ineq, eq, n, m):
    if eq == "=":
        answer = eval(str(n)+ineq+eq+str(m))
    else:
        answer = eval(str(n)+ineq+str(m))
    return int(answer)

'''
eval(expression) 함수 설명
- 하나 이상의 값으로 표현 될 수 있는 코드

1. 문자열 덧셈
a = eval('"BlockDMask" + "blog"')     BlockDMaskblog
2. 숫자 덧셈
b = eval("100 + 32")                  132
3. 내장 함수 abs
c = eval("abs(-56)")                  56
4. 리스트 길이
d = eval("len([1,2,3,4])")            4
5. round 함수
e = eval("round(1.5)")                2

but eval 함수는 사용자가 마음대로 프로그램을 조종 즉, 프로그램에 명령을 입력할 수 있다.
결국 그 말은 프로그램을 상처입히거나 해킹을 하거나 할 수 있다는 뜻과 동일

이 함수를 실제 릴리즈 하는 프로그램에서 사용한다고 하면 위험, 너무 많은 자유를 주는 그런 함수
'''