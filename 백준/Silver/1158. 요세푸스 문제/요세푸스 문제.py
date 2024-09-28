import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())

arr = [i for i in range(1, N+1)]
josephus = []
removeI = 0

while len(arr) > 0:
    removeI += K - 1
    if removeI >= len(arr):
        removeI %= len(arr)
    josephus.append(str(arr[removeI]))
    arr.pop(removeI)

print('<',', '.join(josephus),'>', sep='')
    