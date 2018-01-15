import hashlib


def lowest_decimal(key, part):
    zeroes = "00000" if part == 1 else "000000"
    pos = 5 if part == 1 else 6

    m, i = hashlib.md5(), 0
    m.update(key+str(i))
    while m.hexdigest()[:pos] != zeroes:
        m = hashlib.md5()
        i += 1
        m.update(key+str(i))

    print i, m.hexdigest()

lowest_decimal("ckczppom", 1)
lowest_decimal("ckczppom", 2)