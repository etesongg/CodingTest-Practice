'''
문제 설명
정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.

입출력 예
l	r	result
5	555	[5, 50, 55, 500, 505, 550, 555]
10	20	[-1]
'''

# 다른 사람 풀이
def solution(l, r):
    answer = []
    for num in range(l, r+1):
        if not set(str(num)) - {'0','5'}: 
            answer.append(num)
    return answer if answer else [-1]

# set(str(num)) - {'0', '5'}의 결과가 빈 집합이라면 (즉, 0과 5를 제외한 다른 숫자가 없다면) 해당 숫자를 결과 리스트 answer에 추가