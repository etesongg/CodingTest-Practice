'''
문제 설명
문자열 code가 주어집니다.
code를 앞에서부터 읽으면서 만약 문자가 "1"이면 mode를 바꿉니다. mode에 따라 code를 읽어가면서 문자열 ret을 만들어냅니다.

mode는 0과 1이 있으며, idx를 0 부터 code의 길이 - 1 까지 1씩 키워나가면서 code[idx]의 값에 따라 다음과 같이 행동합니다.

mode가 0일 때
code[idx]가 "1"이 아니면 idx가 짝수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
code[idx]가 "1"이면 mode를 0에서 1로 바꿉니다.
mode가 1일 때
code[idx]가 "1"이 아니면 idx가 홀수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
code[idx]가 "1"이면 mode를 1에서 0으로 바꿉니다.
문자열 code를 통해 만들어진 문자열 ret를 return 하는 solution 함수를 완성해 주세요.

단, 시작할 때 mode는 0이며, return 하려는 ret가 만약 빈 문자열이라면 대신 "EMPTY"를 return 합니다.


입출력 예
code	result
"abc1abc1abc"	"acbac"
'''

def solution(code):
    mode = 0
    ret = ''
    for idx, val in enumerate(code):
        if mode == 0:
            if val != "1":
                if idx%2 == 0:
                    ret += val
            else:
                mode = 1
        else:
            if val != "1":
                if idx%2 == 1:
                    ret += val
            else:
                mode = 0
                    
    answer = ret if ret else "EMPTY"
    return answer


# 다른 사람 풀이 
def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"


def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if code[i] == '1':
            mode ^= 1
        else:
            if i % 2 == mode:
                answer += code[i]

    return answer if answer else 'EMPTY'
'''
풀이
^= 는 비트연산자 중에 xor을 뜻 함
두 비트가 서로 같으면 0 다르면 1
따라서 mode가 0이면 결과는 1이되고, 1이면 같기때문에 0이됨

answer if answer else 'EMPTY'는 answer가 빈문자열이 아니면 answer를 리턴
빈문자열이면 'EMPTY'를 리턴 
if 뒤에 조건이 참이면 if 앞에걸 반환하고, 거짓이면 else 뒤에걸 반환
'''

'''
enumerate(iterable, startIndex) 함수 설명
- Iterable : 반복할 수 있는 개체
- StartIndex : (선택 사항) 개수는 루프의 첫 번째 항목에 대해 startIndex에 제공된 값으로 시작하고 루프의 끝에 도달할 때까지 다음 항목에 대해 증가, 지정하지 않으면 카운트는 0부터 시작

ex) for i in enumerate(code, 10):
10, 'a'
11, 'b'
12, 'c'
'''