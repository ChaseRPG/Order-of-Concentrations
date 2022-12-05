class Sub:
    def __init__(self, name, s1, s2):
        self.name = name
        self.s1 = s1
        self.s2 = s2

    print('To use scientific notation, use e. | EX. 1.25e-2')
    rate1 = float(input('Initial rate of experiment 1: ')) * 10000000
    rate2 = float(input('Initial rate of experiment 2: ')) * 10000000

    def order(self):
        result = int(Sub.rate1 * (self.s2 / self.s1))  # calculations for multiple
        result2 = int(Sub.rate1 * ((self.s2 / self.s1) * (self.s2 / self.s1)))  # for second order

        if result in range(int(Sub.rate2) - 1000000, int(Sub.rate2) + 1000000):
            print(self.name + 'is First Order')
        elif result2 in range(int(Sub.rate2) - 1000000, int(Sub.rate2) + 1000000):
            print(self.name + 'is second order')
        else:
            print('ya messed up chief')


a = Sub('[a]', float(input('A1: ')) * 10000000, float(input('A2: ')) * 10000000)
b = Sub('[b]', float(input('B1: ')) * 10000000, float(input('B2: ')) * 10000000)

if not a.s1 == a.s2 or not b.s1 == b.s2:
    if Sub.rate1 == Sub.rate2:
        print('Zero Order')
        exit(0)

if a.s1 == a.s2:
    Sub.order(b)

if b.s1 == b.s2:
    Sub.order(a)
