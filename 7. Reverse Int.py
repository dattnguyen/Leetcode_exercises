def reverse(x):
    rnum = 0
    if x >= 2 ** 31 - 1 or x <= -2 ** 31:
        return 0

    else:
        if x < 0:
            x = 0 - x
            while x != 0:
                rnum = rnum * 10 + x % 10
                x = int(x / 10)
            return print((0 - rnum))

        else:
            while x != 0:
                rnum = rnum * 10 + x % 10
                x = int(x / 10)
            return print((rnum))

reverse(1256)
