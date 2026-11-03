# EasierPyLangLib

`EasierPyLangLib` is a lightweight Python utility library designed to make common calculations and small programming tasks easier.

## Package layout

- `__init__.py` — package entry point and exports
- `formulas.py` — core mathematical and utility functions
- `example.py` — example usage script

## Included functions

### `fib(x)`
Returns the `x`-th Fibonacci number.

```python
from EasierPyLangLib import formulas as fm

print(fm.fib(10))  # 55
```

### `BMI(w, h)`
Calculates the Body Mass Index (BMI).

```python
from EasierPyLangLib import formulas as fm

print(fm.BMI(80, 1.8))
```

### `factorial(n)`
Calculates the factorial of a non-negative integer.

```python
from EasierPyLangLib import formulas as fm

print(fm.factorial(5))  # 120
```

### `average(*values)`
Returns the arithmetic mean of the given numbers.

```python
from EasierPyLangLib import formulas as fm

print(fm.average(1, 2, 3, 4, 5))  # 3.0
```

### `is_even(value)`
Checks whether an integer is even.

```python
from EasierPyLangLib import formulas as fm

print(fm.is_even(10))  # True
```

### `gcd(a, b)`
Computes the greatest common divisor (GCD) of two integers.

```python
from EasierPyLangLib import formulas as fm

print(fm.gcd(36, 48))  # 12
```

### `clamp(value, minimum, maximum)`
Clamps a number to a specified lower and upper bound.

```python
from EasierPyLangLib import formulas as fm

print(fm.clamp(999, 0, 10))  # 10
```

## Example usage

```python
from EasierPyLangLib import formulas as fm

print(fm.fib(12))
print(fm.BMI(70, 1.75))
print(fm.factorial(6))
print(fm.gcd(84, 30))
print(fm.clamp(42, 0, 20))
```

## Notes

This library is intended to be:

- easy to read
- beginner-friendly
- useful for teaching and small projects
- a collection of common math and utility helpers

If you want, this library can also be expanded with additional helpers such as percentage calculation, distance formulas, or simple validation tools.
