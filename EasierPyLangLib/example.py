# Example usage of EasierPyLangLib
# This file demonstrates the functions in the formulas module.
from EasierPyLangLib import formulas as fm

# Example values
x = 42
w = 80.0  # 80kg
h = 1.8  # 1.8m / 180cm

# Fibonacci number example
print(fm.fib(x))

# BMI calculation example
print(fm.BMI(w, h))

# Additional helper functions
print(fm.factorial(5))      # 5! = 120
print(fm.average(1, 2, 3, 4, 5))  # average = 3.0
print(fm.gcd(36, 48))       # greatest common divisor = 12
print(fm.clamp(999, 0, 10)) # clamp to 10

print(pi, e)
