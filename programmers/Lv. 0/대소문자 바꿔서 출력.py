'''
문제 설명
영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.
'''


str = input()
sentence =''
for i in str:
    if i.isupper()==True:
        sentence +=i.lower()
    else:
        sentence +=i.upper()

# 다른 사람 풀이
str = input().swapcase()

# 관련 함수
str = str.upper() # upper() : 문자열을 대문자로 변환하기
str = str.lower() # lower() : 문자열을 소문자로 변환하기
str = str.capitalize() # capitalize() : 문자열을 첫 글자는 대문자로 만들고 나머지는 소문자로 변환하기
str = str.title() # title() : 문자열의 각 단어의 첫글자를 대문자로 변환하기
str = str.swapcase() # swapcase() : 문자열에 있는 모든 문자의 대/소문자를 반대로 변환하기
# isupper(), islower() 을 이용하면. 이 문자가 모두 대문자인지 모두 소문자인지 확인하여 Boolean 형태로 나타내 준다.


