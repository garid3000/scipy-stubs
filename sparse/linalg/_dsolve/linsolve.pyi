"""
This type stub file was generated by pyright.
"""

from scipy._typing import Untyped

__all__ = ["MatrixRankWarning", "factorized", "spilu", "splu", "spsolve", "spsolve_triangular", "use_solver"]
class MatrixRankWarning(UserWarning):
    ...


def use_solver(**kwargs):
    ...

def spsolve(A, b, permc_spec: Untyped | None = ..., use_umfpack: bool = ...) -> Untyped:
    ...

def splu(A, permc_spec: Untyped | None = ..., diag_pivot_thresh: Untyped | None = ..., relax: Untyped | None = ..., panel_size: Untyped | None = ..., options: Untyped | None = ...) -> Untyped:
    ...

def spilu(A, drop_tol: Untyped | None = ..., fill_factor: Untyped | None = ..., drop_rule: Untyped | None = ..., permc_spec: Untyped | None = ..., diag_pivot_thresh: Untyped | None = ..., relax: Untyped | None = ..., panel_size: Untyped | None = ..., options: Untyped | None = ...) -> Untyped:
    ...

def factorized(A) -> Untyped:
    ...

def spsolve_triangular(A, b, lower: bool = ..., overwrite_A: bool = ..., overwrite_b: bool = ..., unit_diagonal: bool = ...) -> Untyped:
    ...

