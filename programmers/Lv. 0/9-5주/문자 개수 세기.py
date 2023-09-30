'''
문제 설명
알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때, my_string에서 'A'의 개수, my_string에서 'B'의 개수,..., my_string에서 'Z'의 개수, my_string에서 'a'의 개수, my_string에서 'b'의 개수,..., my_string에서 'z'의 개수를 순서대로 담은 길이 52의 정수 배열을 return 하는 solution 함수를 작성해 주세요.

입출력 예
my_string	result
"Programmers"	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0]
'''

# 다른 사람 풀이
def solution(my_string):
    answer=[0]*52 # answer 리스트는 길이 52의 0으로 초기화된 리스트
    for x in my_string:
        if x.isupper(): # 대문자인 경우
            answer[ord(x)-65]+=1
        else: # 소문자인 경우
            answer[ord(x)-71]+=1
    return answer

'''
ord() 함수 설명
- ord()는 파이썬 내장 함수 중 하나로, 문자의 유니코드 코드 포인트(정수 값)를 반환 
예를 들어, ord('A')는 대문자 A의 유니코드 코드 포인트인 65를 반환하고, ord('a')는 소문자 a의 유니코드 코드 포인트인 97을 반환
예를 들어, 주어진 문자열에서 'A'가 등장하면 answer[ord('A') - 65]는 answer[0]이 되어 첫 번째 요소에 대문자 A의 등장 횟수를 저장하게 됨

아스키 코드 : 알파벳 A의 아스키 코드 → 65 / a 의 아스키 코드 → 97
answer 리스트 : 대문자(A~Z) : 인덱스 0~25 / 소문자(a~z) : 인덱스 26~51
'''