# 11654
# 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력
asc = input()
 
print (ord(asc))

# 10809
S = list(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    if i in S:
        print(S.index(i), end=' ')
    else:
        print(-1, end=' ')
# find() 이용
S = input()

for x in 'abcdefghijklmnopqrstuvwxyz':
    print(S.find(x), end = ' ') # 해당 문자가 문자열에 존재하지 않는다면 -1을 반환


# 5622 다이얼
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

alpha = list(input())		
result = 0

for i in alpha:
    for j in dial:
        if i in str(j):		
            num = dial.index(j) + 3		
            result += num
print(result)    