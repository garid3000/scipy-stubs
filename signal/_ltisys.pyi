"""
This type stub file was generated by pyright.
"""

from typing_extensions import Self, override
from scipy._typing import Untyped

__all__ = ["StateSpace", "TransferFunction", "ZerosPolesGain", "bode", "dbode", "dfreqresp", "dimpulse", "dlsim", "dlti", "dstep", "freqresp", "impulse", "lsim", "lti", "place_poles", "step"]
class LinearTimeInvariant:
    def __new__(cls, *system, **kwargs) -> Self:
        ...
    
    inputs: Untyped
    outputs: Untyped
    def __init__(self) -> None:
        ...
    
    @property
    def dt(self) -> Untyped:
        ...
    
    @property
    def zeros(self) -> Untyped:
        ...
    
    @property
    def poles(self) -> Untyped:
        ...
    


class lti(LinearTimeInvariant):
    def __new__(cls, *system) -> Self:
        ...
    
    def __init__(self, *system) -> None:
        ...
    
    def impulse(self, X0: Untyped | None = ..., T: Untyped | None = ..., N: Untyped | None = ...) -> Untyped:
        ...
    
    def step(self, X0: Untyped | None = ..., T: Untyped | None = ..., N: Untyped | None = ...) -> Untyped:
        ...
    
    def output(self, U, T, X0: Untyped | None = ...) -> Untyped:
        ...
    
    def bode(self, w: Untyped | None = ..., n: int = ...) -> Untyped:
        ...
    
    def freqresp(self, w: Untyped | None = ..., n: int = ...) -> Untyped:
        ...
    
    def to_discrete(self, dt, method: str = ..., alpha: Untyped | None = ...) -> Untyped:
        ...
    


class dlti(LinearTimeInvariant):
    def __new__(cls, *system, **kwargs) -> Self:
        ...
    
    def __init__(self, *system, **kwargs) -> None:
        ...
    
    @property
    def dt(self) -> Untyped:
        ...
    
    @dt.setter
    def dt(self, dt):
        ...
    
    def impulse(self, x0: Untyped | None = ..., t: Untyped | None = ..., n: Untyped | None = ...) -> Untyped:
        ...
    
    def step(self, x0: Untyped | None = ..., t: Untyped | None = ..., n: Untyped | None = ...) -> Untyped:
        ...
    
    def output(self, u, t, x0: Untyped | None = ...) -> Untyped:
        ...
    
    def bode(self, w: Untyped | None = ..., n: int = ...) -> Untyped:
        ...
    
    def freqresp(self, w: Untyped | None = ..., n: int = ..., whole: bool = ...) -> Untyped:
        ...
    


class TransferFunction(LinearTimeInvariant):
    def __new__(cls, *system, **kwargs) -> Self:
        ...
    
    def __init__(self, *system, **kwargs) -> None:
        ...
    
    @property
    def num(self) -> Untyped:
        ...
    
    @num.setter
    def num(self, num):
        ...
    
    outputs: int
    inputs: int
    @property
    def den(self) -> Untyped:
        ...
    
    @den.setter
    def den(self, den):
        ...
    
    def to_tf(self) -> Untyped:
        ...
    
    def to_zpk(self) -> Untyped:
        ...
    
    def to_ss(self) -> Untyped:
        ...
    


class TransferFunctionContinuous(TransferFunction, lti):
    @override
    def to_discrete(self, dt, method: str = ..., alpha: Untyped | None = ...) -> Untyped:
        ...
    


class TransferFunctionDiscrete(TransferFunction, dlti):
    ...


