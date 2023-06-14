class rating:
    def __init__(self, a, m, b):
        self.a = a
        self.m = m
        self.b = b

    @property
    def calc(self):
        e = (self.a + 4 * self.m + self.b) / 6
        sd = (self.b - self.a) / 6
        ci_max = e + 2 * sd
        ci_min = e - 2 * sd

        return ci_min, ci_max


count_tasks = int(input('How many tasks you want calculate: '))

for i in range(0, count_tasks):
    a = int(input('Enter first number: '))
    m = int(input('Enter second number: '))
    b = int(input('Enter third number: '))

    obj = rating(a, m, b)

    print(f'Project\'s 95% confidence interval: {obj.calc} points\n')