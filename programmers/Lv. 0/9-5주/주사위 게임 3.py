'''
문제 설명
1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

입출력 예
a	b	c	d	result
2	2	2	2	2222
4	1	4	4	1681
6	3	3	6	27
2	5	2	6	30
6	4	2	5	2
'''

# 처음에는 set을 통해서 풀고 싶었음 
# 하지만 어떤 숫자가 3개인지 2개인지 알 수 없음
def solution(a, b, c, d):
    dice_list = [a, b, c, d]
    score = 0
    dice_set = set(dice_list)
    length = len(dice_set)
    if length == 1:
        score = 1111*a
    elif length == 2:
        max_value = max(dice_set)
        min_value = min(dice_set)
        if dice_list.count(max_value) == 3:
            score = (10 * min_value + max_value)**2
        elif dice_list.count(max_value) == 2:
            score = (max_value + min_value) * abs(max_value - min_value)
    elif length == 3:
        unique_value = 0
        for value in dice_set:
            if dice_list.count(value) == 1:
                unique_value = value
        score = unique_value
    else:
        score = min(dice_list)
    return score

# 정렬로 풀기
def solution(a, b, c, d):
    dice_list = [a, b, c, d]
    dice_list.sort()
    score = 0
    
    if dice_list[0] == dice_list[3]:
        score = 1111*dice_list[0]
    elif dice_list[0] == dice_list[2]:
        score = (10 * dice_list[0] + dice_list[3])**2
    elif dice_list[1] == dice_list[3]:
        score = (10 * dice_list[1] + dice_list[0])**2
    elif dice_list[0] == dice_list[1] and dice_list[2] == dice_list[3]:
        score = (dice_list[0] + dice_list[2])*abs(dice_list[0] - dice_list[2])
    elif dice_list[0] == dice_list[1] and dice_list[2] != dice_list[3]:
        score = dice_list[2] * dice_list[3]
    elif dice_list[0] != dice_list[1] and dice_list[2] == dice_list[3]:
        score = dice_list[0] * dice_list[1]
    elif dice_list[1] == dice_list[2] and dice_list[0] != dice_list[3]:
        score = dice_list[0] * dice_list[3]
    else:
        score = dice_list[0]
        
    return score


# 다른 사람 풀이
def solution(a, b, c, d):
    l = [a,b,c,d]
    c = [l.count(x) for x in l]
    if max(c) == 4:
        return 1111*a
    elif max(c) == 3:
        return (10*l[c.index(3)]+l[c.index(1)])**2
    elif max(c) == 2:
        if min(c) == 1:
            return eval('*'.join([str(l[i]) for i, x in enumerate(c) if x == 1]))
        else:
            return (max(l) + min(l)) * abs(max(l) - min(l))
    else:
        return min(l)