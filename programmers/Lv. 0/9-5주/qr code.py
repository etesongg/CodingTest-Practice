'''
문제 설명
두 정수 q, r과 문자열 code가 주어질 때, code의 각 인덱스를 q로 나누었을 때 나머지가 r인 위치의 문자를 앞에서부터 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

입출력 예
q	r	code	result
3	1	"qjnwezgrpirldywt"	"jerry"
1	0	"programmers"	"programmers"
'''

def solution(q, r, code):
    answer = ''
    for idx, val in enumerate(code):
        if idx%q == r:
            answer += val
    return answer


# 다른 사람 풀이
def solution(q, r, code):
    return code[r::q] # 문자열 code의 index를 q로 나누면 q-1까지의 나머지가 q간격으로 반복되니 target 나머지가 곧 시작 index가 되고 그걸 code의 끝까지 q간격으로 반환하는거나 다름없습니다