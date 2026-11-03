# v0.1.2.0
from importlib import import_module

from .maths import e, pi

# Keep the package import path stable even though the implementation lives in the
# nested maths/formulas.py module.
formulas = import_module(".maths.formulas", __name__)

BMI, average, clamp, factorial, fib, gcd, is_even = (
    formulas.BMI,
    formulas.average,
    formulas.clamp,
    formulas.factorial,
    formulas.fib,
    formulas.gcd,
    formulas.is_even,
)

from . import maths

__version__ = "0.1.2.0"

__all__ = [
    "formulas",
    "maths",
    "BMI",
    "fib",
    "factorial",
    "average",
    "is_even",
    "gcd",
    "clamp",
    "__version__",
    "pi",
    "e",
]

# test run
if __name__ == "__main__":
    import EasierPyLangLib.example as example
