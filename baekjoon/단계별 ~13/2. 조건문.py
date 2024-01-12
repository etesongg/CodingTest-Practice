# 2884
# 45분 일찍 알람 설정하기
h, m = map(int, input().split())

if m >=45:
    print(f'{h} {m-45}')
elif m < 45 and 0<h<24:
    print(f'{h-1} {60-(45-m)}')
elif m < 45 and h == 0:
    print(f'{23} {60-(45-m)}')

# 2525
# 오븐 시계
h, m = map(int, input().split())
c = int(input())

h += c//60
m = c%60

if h >= 24:
    h = h%24
    print(f'{h} {m}')
else:
    print(f'{h} {m}') 