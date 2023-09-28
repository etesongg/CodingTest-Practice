'''
문제 설명
문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다. queries의 원소는 [s, e] 형태로, my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다. my_string에 queries의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.

입출력 예
my_string	queries	result
"rermgorpsam"	[[2, 3], [0, 7], [5, 9], [6, 10]]	"programmers"
'''

def solution(my_string, queries):
    for a, b in queries:
        my_string = my_string[:a] + my_string[a:b+1][::-1] + my_string[b+1:] # 처음에 my_string[a:b+1:-1]로 함 이렇게 해도 my_string의 a부터 b까지 역순으로 변환하는게 아닌 my_string 전체를 역순으로 변환함
    return my_string


# 다른 사람 풀이 
def solution(my_string, queries):
    answer=list(my_string)
    for s,e in queries:
        answer[s:e+1]=answer[s:e+1][::-1]
    return ''.join(answer)