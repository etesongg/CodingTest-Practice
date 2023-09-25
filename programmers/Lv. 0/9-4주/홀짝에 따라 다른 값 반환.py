'''
문제 설명
양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.

입출력 예
n	result
7	16
10	220
'''

def solution(n):
    answer = 0
    if n%2 == 1: # oddoreven = "odd" if n%2 == 1 else "even" 변수 정의해 홀짝 판단 if oddoreven == "odd": 
        for i in range(1, n+1, 2):
            answer += i
    else:
        for i in range(2, n+1, 2):
            answer += i*i
    return answer



# 다른 사람 풀이
def solution(n):
    if n%2: # n%2 == 1 즉, 홀수 일때 실행
        return sum(range(1,n+1,2))
    return sum([i*i for i in range(2,n+1,2)])

