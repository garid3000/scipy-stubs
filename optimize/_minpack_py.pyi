"""
This type stub file was generated by pyright.
"""
from typing import Callable
from numpy.typing import NDArray
import numpy as np
from scipy._typing import Untyped

__all__ = ["curve_fit", "fixed_point", "fsolve", "leastsq"]
def fsolve(func, x0, args=..., fprime: Untyped | None = ..., full_output: int = ..., col_deriv: int = ..., xtol: float = ..., maxfev: int = ..., band: Untyped | None = ..., epsfcn: Untyped | None = ..., factor: int = ..., diag: Untyped | None = ...) -> Untyped:
    ...

def leastsq(func, x0, args=..., Dfun: Untyped | None = ..., full_output: bool = ..., col_deriv: bool = ..., ftol: float = ..., xtol: float = ..., gtol: float = ..., maxfev: int = ..., epsfcn: Untyped | None = ..., factor: int = ..., diag: Untyped | None = ...) -> Untyped:
    ...

def curve_fit(f: Callable[[NDArray[np.float64], float,float,float], NDArray[np.float64]],
              xdata:NDArray[np.float64],
              ydata:NDArray[np.float64],
              p0: NDArray[np.float64] |list[float|int] | None = ...,
              sigma: NDArray[np.float64] | None = ...,
              absolute_sigma: bool = ...,
              check_finite: bool | None = ...,
              bounds:tuple[tuple[float, float, float]|NDArray[np.float64]|list[float|int],tuple[float, float, float]|NDArray[np.float64]|list[float|int]] = ...,
              method: str | None = ...,
              jac: Callable[[NDArray[np.float64]],NDArray[np.float64]] |str | None = ..., *,
              full_output: bool = ...,
              nan_policy: str | None = ...,
              **kwargs:str|bool|float|None
              ) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    ...

def check_gradient(fcn, Dfcn, x0, args=..., col_deriv: int = ...) -> Untyped:
    ...

def fixed_point(func, x0, args=..., xtol: float = ..., maxiter: int = ..., method: str = ...) -> Untyped:
    ...

