'''
문제 설명
boolean 변수 x1, x2, x3, x4가 매개변수로 주어질 때, 다음의 식의 true/false를 return 하는 solution 함수를 작성해 주세요.

(x1 ∨ x2) ∧ (x3 ∨ x4)

입출력 예
x1	x2	x3	x4	result
false	true	true	true	true
true	false	false	false	false
'''

def solution(x1, x2, x3, x4):
    answer = (x1 or x2) and (x3 or x4)
    return answer


# 다른 사람 풀이
def solution(x1, x2, x3, x4):
    return (x1 | x2) & (x3 | x4)

'''
and , or / &, | 차이 설명
- and 연산자: 이것은 논리 연산자로, 좌항과 우항이 모두 True일 때만 결과가 True이고, 그 외에는 항상 False

- & 비트 연산자: 이것은 비트 단위 연산을 수행, &는 대응하는 비트가 모두 1일 때만 해당 비트를 1로 설정하고, 그 외에는 해당 비트를 0으로 설정

*논리 연산자는 주로 불리언(Boolean) 값 또는 조건식을 다룰 때 사용되는 연산자
'''
