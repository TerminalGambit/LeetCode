def canChange(start: str, target: str) -> bool:
    if start.replace('_', '') != target.replace('_', ''):
        return False

    sl_pos = []
    sr_pos = []
    tl_pos = []
    tr_pos = []

    for i in range(len(start)):
        if start[i] == 'L':
            sl_pos.append(i)
        elif start[i] == 'R':
            sr_pos.append(i)
        if target[i] == 'L':
            tl_pos.append(i)
        elif target[i] == 'R':
            tr_pos.append(i)

    for s_pos, t_pos in zip(sl_pos,tl_pos):
        if s_pos < t_pos:
            return False

    for s_pos, t_pos in zip(sr_pos,tr_pos):
        if s_pos > t_pos:
            return False

    return True
