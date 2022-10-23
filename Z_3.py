from functools import reduce

num = int(input('number N = '))

count = 1

#способ нахождения факториала N! = 1*2..n
# for i in range(1, num+1):
#     count *= i

count = reduce((lambda prev, y:
                [prev[0] * y[0], prev[1] + [y[0]]]),
               [[i, [i]] for i in range(1, num+1)])

print(count[0])
print(count[1])