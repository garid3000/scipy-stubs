"""
This type stub file was generated by pyright.
"""

import numpy as np
import numpy.typing as npt
from typing import Literal
from scipy._typing import Untyped

__all__ = ["LinAlgError", "LinAlgWarning", "norm"]
class LinAlgWarning(RuntimeWarning):
    ...


def norm(a: npt.ArrayLike, ord: Literal["fro", "nuc", 0, 1, -1, 2, -2] | float | None = ..., axis: Untyped | None = ..., keepdims: bool = ..., check_finite: bool = ...) -> np.float64 | npt.NDArray[np.float64]:
    ...

