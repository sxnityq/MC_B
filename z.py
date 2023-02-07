def str_to_int(limit : str):
    res = 0
    for pointer, chr in enumerate(limit[::-1], 0):
        if not chr.isdigit():
            return 9
        res += int(chr) * 10**pointer
    return res 