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
    x, y = map(int, input().split())
    xy_list.append([x, y])

xy_list.sort()
for xy in xy_list:
    print(xy[0], xy[1])

# 11651 좌표 정렬하기 2
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
N = int(input())
xy_list = []

for _ in range(N):
    x, y = map(int, input().split())
    xy_list.append([y, x])

xy_list.sort()
for xy in xy_list:
    print(xy[1], xy[0])

# 1181 단어 정렬
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오. 길이가 짧은 것부터, 길이가 같으면 사전 순으로 단, 중복된 단어는 하나만 남기고 제거해야 한다.
N = int(input()) # input() 대신 sys.stdin.readline()
str_li = [input() for _ in range(N)] # for문 안에 sys.stdin.readline()을 사용하면 출력형식이 잘못되었다고 나옴 후자는 개행문자 포함해서 저장하기 때문 "abc\n" 그러므로 sys.stdin.readline().strip()처리 해줘야 함

set_li = set(str_li)    #
str_li = list(set_li)   # str_li = sorted(list(set(str_li))) 로 한 줄로 적기
str_li.sort()           # 
str_li.sort(key = len)

for i in str_li:
    print(i)

# 10814 나이순 정렬
# 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬
import sys
input = sys.stdin.readline

N = int(input())
mem_li = []
for _ in range(N):
    age, name = map(str, input().split())
    age = int(age)
    mem_li.append([age, name])

mem_li.sort(key = lambda x : x[0]) # 첫 번째 인자를 기준으로 오름차순(내림차순은 - 붙이기)
for i in mem_li:
    print(i[0], i[1])

# 18870 좌표 압축
# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다. Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다. X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split())) # li = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

li2 = sorted(list(set(li))) # [1, 2, 3, 4, 5, 6, 9]
dic = {li2[i] : i for i in range(len(li2))} # {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 9: 6}
for i in li:
    print(dic[i], end=' ') # dic[3] = 2