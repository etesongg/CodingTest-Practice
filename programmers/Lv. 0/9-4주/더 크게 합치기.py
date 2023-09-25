'''
문제 설명
연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.
12 ⊕ 3 = 123
3 ⊕ 12 = 312
양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.
단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.

a	b	result
9	91	991
89	8	898
'''

def solution(a, b):
    ab_join = int(f'{a}{b}')
    ab_revers = int(f'{b}{a}')
    answer = ab_join if ab_join > ab_revers else ab_revers
    return answer

# 두 수의 연산값 비교하기
def solution(a, b):
    ab_join = int(f'{a}{b}')
    ab_mul = 2 * a * b
    answer = max(ab_join, ab_mul)
    # answer = max(int(f'{a}{b}'), 2*a*b)
    return answer


# 다른 사람 풀이
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))