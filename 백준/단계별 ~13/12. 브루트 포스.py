# 2798 블랙잭
# 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다. N장의 카드 중에서 3장의 카드를 골라 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력
N, M = map(int, input().split())
cards = list(map(int, input().split()))
res = []
             
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
             three_cards = cards[i] + cards[j] + cards[k]
             if three_cards > M:
                 continue
             else:
                 res.append(three_cards)

print(max(res))
'''
다른 풀이
순열 : 순서를 고려하여 뽑는 경우의 수

permutations(iterable객체, r개)
iterable 객체 : 반복문, 리스트 등 반복 가능한 객체
r개 : 해당 객체에서 중복을 허용하지 않고 뽑을 개수(생략 가능)
순서대로 뽑는다. -> ['AB', 'AC', 'BA', 'BC', 'CA', 'CB']

from itertools import permutations

N, M = map(int, input().split())
cards = list(map(int, input().split()))
res = []
             
for three_cards in permutations(cards, 3):
    if sum(three_cards) > M:
        continue
    else:
        res.append(sum(three_cards))

print(max(res))

조합 : 순서를 생각하지 않고 뽑는 경우의 수

combinations(iterable객체, r개)
iterable 객체 : 반복문, 리스트 등 반복 가능한 객체
r개 : 해당 객체에서 중복을 허용하지 않고 뽑을 개수(생략 안됨)
뽑는 순서를 고려하지 않는다. -> (AB와 BA를 같은 것으로 본다.)

from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))
res = []
             
for three_cards in combinations(cards, 3):
    if sum(three_cards) > M:
        continue
    else:
        res.append(sum(three_cards))

print(max(res))
'''
# 
# 







# 
# 
