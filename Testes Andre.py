def Travel_Distance(dist_to_beg, dist_beg_end, n_steps_to_end):
    dist_to_end=dist_beg_end+dist_to_beg
    worth=True
    if dist_to_end>n_steps_to_end:
        worth=False

    return worth