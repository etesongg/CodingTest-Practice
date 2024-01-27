# 2750 수 정렬하기
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램, 결과를 한 줄에 하나씩 출력
N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

for num in nums:
    print(num)

# 2751 수 정렬하기 2(시간 초과 -> sys.stdin.readline() 사용)
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. <- 이 조건때문에 input()을 사용하면 시간 초과 됨(3. 반복문 15552) 
import sys

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

nums.sort()
for num in nums:
    print(num)

# 10989 수 정렬하기 3(메모리 초과 -> 계수 정렬 사용)
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬 
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수
import sys
input = sys.stdin.readline

N = int(input())
num_list = [0] * (10000 + 1)

for _ in range(N):
    num_list[int(input())] += 1

for i in range(len(num_list)):
    if num_list[i] != 0:
        for _ in range(num_list[i]):
            print(i)
'''
계수정렬
카운트 할 배열을 선언하고, 정렬할 배열 요소가 몇개가 있는지 카운트 배열 각 인덱스에 담는다데이터의 크기가 한정되어  빠르게 동작해야할 때 사용된다.
즉 계수정렬은 데이터의 크기가 한정되었을 때문 사용, 매우 빠름
'''

# 1427 소트인사이드
# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬
N = input()

num_list = [N[i] for i in range(len(N))]
num_list.sort(reverse=True)

print(''.join(num_list))

# 11650 좌표 정렬하기
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
N = int(input())
xy_list = []

for _ in range(N):
    [x, y] = map(int, input().split())
    xy_list.append([x, y])

xy_list.sort()
for xy in xy_list:
    print(xy[0], xy[1])


