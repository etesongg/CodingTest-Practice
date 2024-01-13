# 10871
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력
n, x = map(int, input().split())
a_list = list(map(int, input().split()))

for i in a_list:
    if i < x:
        print(i, end=' ')

# 10813
# 바구니를 총 N개, 앞으로 M번 공을 바꾸려고 한다. 
N, M = map(int, input().split())
baskets = []
for n in range(1, N+1):
    baskets.append(n)

for _ in range(M):
    i, j = map(int, input().split())
    baskets[i-1], baskets[j-1] = baskets[j-1], baskets[i-1]
    
for b in baskets:
    print(b, end=' ')


# 5597
# 학생이 30명, 과제를 28명이 제출 그 중에서 제출 안 한 학생 2명의 출석번호
students = [n for n in range(1, 31)]

for _ in range(28):
    sub_student = int(input())
    students.remove(sub_student)
    
print(min(students))
print(max(students))

# 3052
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램
num = [int(input())%42 for _ in range(10)]

print(len(set(num)))

# 10811
# 바구니를 총 N개 가지고 있고 M번 바구니의 순서를 역순
N, M = map(int, input().split())
baskets = [n for n in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    baskets[i-1:j] = reversed(baskets[i-1:j]) # reversed는 뒤집어진 리스트의 값을 return/ reverse는 리스트를 뒤집는다. return 값 없음
    
for b in baskets:
    print(b, end=' ')