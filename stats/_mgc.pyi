"""
This type stub file was generated by pyright.
"""

from scipy._typing import Untyped

class _ParallelP:
    x: Untyped
    y: Untyped
    random_states: Untyped
    def __init__(self, x, y, random_states) -> None:
        ...
    
    def __call__(self, index) -> Untyped:
        ...
    


MGCResult: Untyped
def multiscale_graphcorr(x, y, compute_distance=..., reps: int = ..., workers: int = ..., is_twosamp: bool = ..., random_state: Untyped | None = ...) -> Untyped:
    ...

