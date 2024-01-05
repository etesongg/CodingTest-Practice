'''
문제 설명
오늘 해야 할 일이 담긴 문자열 배열 todo_list와 각각의 일을 지금 마쳤는지를 나타내는 boolean 배열 finished가 매개변수로 주어질 때, todo_list에서 아직 마치지 못한 일들을 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
'''

def solution(todo_list, finished):
    answer = []
    false_idx = []
    for idx, val in enumerate(finished):
        if int(val) == 0:
            false_idx.append(idx)

    for idx, val in enumerate(todo_list):
        if idx in false_idx:
            answer.append(val) 
    
    return answer


# 다른 사람 풀이
def solution(todo_list, finished):
    return [work for idx, work in enumerate(todo_list) if not finished[idx]]
'''
if not finished[idx]: 현재 작업의 인덱스(idx)를 사용하여 finished 리스트에서 해당 작업이 완료되었는지를 확인합니다. not finished[idx]는 해당 작업이 완료되지 않았을 때 참(True)이 됩니다.

work: 만약 작업이 완료되지 않았다면, 현재의 작업(work)을 결과 리스트에 추가합니다.
'''

def solution(todo_list, finished):
    return [x for x, b in zip(todo_list, finished) if not b]
'''
zip(todo_list, finished): todo_list와 finished 리스트의 각각의 원소를 하나씩 묶어서 튜플을 만듭니다. 예를 들어, zip([a, b, c], [1, 0, 1])은 [(a, 1), (b, 0), (c, 1)]와 같이 튜플의 리스트를 생성합니다.

if not b: 현재 작업의 완료 여부를 검사합니다. not b는 해당 작업이 완료되지 않았을 때 참(True)이 됩니다.
작업이 완료되지 않은 경우에만 리스트에 현재의 작업(x)을 추가합니다.
'''