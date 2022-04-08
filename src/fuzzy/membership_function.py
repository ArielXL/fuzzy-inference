
class MembershipFunction:

    class Triangle:
        def __init__(self, a, b, c, min, max):
            self.a = a
            self.b = b
            self.c = c
            self.min = min
            self.max = max

        def get_interval(self):
            return [self.min, self.max]

        def __call__(self, x):
            if x < self.min or x > self.max:
                raise Exception('Argumento fuera del dominio.')
            elif x <= self.a or x >= self.c:
                return 0
            elif self.a <= x <= self.b:
                return (x - self.a) / (self.b - self.a)
            elif self.b <= x <= self.c:
                return (self.c - x) / (self.c - self.b)

    class Trapesoid:
        def __init__(self, a, b, c, d, min, max):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.min = min
            self.max = max

        def get_interval(self):
            return [self.min, self.max]

        def __call__(self, x):
            if x < self.min or x > self.max:
                raise Exception('Argumento fuera del dominio.')
            elif x <= self.a or x >= self.d:
                return 0
            elif self.a <= x <= self.b:
                return (x - self.a) / (self.b - self.a)
            elif self.b <= x <= self.c:
                return 1
            elif self.c <= x <= self.d:
                return (self.d - x) / (self.d - self.c)

    class Gausiana:
        def __init__(self, width, center, min, max):
            self.width = width
            self.center = center
            self.min = min
            self.max = max

        def get_interval(self):
            return [self.min, self.max]

        def __call__(self, x):
            if x < self.min or x > self.max:
                raise Exception('Argumento fuera del dominio.')
            else:
                return exp(-0.5 * ((x - self.center) / self.width) ** 2)

    class Bell:
        def __init__(self, width, m, center, min, max):
            self.width = width
            self.m = m
            self.center = center
            self.min = min
            self.max = max

        def get_interval(self):
            return [self.min, self.max]

        def __call__(self, x):
            if x < self.min or x > self.max:
                raise Exception('Argumento fuera del dominio.')
            else:
                return 1 / (1 + abs((x - self.center) / self.width) ** (2 * self.m))

    class Sigmoid:
        def __init__(self, m, center, min, max):
            self.m = m
            self.center = center
            self.min = min
            self.max = max

        def get_interval(self):
            return [self.min, self.max]

        def __call__(self, x):
            if x < self.min or x > self.max:
                raise Exception('Argumento fuera del dominio.')
            else:
                return 1 / (1 + exp(-self.m * (x - self.center)))

    class Singleton:
        def __init__(self, a, min, max):
            self.a = a
            self.min = min
            self.max = max
        
        def get_interval(self):
            return [self.min, self.max]
        
        def __call__(self, x):
            if x < self.min or x > self.max:
                raise Exception('Argumento fuera del dominio.')
            elif x == self.a:
                return 0
            else:
                return 1

