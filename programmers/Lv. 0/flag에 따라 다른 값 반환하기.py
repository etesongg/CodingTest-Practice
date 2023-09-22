'''
문제 설명
두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때, flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수를 작성해 주세요.
'''

def solution(a, b, flag):
    answer = a + b if flag == 1 else a - b
    return answer


# 다른 사람 풀이
def solution(a, b, flag):
    if flag: return a+b # flag가 True 일때 실행 즉, flag 1 일때 실행
    return a-b