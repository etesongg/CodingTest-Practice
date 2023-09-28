'''
문제 설명
어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
문자열 my_string과 is_suffix가 주어질 때, is_suffix가 my_string의 접미사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.

입출력 예
my_string	is_suffix	result
"banana"	"ana"	1
"banana"	"nan"	0
"banana"	"wxyz"	0
"banana"	"abanana"	0
'''

def solution(my_string, is_suffix):
    answer_list = [my_string[i:] for i in range(len(my_string))]
    answer = int(is_suffix in answer_list) # True, False를 0, 1이 되도록 변환
    return answer


# 다른 사람 풀이
def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))

'''
endswith() 함수 설명
- 정의된 문자열이 지정된 접미사로 끝나면 True를 돌려주고, 그렇지 않으면 False를 돌려줌 
접미사는 찾고자 하는 접미사들의 튜플이 될 수 도 있음
선택적 start가 제공되면 그 위치에서 검사를 시작함, 선택적 end를 사용하면 해당위치에서 비교를 중단함
>> str.endswith(접미사[, start [,end]])
'''