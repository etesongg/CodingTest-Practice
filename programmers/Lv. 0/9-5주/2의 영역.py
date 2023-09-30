'''
2의 영역
문제 설명
정수 배열 arr가 주어집니다. 배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.
단, arr에 2가 없는 경우 [-1]을 return 합니다.

입출력 예
arr	result
[1, 2, 1, 4, 5, 2, 9]	[2, 1, 4, 5, 2]
[1, 2, 1]	[2]
[1, 1, 1]	[-1]
[1, 2, 1, 2, 1, 10, 2, 1]	[2, 1, 2, 1, 10, 2]
'''

def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2):len(arr)-arr[::-1].index(2)]
# len(arr) - arr[::-1].index(2): 전체 리스트의 길이에서 역순으로 찾은 2의 인덱스를 뺀 값입니다. 이는 역순에서의 2의 실제 인덱스 값