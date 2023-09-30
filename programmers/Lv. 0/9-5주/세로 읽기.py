'''
문제 설명
문자열 my_string과 두 정수 m, c가 주어집니다. my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.

입출력 예
my_string	m	c	result
"ihrhbakrfpndopljhygc"	4	2	"happy"
"programmers"	1	1	"programmers"
'''

def solution(my_string, m, c):
    answer = ''
    for i in range(c-1, len(my_string), m): # c-1, c-1 + m, c-1 + 2m, ...
        answer += my_string[i]
    return answer


# 다름 사람 풀이
def solution(s, m, c):
    return s[c-1::m] # 슬라이싱 문법에서 start:stop:step을 사용할 때, start와 stop은 선택적인 매개변수이다. 만약 start를 지정하지 않으면 슬라이싱은 문자열의 첫 번째 글자부터 시작하고, stop을 지정하지 않으면 문자열의 끝까지 슬라이싱한다. 