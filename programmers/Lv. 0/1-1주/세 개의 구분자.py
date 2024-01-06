'''
문제 설명
임의의 문자열이 주어졌을 때 문자 "a", "b", "c"를 구분자로 사용해 문자열을 나누고자 합니다.

예를 들어 주어진 문자열이 "baconlettucetomato"라면 나눠진 문자열 목록은 ["onlettu", "etom", "to"] 가 됩니다.

문자열 myStr이 주어졌을 때 위 예시와 같이 "a", "b", "c"를 사용해 나눠진 문자열을 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

단, 두 구분자 사이에 다른 문자가 없을 경우에는 아무것도 저장하지 않으며, return할 배열이 빈 배열이라면 ["EMPTY"]를 return 합니다.
'''

import re 
def solution(myStr):
    answer = [part for part in re.split('a|b|c', myStr) if part]
    if len(answer) == 0:
        return ["EMPTY"]
    
    return answer

''' 
re
Python의 내장 모듈 re에는 이 경우에 사용할 수있는 split()메소드가 있습니다.
다중 구분 기호를 구분하기 위해 기본 a 또는 b 정규식 (a|b)을 사용하십시오.
'''
