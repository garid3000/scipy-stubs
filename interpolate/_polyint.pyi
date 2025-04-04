"""
This type stub file was generated by pyright.
"""

from scipy._typing import Untyped

class _Interpolator1D:
    dtype: Untyped
    def __init__(self, xi: Untyped | None = ..., yi: Untyped | None = ..., axis: Untyped | None = ...) -> None:
        ...
    
    def __call__(self, x) -> Untyped:
        ...
    


class _Interpolator1DWithDerivatives(_Interpolator1D):
    def derivatives(self, x, der: Untyped | None = ...) -> Untyped:
        ...
    
    def derivative(self, x, der: int = ...) -> Untyped:
        ...
    


class KroghInterpolator(_Interpolator1DWithDerivatives):
    xi: Untyped
    yi: Untyped
    c: Untyped
    def __init__(self, xi, yi, axis: int = ...) -> None:
        ...
    


def krogh_interpolate(xi, yi, x, der: int = ..., axis: int = ...) -> Untyped:
    ...

def approximate_taylor_polynomial(f, x, degree, scale, order: Untyped | None = ...) -> Untyped:
    ...

class BarycentricInterpolator(_Interpolator1DWithDerivatives):
    xi: Untyped
    n: Untyped
    wi: Untyped
    def __init__(self, xi, yi: Untyped | None = ..., axis: int = ..., *, wi: Untyped | None = ..., random_state: Untyped | None = ...) -> None:
        ...
    
    yi: Untyped
    def set_yi(self, yi, axis: Untyped | None = ...):
        ...
    
    def add_xi(self, xi, yi: Untyped | None = ...):
        ...
    
    def __call__(self, x) -> Untyped:
        ...
    
    def derivative(self, x, der: int = ...) -> Untyped:
        ...
    


def barycentric_interpolate(xi, yi, x, axis: int = ..., *, der: int = ...) -> Untyped:
    ...

