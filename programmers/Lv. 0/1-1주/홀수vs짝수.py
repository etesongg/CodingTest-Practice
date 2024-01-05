'''
문제 설명
정수 리스트 num_list가 주어집니다. 가장 첫 번째 원소를 1번 원소라고 할 때, 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록 solution 함수를 완성해주세요. 두 값이 같을 경우 그 값을 return합니다.
'''

def solution(num_list):
    even_num = 0
    odd_num = 0
    for idx, val in enumerate(num_list):    # enumerate대신 for i in range(len(num_list)):
        idx = idx + 1
        if idx%2 == 1:
            odd_num += val
        else:
            even_num += val
        
    if odd_num > even_num:
        return odd_num
    else:
        return even_num
    
    
    
    
    
    