# 1085 직사각형에서 탈출
# 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램
x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))

# 3009 네 번째 점
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램(x, y 의 갯수를 세고 한개만 있는 좌표가 네번째 점)
x_nums = []
y_nums = []

for _ in range(3):
    x, y = map(int, input().split())
    x_nums.append(x)
    y_nums.append(y)

for i in range(3):
  if x_nums.count(x_nums[i]) == 1:
    x = x_nums[i]
  if y_nums.count(y_nums[i]) == 1:
    y = y_nums[i]

print(x, y)

# 10101 삼각형 외우기
# 세 각의 크기가 모두 60이면, Equilateral, 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles, 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene, 세 각의 합이 180이 아닌 경우에는 Error
angle = [int(input()) for _ in range(3)]

if angle.count(60) == 3:
    print('Equilateral')
elif sum(angle) == 180 and len(set(angle)) == 2:
    print('Isosceles')
elif sum(angle) == 180 and len(set(angle)) == 3:
    print('Scalene')
else:
    print('Error')

# 5073 삼각형과 세 변
# 삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의한다. Equilateral :  세 변의 길이가 모두 같은 경우, Isosceles : 두 변의 길이만 같은 경우, Scalene : 세 변의 길이가 모두 다른 경우, 단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우(6,3,2)에는 "Invalid" 를 출력
while 1:
    side = list(map(int, input().split()))

    if side.count(0) == 3:
        break
    elif max(side) >= sum(side)-max(side):
        print('Invalid')
    elif len(set(side)) == 1:
        print('Equilateral')
    elif len(set(side)) == 2:
        print('Isosceles')
    elif len(set(side)) == 3:
        print('Scalene')

# 14215 세 막대
# 길이가 a, b, c인 세 막대를 가지고 있고, 각 막대의 길이를 마음대로 줄일 수 있다. 영선이는 세 막대를 이용해서 아래 조건을 만족하는 삼각형을 만들려고 한다. 1. 각 막대의 길이는 양의 정수이다. 2. 세 막대를 이용해서 넓이가 양수인 삼각형을 만들 수 있어야 한다. 3. 삼각형의 둘레를 최대로 해야 한다. a, b, c가 주어졌을 때, 만들 수 있는 가장 큰 둘레를 구하는 프로그램
ls = sorted(list(map(int, input().split())))

if ls[0] + ls[1] > ls[2]:
    print(sum(ls))
else:
    print((ls[0] + ls[1]) * 2 - 1)