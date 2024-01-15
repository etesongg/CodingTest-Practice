# 2745 진법 변환
# B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램, (2 ≤ B ≤ 36)
N, B = input().split()
B = int(B)

alphabet_list = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
formation_list = list(range(36))

result = 0

for idx, val in enumerate(N):
    num_idx = alphabet_list.index(val)
    result += (formation_list[num_idx]*(B**(len(N)-1-idx)))
    
print(result)

# 11005 진법 변환 2
# 10진법 수 N이 주어진다. 이 수를 B진법으로,  (2 ≤ B ≤ 36) N
N, B = map(int, input().split())
alphabet_list = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
formation_list = list(range(36))

result =''

while N >= B:
    idx = N%B
    alphabet_idx = formation_list.index(idx)
    result += alphabet_list[alphabet_idx]
    
    N = N//B

alphabet_idx = formation_list.index(N)
result += alphabet_list[alphabet_idx]

print(result[::-1])

# 2903 중앙 이동 알고리즘
N = int(input())
print((2**N+1)**2) # 한 변에 놓일 점의 개수를 구한 뒤 제곱


# 2292 벌집
# 입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력(1에서 N까지 가는 규칙성 생각하기)
N = int(input())

num, cnt = 1, 1
while N > num:
    num += 6*cnt
    cnt += 1
    
print(cnt)

# 1193 분수찾기
# 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자. X가 주어졌을 때, X번째 분수를 구하는 프로그램(규칙찾기)
N = int(input())
line = 1

while N > line:
    N -= line
    line += 1
    
if line % 2 == 0:
    a = N
    b= line - N + 1
else:
    a = line - N + 1
    b = N
    
print(f'{a}/{b}')

# 2869 달팽이는 올라가고 싶다
# 높이가 V미터, 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.
import math

A, B, V = map(int, input().split())

days = math.ceil((V - A) / (A - B)) + 1
print(days)