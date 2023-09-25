'''
문제 설명
문자들이 담겨있는 배열 arr가 주어집니다. arr의 원소들을 순서대로 이어 붙인 문자열을 return 하는 solution함수를 작성해 주세요.

입출력 예
arr	result
["a","b","c"]	"abc"
'''

def solution(arr):
    answer = ''
    for i in range(len(arr)):
        answer += arr[i] 
    return answer


# 다름 사람 풀이
def solution(arr):
    return ''.join(arr)

'''
join 함수 설명
- ''.join(리스트)
''.join(리스트)를 이용하면 매개변수로 들어온 ['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환해주는 함수인 것입니다.

- '구분자'.join(리스트)
'구분자'.join(리스트)를 이용하면 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐줍니다.
'_'.join(['a', 'b', 'c']) 라 하면 "a_b_c" 와 같은 형태로 문자열을 만들어서 반환해 줍니다.

예. 눈치 빠르신 분들은 눈치채셨겠지만
처음에 소개 해준 ''.join(리스트)는 '구분자'.join(리스트)에서 '구분자'가 그냥 공백인 것과 같습니다.

즉, 정리하자면 join함수의 찐 모양은 '구분자'.join(리스트) 입니다.
'''