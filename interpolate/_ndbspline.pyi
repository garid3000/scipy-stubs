"""
This type stub file was generated by pyright.
"""

from scipy._typing import Untyped

class NdBSpline:
    k: Untyped
    t: Untyped
    c: Untyped
    extrapolate: Untyped
    def __init__(self, t, c, k, *, extrapolate: Untyped | None = ...) -> None:
        ...
    
    def __call__(self, xi, *, nu: Untyped | None = ..., extrapolate: Untyped | None = ...) -> Untyped:
        ...
    
    @classmethod
    def design_matrix(cls, xvals, t, k, extrapolate: bool = ...) -> Untyped:
        ...
    


def make_ndbspl(points, values, k: int = ..., *, solver=..., **solver_args) -> Untyped:
    ...