class ZerosPolesGain(LinearTimeInvariant):
    inputs: int
    outputs: int
    def __new__(cls, *system, **kwargs) -> Self:
        ...
    
    def __init__(self, *system, **kwargs) -> None:
        ...
    
    @property
    def zeros(self) -> Untyped:
        ...
    
    @zeros.setter
    def zeros(self, zeros):
        ...
    
    @property
    def poles(self) -> Untyped:
        ...
    
    @poles.setter
    def poles(self, poles):
        ...
    
    @property
    def gain(self) -> Untyped:
        ...
    
    @gain.setter
    def gain(self, gain):
        ...
    
    def to_tf(self) -> Untyped:
        ...
    
    def to_zpk(self) -> Untyped:
        ...
    
    def to_ss(self) -> Untyped:
        ...
    


class ZerosPolesGainContinuous(ZerosPolesGain, lti):
    def to_discrete(self, dt, method: str = ..., alpha: Untyped | None = ...) -> Untyped:
        ...
    


class ZerosPolesGainDiscrete(ZerosPolesGain, dlti):
    ...


class StateSpace(LinearTimeInvariant):
    __array_priority__: float
    __array_ufunc__: Untyped
    inputs: Untyped
    outputs: Untyped
    def __new__(cls, *system, **kwargs) -> Self:
        ...
    
    def __init__(self, *system, **kwargs) -> None:
        ...
    
    def __mul__(self, other) -> Untyped:
        ...
    
    def __rmul__(self, other) -> Untyped:
        ...
    
    def __neg__(self) -> Untyped:
        ...
    
    def __add__(self, other) -> Untyped:
        ...
    
    def __sub__(self, other) -> Untyped:
        ...
    
    def __radd__(self, other) -> Untyped:
        ...
    
    def __rsub__(self, other) -> Untyped:
        ...
    
    def __truediv__(self, other) -> Untyped:
        ...
    
    @property
    def A(self) -> Untyped:
        ...
    
    @A.setter
    def A(self, A):
        ...
    
    @property
    def B(self) -> Untyped:
        ...
    
    @B.setter
    def B(self, B):
        ...
    
    @property
    def C(self) -> Untyped:
        ...
    
    @C.setter
    def C(self, C):
        ...
    
    @property
    def D(self) -> Untyped:
        ...
    
    @D.setter
    def D(self, D):
        ...
    
    def to_tf(self, **kwargs) -> Untyped:
        ...
    
    def to_zpk(self, **kwargs) -> Untyped:
        ...
    
    def to_ss(self) -> Untyped:
        ...
    


class StateSpaceContinuous(StateSpace, lti):
    def to_discrete(self, dt, method: str = ..., alpha: Untyped | None = ...) -> Untyped:
        ...
    


class StateSpaceDiscrete(StateSpace, dlti):
    ...


def lsim(system, U, T, X0: Untyped | None = ..., interp: bool = ...) -> Untyped:
    ...

def impulse(system, X0: Untyped | None = ..., T: Untyped | None = ..., N: Untyped | None = ...) -> Untyped:
    ...

def step(system, X0: Untyped | None = ..., T: Untyped | None = ..., N: Untyped | None = ...) -> Untyped:
    ...

def bode(system, w: Untyped | None = ..., n: int = ...) -> Untyped:
    ...

def freqresp(system, w: Untyped | None = ..., n: int = ...) -> Untyped:
    ...

class Bunch:
    def __init__(self, **kwds) -> None:
        ...
    


def place_poles(A, B, poles, method: str = ..., rtol: float = ..., maxiter: int = ...) -> Untyped:
    ...

def dlsim(system, u, t: Untyped | None = ..., x0: Untyped | None = ...) -> Untyped:
    ...

def dimpulse(system, x0: Untyped | None = ..., t: Untyped | None = ..., n: Untyped | None = ...) -> Untyped:
    ...

def dstep(system, x0: Untyped | None = ..., t: Untyped | None = ..., n: Untyped | None = ...) -> Untyped:
    ...

def dfreqresp(system, w: Untyped | None = ..., n: int = ..., whole: bool = ...) -> Untyped:
    ...

def dbode(system, w: Untyped | None = ..., n: int = ...) -> Untyped:
    ...

