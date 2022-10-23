lst = []

lst = list(map(int, input('Enter digits - interval: ').split()))

def summaOdd(lst):
    # countSum = 0
    #
    # for i in range(len(lst)):
    #     if i%2 != 0:
    #         countSum+=lst[i]
    #
    countSum = sum([lst[x] for x in range(1, len(lst), 2)])

    print(countSum)

summaOdd(lst)