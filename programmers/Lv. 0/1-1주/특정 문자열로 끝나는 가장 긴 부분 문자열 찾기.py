'''
문제 설명
문자열 myString과 pat가 주어집니다. myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return 하는 solution 함수를 완성해 주세요.
'''

def solution(myString, pat):
    answer = ''
    myString_reverse = myString[::-1]
    pat_reverse = pat[::-1]
    index = 0
    for i in myString_reverse:
        if myString_reverse[index:index+len(pat)] == pat_reverse:
            break
        index += 1
    answer = myString_reverse[index:][::-1]
    
    return answer

# 다른 사람 풀이
def solution(myString, pat):
    return myString[:len(myString) - myString[::-1].index(pat[::-1])]