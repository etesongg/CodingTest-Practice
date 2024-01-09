# 1000
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
a, b = map(int,input().split())
print(a+b)

# 2588
# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
# 1
num1 = int(input())
num2 = input()

a1 = int(num2[2]) * num1
a2 = int(num2[1]) * num1
a3 = int(num2[0]) * num1
print(a1, a2, a3, num1 * int(num2))

# 2
num1 = int(input())
num2 = int(input())

print(num1 * (num2%10))
print(num1 * ((num2%100)//10))
print(num1 * (num2//100))
print(num1 * num2)

# 3
num1 = int(input())
num2 = input() 

for i in range(len(num2), 0, -1):	
    print(num1 * int(num2[i-1]))

print(num1 * int(num2))

# 10171 (\, ' 등의 문자에 주의)
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")
\    /\
 )  ( ')
(  /  )
 \(__)|

# 10172 ( ", `, \ 등의 문자에 주의)
print("|\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\__|")
|\_/|
|q p|   /}
( 0 )"""\
|"^"`    |
||_/=\\__|