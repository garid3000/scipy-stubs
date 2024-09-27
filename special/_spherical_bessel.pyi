"""
This type stub file was generated by pyright.
"""

import numpy as np
import numpy.typing as npt
from typing import TypeAlias
from numpy._typing import _ArrayLikeComplex_co, _ArrayLikeInt_co

_Scalar_fc: TypeAlias = np.float64 | np.complex128
def spherical_jn(n: _ArrayLikeInt_co, z: _ArrayLikeComplex_co, derivative: bool = ...) -> _Scalar_fc | npt.NDArray[_Scalar_fc]:
    ...

def spherical_yn(n: _ArrayLikeInt_co, z: _ArrayLikeComplex_co, derivative: bool = ...) -> _Scalar_fc | npt.NDArray[_Scalar_fc]:
    ...

def spherical_in(n: _ArrayLikeInt_co, z: _ArrayLikeComplex_co, derivative: bool = ...) -> _Scalar_fc | npt.NDArray[_Scalar_fc]:
    ...

def spherical_kn(n: _ArrayLikeInt_co, z: _ArrayLikeComplex_co, derivative: bool = ...) -> _Scalar_fc | npt.NDArray[_Scalar_fc]:
    ...

