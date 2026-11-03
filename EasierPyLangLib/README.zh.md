# EasierPyLangLib

`EasierPyLangLib` 是一个轻量级 Python 工具库，目标是让常见的计算和小工具调用更简单。

## 目录结构

- `__init__.py`：包入口，导出可用模块
- `formulas.py`：包含基础数学与实用函数
- `example.py`：展示如何使用这些函数的示例脚本

## 当前包含的函数

### `fib(x)`
计算 Fibonacci 数列中的第 `x` 项。

```python
from EasierPyLangLib import formulas as fm

print(fm.fib(10))  # 55
```

### `BMI(w, h)`
计算 BMI（身体质量指数）。

```python
from EasierPyLangLib import formulas as fm

print(fm.BMI(80, 1.8))
```

### `factorial(n)`
计算非负整数的阶乘。

```python
from EasierPyLangLib import formulas as fm

print(fm.factorial(5))  # 120
```

### `average(*values)`
计算多个数的平均值。

```python
from EasierPyLangLib import formulas as fm

print(fm.average(1, 2, 3, 4, 5))  # 3.0
```

### `is_even(value)`
判断整数是否为偶数。

```python
from EasierPyLangLib import formulas as fm

print(fm.is_even(10))  # True
```

### `gcd(a, b)`
计算两个整数的最大公约数（GCD）。

```python
from EasierPyLangLib import formulas as fm

print(fm.gcd(36, 48))  # 12
```

### `clamp(value, minimum, maximum)`
将一个数限制在指定区间内。

```python
from EasierPyLangLib import formulas as fm

print(fm.clamp(999, 0, 10))  # 10
```

## 使用方式

```python
from EasierPyLangLib import formulas as fm

print(fm.fib(12))
print(fm.BMI(70, 1.75))
print(fm.factorial(6))
print(fm.gcd(84, 30))
print(fm.clamp(42, 0, 20))
```

## 说明

这个库的设计目标是：

- 简单易学
- 适合教学和小项目
- 提供常见数学与实用函数

如果你需要的，这个库会对你非常很有帮助的！
