'''
문제 설명
1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다. 세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c라고 했을 때 얻는 점수는 다음과 같습니다.

세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) × (a2 + b2 + c2 )점을 얻습니다.
세 숫자가 모두 같다면 (a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )점을 얻습니다.
세 정수 a, b, c가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

입출력 예
a	b	c	result
2	6	1	9
5	3	3	473
4	4	4	110592
'''

def solution(a, b, c):
    if a == b and b == c:
        answer = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    elif a != b and b != c and a != c:
        answer = a+b+c
    else:
        answer = (a+b+c)*(a**2+b**2+c**2)

    return answer

# 다른 사람 풀이
def solution(a, b, c):
    answer=a+b+c
    if a==b or b==c or a==c: answer*=a**2+b**2+c**2
    if a==b==c:answer*=a**3+b**3+c**3
    return answer

def solution(a, b, c):
    check=len(set([a,b,c]))
    if check==1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)
'''
set 함수
- 주어진 시퀀스 (리스트, 튜플 등)에서 중복된 원소를 제거하고 고유한 원소만 남긴 후 이를 다시 리스트로 변환하는 역할
- set([a, b, c])를 사용하여 변수 a, b, c의 값을 모아서 중복된 값이 제거된 집합(set)을 생성
+ 순서도 없음(Unordered).
'''