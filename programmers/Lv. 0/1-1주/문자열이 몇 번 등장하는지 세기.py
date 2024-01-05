'''
문제 설명
문자열 myString과 pat이 주어집니다. myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.
'''

def solution(myString, pat):
    answer = 0
    pat_len = len(pat)
    for i in range(len(myString)-pat_len+1):
        if myString[i:i+pat_len] == pat: # 밑에 풀이 처럼 [i:n] 뒤에 계산할 필요 없이 접두사 확인 함수로 확인하는게 더 빠를듯 
            answer += 1
    
    return answer


# 다른 사람 풀이
def solution(myString, pat):
    answer = 0
    for i, x in enumerate(myString) :
        if myString[i:].startswith(pat) :
            answer += 1
    return answer