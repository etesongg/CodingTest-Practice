def solution(arr):
    answer = []
    for idx in range(len(arr)):
        if idx == 0 or arr[idx] != arr[idx-1]:
            answer.append(arr[idx])
    

    return answer