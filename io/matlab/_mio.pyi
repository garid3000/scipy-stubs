"""
This type stub file was generated by pyright.
"""

from scipy._typing import Untyped

def mat_reader_factory(file_name, appendmat: bool = ..., **kwargs) -> Untyped:
    ...

def loadmat(file_name, mdict: Untyped | None = ..., appendmat: bool = ..., **kwargs) -> Untyped:
    ...

def savemat(file_name, mdict, appendmat: bool = ..., format: str = ..., long_field_names: bool = ..., do_compression: bool = ..., oned_as: str = ...):
    ...

def whosmat(file_name, appendmat: bool = ..., **kwargs) -> Untyped:
    ...

