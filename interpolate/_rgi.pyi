"""
This type stub file was generated by pyright.
"""

from scipy._typing import Untyped

__all__ = ["RegularGridInterpolator", "interpn"]
class RegularGridInterpolator:
    method: Untyped
    bounds_error: Untyped
    values: Untyped
    fill_value: Untyped
    def __init__(self, points: Untyped, values: Untyped, method: str = ..., bounds_error: bool = ..., fill_value: Untyped = ..., *, solver: Untyped | None = ..., solver_args: Untyped | None = ...) -> None:
        ...
    
    def __call__(self, xi: Untyped, method: Untyped | None = ..., *, nu: Untyped | None = ...) -> Untyped:
        ...
    


def interpn(points: Untyped, values: Untyped, xi: Untyped, method: str = ..., bounds_error: bool = ..., fill_value: Untyped = ...) -> Untyped:
    ...

