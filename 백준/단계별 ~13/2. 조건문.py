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
taken_m = int(input())

taken_m += m
res_h = (h + (taken_m//60))%24
res_m = taken_m%60
print(res_h,res_m)