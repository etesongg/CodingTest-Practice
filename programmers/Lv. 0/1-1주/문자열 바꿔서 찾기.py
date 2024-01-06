'''
문제 설명
문자 "A"와 "B"로 이루어진 문자열 myString과 pat가 주어집니다. myString의 "A"를 "B"로, "B"를 "A"로 바꾼 문자열의 연속하는 부분 문자열 중 pat이 있으면 1을 아니면 0을 return 하는 solution 함수를 완성하세요.
'''

def solution(myString, pat):
    re_str = ''
    for w in myString:
        if w == 'A':
            re_str += 'B'
        else:
            re_str += 'A'
    if pat in re_str:
        return 1
    else:
        return 0
    
# replace() 사용하려고 했는데 .replace('A', 'B').replace('B', 'A')만 생각함
# answer = int(pat in myString.replace('A', 'C').replace('B', 'A').replace('C', 'B')) 