'''
문제 설명
정수 배열 arr가 주어집니다. 이때 arr의 원소는 1 또는 0입니다. 정수 idx가 주어졌을 때, idx보다 크면서 배열의 값이 1인 가장 작은 인덱스를 찾아서 반환하는 solution 함수를 완성해 주세요.
단, 만약 그러한 인덱스가 없다면 -1을 반환합니다.

입출력 예
arr	idx	result
[0, 0, 0, 1]	1	3
[1, 0, 0, 1, 0, 0]	4	-1
[1, 1, 1, 1, 0]	3	3
'''

def solution(arr, idx): 
    for i in range(idx, len(arr)):
        print(i)
        if arr[i]:
            return i
    return -1


# 다른 사람 풀이
def solution(arr, idx):
    answer = 0
    try:
        answer = arr.index(1, idx) # arr에서 값이 1인 요소의 첫 번째 등장 인덱스 찾기 이때, 찾기를 시작할 인덱스는 idx로 지정
    except:
        answer = -1

    return answer

'''
index() 함수 설명
- index() 함수는 파이썬 리스트에서 특정 값의 첫 번째 등장 인덱스를 반환하는 함수

list.index(value, start, end)
value: 찾고자 하는 값
start: 검색을 시작할 인덱스. 이 인덱스부터 리스트를 탐색합니다. 기본값은 0입니다.
end: 검색을 종료할 인덱스. 이 인덱스 이전까지 리스트를 탐색합니다. 기본값은 리스트의 길이입니다.
만약 해당 값이 리스트에 없으면 ValueError를 발생
'''