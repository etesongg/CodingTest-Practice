'''
문제 설명
문자열 myString이 주어집니다. myString에서 알파벳 "a"가 등장하면 전부 "A"로 변환하고, "A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 return 하는 solution 함수를 완성하세요.
'''

def solution(myString):
    answer = ''
    for i in myString:
        i = i.lower()
        if i == 'a':
            answer += 'A'
        else:
            answer += i
    return answer


# 다른 사람 풀이 
def solution(myString):
    return myString.lower().replace('a', 'A')