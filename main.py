a1 = float(input('A1: ')) * 10000
a2 = float(input('A2: ')) * 10000
b1 = float(input('B1: ')) * 10000
b2 = float(input('B2: ')) * 10000
rate1 = float(input('Initial rate of experiment 1: ')) * 10000
rate2 = float(input('Initial rate of experiment 2: ')) * 10000

# check to see if rates equal each other and no constant, if so zero order
if not a1 == a2 or not b1 == b2:
    if rate1 == rate2:
        print('Zero Order')
        exit(0)

if a1 == a2:                         # check to see if [A] is constant
    result = int(rate1 * (b2 / b1))      # calculations for multiple
    result2 = int(rate1 * ((b2 / b1) * (b2 / b1)))            # for second order

    if result in range(int(rate2) - 1000, int(rate2) + 1000):
        print('[B] is First Order')
    elif result2 in range(int(rate2) - 1000, int(rate2) + 1000):
        print('[B] is second order')
    else:
        print('ya messed up chief')

if b1 == b2:                         # check to see if [B] is constant
    result = float(rate1 * (a2 / a1))      # calculations for multiple
    result2 = float(rate1 * ((a2 / a1) * (a2 / a1)))            # for second order

    if result in range(int(rate2) - 1000, int(rate2) + 1000):
        print('[A] is First Order')
    elif result2 in range(int(rate2) - 1000, int(rate2) + 1000):
        print('[A] is second order')
    else:
        print('ya messed up chief')
