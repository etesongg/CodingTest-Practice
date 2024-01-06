'''
문제 설명
문자열 배열 strArr가 주어집니다. 배열 내의 문자열 중 "ad"라는 부분 문자열을 포함하고 있는 모든 문자열을 제거하고 남은 문자열을 순서를 유지하여 배열로 return 하는 solution 함수를 완성해 주세요.
'''

def solution(strArr):
    answer = []                 # 이 네 줄을
    for i in strArr:            # answer = [word for word in strArr if 'ad' not in word]
        if 'ad' not in i:       # 간단하게 작성하기
            answer.append(i)    #
        
    return answer

# i보다 변수 이름 더 명확하게 짓기
# 리스트 만들고 append 하는 것보다 리스트 컴프리헨션으로 간단하게 만들기 