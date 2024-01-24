'''
시간 복잡도(입력값의 변화에 따라 연산을 실행할때, 연산 횟수에 비해 시간이 얼마만큼 걸리는가?)

Big-O(빅-오) : 상한 점근(최악)
Big-Ω(빅-오메가) : 하한 점근(최선)
Big-θ(빅-세타) : 그 둘의 평균(중간)

가장 자주 사용되는 표기법은 빅오 표기법으로 최악의 경우를 고려하므로, 프로그램이 실행되는 과정에서 소요되는 최악의 시간까지 고려할 수 있기 때문이다.
"이정도 시간까지 걸릴 수 있다"를 고려해서 그에 맞는 대응을 해야한다.

Big-O 표기법의 종류
O(1) : 일정한 복잡도이며 입력값이 증가하더라도 시간이 늘어나지 않는다.(입력값의 크기와 관계없이 즉시 출력값을 얻어낼 수 있다)
O(n) : 선형 복잡도이며 입력값이 증가함에 따라 시간 또한 같은 비율로 증가한다. (입력값이 1증가할때마다 코드의 실행 시간이 2초씩 증가한다면 O(2n)이라고 표현할 수 있다. 하지만 입력값이 커지면 커질수록 계수의 의미가 퇴색되기 때문에 이 알고리즘 또한 O(n)라고 표기한다.)
O(log n) : 로그 복잡도라고 부르면 빅오표기법중 O(1) 다음으로 빠른 시간 복잡도를 가진다.
O(n^2) : 2차 복잡도이며 입력값이 증가함에 따라 시간이 n의 제곱수의 비율로 증가하는 것을 의미한다.
O(2^n) : 기하급수적 복잡도라고 부르며 빅오 표기법 중 가장 느린 시간 복잡도를 가진다. 
'''

# 24262 알고리즘 수업 - 알고리즘의 수행 시간 1(O(1))
'''
문제 설명
입력의 크기 n이 주어지면 MenOfPassion 알고리즘 수행 시간을 예제 출력과 같은 방식으로 출력해보자.

MenOfPassion 알고리즘은 다음과 같다.

MenOfPassion(A[], n) {
    i = ⌊n / 2⌋;
    return A[i]; # 코드1
}
첫째 줄에 코드1 의 수행 횟수를 출력
째 줄에 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 출력한다

답 설명
MenOfPassion 함수는 반복문도 없고 단순히 입력값을 받아서 배열의 Indexing 값을 출력하는 함수이므로 입력이 아무리 커져도 '딱 1번'만 코드를 실행합니다. 그래서 첫 줄에는 무조건 1을 출력해야 합니다.

또한, 입력과 무관한 시간 복잡도 함수는 O(1)로 표현하고 상수항이므로 차수는 0이 됩니다. 따라서 두 번째 줄에는 무조건 0을 출력해야 합니다.
'''
print(1)
print(0)

# 24263 (O(n))
'''
문제 설명
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        sum <- sum + A[i]; # 코드1
    return sum;
}
첫째 줄에 코드1 의 수행 횟수를 출력한다.

둘째 줄에 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 출력한다. 단, 다항식으로 나타낼 수 없거나 최고차항의 차수가 3보다 크면 4를 출력한다.

답 설명
위에 코드를 파이썬 코드로 변환하면
def MenOfPassion(A, n):
	answer = 0
    for i in range(n):
    	answer = answer + A[i]
    return answer
'''
n = int(input())

print(n)
print(1)

# 24265 O(n2)
'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}
이중 for 문이 사용되었기 때문에 시간 복잡도는 O(n^2)
등차수열 공식 n(n-1)/2
'''
n = int(input())
    
print(n*(n-1)//2)
print(2)
# -----------------------------
# 다른 방법
n = int(input())

res = 0
for i in range(1, n):
    res += i
print(res)
print(2)

# 24266 O(n^3)
'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            for k <- 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
3중 for문 O(n^3)
'''

# 24267 O(n^3)
'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}

문제풀이
nC3 
https://dev-mandos.tistory.com/124

(n=7이면 5!+4!+3!+2!+1!)
n = int(input())
cnt = n-2
sum = 0
for i in range(1,n-1):
sum += cnt*i
cnt -= 1
print(sum)
print(3)
'''
n = int(input())

print((n*(n-1)*(n-2))//6)
print(3)

# 24313 점근적 표기 1
# 알고리즘의 소요 시간을 나타내는 O-표기법(빅-오)을 다음과 같이 정의하자. O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다} 이 정의는 실제 O-표기법(https://en.wikipedia.org/wiki/Big_O_notation)과 다를 수 있다. 함수 f(n) = a1n + a0, 양의 정수 c, n0가 주어질 경우 O(n) 정의를 만족하는지 알아보자. 첫째 줄에 함수 f(n)을 나타내는 정수 a1, a0가 주어진다. (0 ≤ |ai| ≤ 100), 다음 줄에 양의 정수 c가 주어진다. (1 ≤ c ≤ 100), 다음 줄에 양의 정수 n0가 주어진다. (1 ≤ n0 ≤ 100)
a1, a0 = map(int, input().split())

c = int(input())
n0 = int(input())

# f(n) = a1*n + a0, g(n) = n
# 판별식 f(n) ≤ c × g(n)
# a1*n + a0 <= c*n
# (a1-c)*n0 + a0 <= 0
if (a1*n0 + a0) <= (c*n0) and a1 <= c: # a0 와 a1은 음수도 될 수 있기 때문에 a1 <= c 조건을 통해 보장 해주기
    print(1)
else:
    print(0)
# https://kevinitcoding.tistory.com/entry/%EB%B0%B1%EC%A4%80Python-24313%EB%B2%88-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%88%98%EC%97%85-%EC%A0%90%EA%B7%BC%EC%A0%81-%ED%91%9C%EA%B8%B0-1-%EB%AC%B8%EC%A0%9C