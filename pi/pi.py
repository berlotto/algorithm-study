from decimal import Decimal

"""Calculando PI pela formula de Leibniz

pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...
"""


def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0

    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2
        operation *= -1.0

    return pi



def calculate_pi_decimal(n_terms: int) -> Decimal:
    numerator: Decimal = Decimal(4.0)
    denominator: Decimal = Decimal(1.0)
    operation: Decimal = Decimal(1.0)
    pi: Decimal = Decimal(0.0)

    dois = Decimal(2)
    mum = Decimal(-1.0)

    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += dois
        operation *= mum

    return pi

print(calculate_pi(10000000))
print(calculate_pi_decimal(10000000))