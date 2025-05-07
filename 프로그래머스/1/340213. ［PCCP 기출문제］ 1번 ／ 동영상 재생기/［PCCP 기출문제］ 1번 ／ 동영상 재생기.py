def trans_sec(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def solution(video_len, pos, op_start, op_end, commands):
    video_len = trans_sec(video_len)
    pos = trans_sec(pos)
    op_start = trans_sec(op_start)
    op_end = trans_sec(op_end)
    
    if op_start <= pos <= op_end:
        pos = op_end
        
    for command in commands:
        if command == 'prev':
            pos = max(0, pos - 10)
        elif command == 'next':
            pos = min(video_len, pos + 10)
        
        if op_start <= pos <= op_end:
            pos = op_end
        
    mm = pos//60
    ss = pos%60
     
    return f'{mm:02d}:{ss:02d}'