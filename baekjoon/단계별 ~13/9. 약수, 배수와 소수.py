# 2501 약수 구하기
# 두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성
N, K = map(int, input().split())
factors=[]

for i in range(1, N//2+1):
    if N % i == 0:
        factors.append(i)

if K > len(factors):
    print(0)
else:
    print(factors[K-1])

# 9506 약수들의 합
# n이 완전수라면, n을 n이 아닌 약수들의 합으로 나타내어 출력한다, 약수들은 오름차순으로 나열해야 한다 ,n이 완전수가 아니라면 n is NOT perfect. 를 출력한다.
while 1: 
    n = int(input())
    if n == -1:
        break
        
    factors = []    
    for i in range(1, n//2+1): # 약수 최적화
        if n % i == 0:
            factors.append(i)
    
    if n == sum(factors):
        factors_str = ' + '.join(str(i) for i in factors)
        print(f'{n} = {factors_str}')
    else:
        print(f'{n} is NOT perfect.')

# 1978 소수 찾기
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력
N = int(input())
num_list = list(map(int, input().split()))
result = 0

for num in num_list:
    cnt = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                cnt += 1
        
        if cnt == 0:
            result += 1
    
print(result)
