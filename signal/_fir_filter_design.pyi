"""
This type stub file was generated by pyright.
"""

from typing import Literal
from scipy._typing import Untyped, UntypedArray

def kaiser_beta(a) -> Untyped:
    ...

def kaiser_atten(numtaps, width) -> Untyped:
    ...

def kaiserord(ripple, width) -> Untyped:
    ...

def firwin(numtaps, cutoff, *, width: Untyped | None = ..., window: str = ..., pass_zero: bool = ..., scale: bool = ..., fs: Untyped | None = ...) -> Untyped:
    ...

def firwin2(numtaps, freq, gain, *, nfreqs: Untyped | None = ..., window: str = ..., antisymmetric: bool = ..., fs: Untyped | None = ...) -> Untyped:
    ...

def remez(numtaps, bands, desired, *, weight: Untyped | None = ..., type: str = ..., maxiter: int = ..., grid_density: int = ..., fs: Untyped | None = ...) -> Untyped:
    ...

def firls(numtaps, bands, desired, *, weight: Untyped | None = ..., fs: Untyped | None = ...) -> Untyped:
    ...

def minimum_phase(h: UntypedArray, method: Literal["homomorphic", "hilbert"] = ..., n_fft: int | None = ..., *, half: bool = ...) -> UntypedArray:
    ...

