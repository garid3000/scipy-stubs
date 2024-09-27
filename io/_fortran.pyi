"""
This type stub file was generated by pyright.
"""

from types import TracebackType
from scipy._typing import Untyped

class FortranEOFError(TypeError, OSError):
    ...


class FortranFormattingError(TypeError, OSError):
    ...


class FortranFile:
    def __init__(self, filename, mode: str = ..., header_dtype=...) -> None:
        ...
    
    def write_record(self, *items):
        ...
    
    def read_record(self, *dtypes, **kwargs) -> Untyped:
        ...
    
    def read_ints(self, dtype: str = ...) -> Untyped:
        ...
    
    def read_reals(self, dtype: str = ...) -> Untyped:
        ...
    
    def close(self):
        ...
    
    def __enter__(self) -> Untyped:
        ...
    
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, tb: TracebackType | None):
        ...
    


