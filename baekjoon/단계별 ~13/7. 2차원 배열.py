# 2738 행렬 덧셈
# 첫째 줄에 행렬의 크기 N 과 M, 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. 행렬 A와 B를 더한 행렬을 출력
N, M = map(int, input().split())
A, B = [], []

for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)
    
for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)
    
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()

# 2566 최댓값
#  9×9 격자판, 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수
matrix = []

for row in range(9):
    row_values = list(map(int, input().split()))
    matrix.append(row_values)
    
max_val = {"num": matrix[0][0], "row": 1, "col": 1}

for row in range(9):
    for col in range(9):
        if matrix[row][col] > max_val["num"]:
            max_val["num"] = matrix[row][col]
            max_val["row"] = row + 1
            max_val["col"] = col + 1

print(max_val["num"])
print(max_val["row"], max_val["col"])
        
# 10798 세로읽기
# 한 줄의 단어는 글자들을 빈칸 없이 연속으로 나열해서 최대 15개의 글자, 세로로 읽을 때 해당 자리의 글자가 없으면, 읽지 않고 그 다음 글자를 계속 읽는다, 세로로 읽은 순서대로 글자들을 공백 없이 출력
black_board = [input() for row in range(5)]
    
vertical = []

for col in range(15):
    for row in range(5):
        if col < len(black_board[row]): # 해당자리에 글자가 있는지 확인
            vertical.append(black_board[row][col]) # 굳이 새로운 리스트에 담지말고 print(black_board[row][col], end='')

print(''.join(vertical))