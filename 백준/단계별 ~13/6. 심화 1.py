# 2444
# 별 찍기
star_count = int(input())

for i in range(1, star_count):
    print(' '*(star_count-i)+'*'*(2*i-1))
    
for i in range(star_count, 0, -1):
    print(' '*(star_count-i)+'*'*(2*i-1))

# 1157
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램
word = input().lower()
unique_word = list(set(word))

cnt = []

for w in unique_word:
    count = word.count(w)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(unique_word[(cnt.index(max(cnt)))].upper())

# 2941 
# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력
word = input()
Croatia_alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for c in Croatia_alp:
    word = word.replace(c, '*')

print(len(word))
''' for문 
ljes=njak
ljes=njak
ljes=njak
ljes=njak
*es=njak
*es=*ak
*e**ak
*e**ak '''

# 1316
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
N = int(input())
group_word = N

for i in range(N) :
    word = input()
    for j in range(len(word)-1) :
        if word[j] == word[j+1] :
            continue
        elif word[j] in word[j+1:] :
            group_word -= 1
            break
print(group_word)


# 25206
# 20줄에 걸쳐 치훈이가 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분, 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합, 결과 3.284483
rating = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0}
total_credit = 0
result = 0

for _ in range(20):
    class_, credit, grade = input().split()
    credit = float(credit)
    if grade != 'P':
        total_credit += credit
        result += credit*rating[grade]

print(f'{(result/total_credit):.6f}')
# print('%.6f'%(result/total_credit))
'''
%d	10진수
%o	8진수
%x	16진수
%f	실수(소수점이 붙은 수)
%c	단일 문자
%s	문자열

반올림
round(값, 반올림하려는 자리수)
'''