"""
This type stub file was generated by pyright.
"""

import numpy as np
import numpy.typing as npt
from typing import TypeAlias

_Array_f: TypeAlias = npt.NDArray[np.float32 | np.float64]
_Array_fc: TypeAlias = npt.NDArray[np.float32 | np.float64 | np.complex64 | np.complex128]
def symiirorder1_ic(signal: _Array_fc, c0: float, z1: float, precision: float) -> _Array_fc:
    ...

def symiirorder2_ic_fwd(signal: _Array_f, r: float, omega: float, precision: float) -> _Array_f:
    ...

def symiirorder2_ic_bwd(signal: _Array_f, r: float, omega: float, precision: float) -> _Array_f:
    ...

def sepfir2d(input: _Array_fc, hrow: _Array_fc, hcol: _Array_fc) -> _Array_fc:
    ...

