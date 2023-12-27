class ArithmeticProgression:

    def __init__(self, a, d):
        self.a = a
        self.d = d

    def nth_term(self, n):

        if n < 1:
            raise ValueError("Номер члена повинен бути не менше 1")

        return self.a + (n - 1) * self.d
