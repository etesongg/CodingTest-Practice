'''
문제 설명
문자열 my_string과 정수 배열 indices가 주어질 때, my_string에서 indices의 원소에 해당하는 인덱스의 글자를 지우고 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

입출력 예
my_string	indices	result
"apporoograpemmemprs"	[1, 16, 6, 15, 0, 10, 11, 3]	"programmers"
'''

def solution(my_string, indices):
    my_string = list(my_string)
    for i in sorted(indices, reverse=True): # 앞에서 부터 제거하면 인덱스가 변경되기 때문에 리스트 요소 역순 제거 함
        del my_string[i] # my_string.pop(indice) 가능
    return ''.join(my_string)


'''
리스트 요소 조작
- append(item): 새로운 요소를 리스트의 끝에 추가합니다.
- insert(index, item): 특정 인덱스에 새로운 요소를 삽입합니다.
- remove(item): 리스트에서 특정 요소를 제거합니다. 단, 처음으로 나오는 것만 제거됩니다.
- pop(index): 특정 인덱스의 요소를 제거하고 반환합니다. 인덱스를 지정하지 않으면 마지막 요소가 제거됩니다.
- del list[index]: 특정 인덱스의 요소를 제거합니다. pop()과 달리 반환값이 없습니다.
- sort(): 리스트의 요소를 오름차순으로 정렬합니다. 기본적으로 숫자 및 문자열의 경우 오름차순으로 정렬됩니다.
- sorted(list): 리스트의 요소를 정렬한 새로운 리스트를 반환합니다. 원본 리스트는 변경되지 않습니다.
'''
