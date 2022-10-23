def endOfLoop():
    raise StopIteration

def numPi(form=1.0e-5):
    num = 0
    # d = 1
    # two = 1
    # while True:
    #     i = 4 / d
    #     num += two * i
    #
    #     if i<form:
    #         return num
    #
    #     two = -two
    #     d += 2

    # for i in range(100000):
    #     if (v < form):
    #         break
    #     num += (1 if (i % 2 == 0) else -1) * v

    a = [endOfLoop() if (4 / (1 + i*2) < form) else 4 / (1 + i*2) for i in range(100000)]
    num = sum([a[i] * (1 if (i % 2 == 0) else -1) for i in range(len(a))])
    return num

print(f'the numbers PI is equal to {round(numPi(),4)}')