'''
문제 설명
아무 원소도 들어있지 않은 빈 배열 X가 있습니다. 길이가 같은 정수 배열 arr과 boolean 배열 flag가 매개변수로 주어질 때, flag를 차례대로 순회하며 flag[i]가 true라면 X의 뒤에 arr[i]를 arr[i] × 2 번 추가하고, flag[i]가 false라면 X에서 마지막 arr[i]개의 원소를 제거한 뒤 X를 return 하는 solution 함수를 작성해 주세요.
'''

def solution(arr, flag):
    answer = []
    for idx, val in enumerate(arr):
        if flag[idx] == 1:
            for i in range(val*2):
                answer.append(val)
        else:
            for i in range(val):
                answer.pop()
                     
    return answer

# 다른 사람 풀이
def solution(arr, flag):
    answer = []
    for i, j in zip(arr, flag):
        if j:
            answer += [i] * i * 2
        else:
            answer = answer[:-i]
    return answer