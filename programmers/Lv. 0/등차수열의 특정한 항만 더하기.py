'''
문제 설명
두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다. 첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때, 이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return 하는 solution 함수를 작성해 주세요.

입출력 예
a	d	included	result
3	4	[true, false, false, true, true]	37
7	1	[false, false, false, true, false, false, false]	10
'''

def solution(a, d, included):
    result = 0
    for idx, option in enumerate(included):
        if option:
            result += a+(d*idx)
            
    answer = result
    return answer

    
# 다른 사람 풀이
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + d * i) * int(included[i]) # int(included[i]) False경우에는 0, 곱하면 0, 결국엔 True 값만 더함
    return answer

def solution(a, d, included):
    return sum(a + i * d for i, f in enumerate(included) if f)