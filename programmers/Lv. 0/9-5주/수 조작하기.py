'''
문제 설명
정수 n과 문자열 control이 주어집니다. control은 "w", "a", "s", "d"의 4개의 문자로 이루어져 있으며, control의 앞에서부터 순서대로 문자에 따라 n의 값을 바꿉니다.

"w" : n이 1 커집니다.
"s" : n이 1 작아집니다.
"d" : n이 10 커집니다.
"a" : n이 10 작아집니다.
위 규칙에 따라 n을 바꿨을 때 가장 마지막에 나오는 n의 값을 return 하는 solution 함수를 완성해 주세요.

입출력 예
n	control	result
0	"wsdawsdassw"	-1
'''

def solution(n, control):
    for i in control:
        if i == "w":
            n += 1
        elif i == "s":
            n -= 1
        elif i == "d":
            n += 10
        else:
            n -= 10

    return n


# 다른 사람 풀이
def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])

'''
dict(zip()) 함수 설명
- 딕셔너리
>>> d = {'a' : 1, 'b': 2, 'c': 3}
>>> d
{'a': 1, 'b': 2, 'c': 3}

- dict()
>>> d = dict([('a', 1), ('b', 2), ('c', 3)])
>>> d
{'a': 1, 'b': 2, 'c': 3}

키가 문자열인 경우
>>> d = dict(a=1, b=2, c=3)
>>> d
{'a': 1, 'b': 2, 'c': 3}

- zip()
>>> z = zip(['a', 'b', 'c'], [1, 2, 3]) 두 개의 리스트, 튜플zip(('a', 'b', 'c'), (1, 2, 3))을 이용하여 key와 value를 구성
>>> for i in z:
	print(i, end=' ')
('a', 1) ('b', 2) ('c', 3) 

- dict(zip())
>>> d = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
>>> d
{'a': 1, 'b': 2, 'c': 3}
'''
