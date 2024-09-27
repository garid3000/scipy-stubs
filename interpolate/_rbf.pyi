"""
This type stub file was generated by pyright.
"""

from scipy._typing import Untyped

class Rbf:
    xi: Untyped
    N: Untyped
    mode: Untyped
    di: Untyped
    norm: Untyped
    epsilon: Untyped
    smooth: Untyped
    function: Untyped
    nodes: Untyped
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @property
    def A(self) -> Untyped:
        ...
    
    def __call__(self, *args) -> Untyped:
        ...
    


