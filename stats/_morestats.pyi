"""
This type stub file was generated by pyright.
"""

from typing import NamedTuple
from scipy._typing import Untyped

__all__ = ["anderson", "anderson_ksamp", "ansari", "bartlett", "bayes_mvs", "boxcox", "boxcox_llf", "boxcox_normmax", "boxcox_normplot", "circmean", "circstd", "circvar", "directional_stats", "false_discovery_control", "fligner", "kstat", "kstatvar", "levene", "median_test", "mood", "mvsdist", "ppcc_max", "ppcc_plot", "probplot", "shapiro", "wilcoxon", "yeojohnson", "yeojohnson_llf", "yeojohnson_normmax", "yeojohnson_normplot"]
class Mean(NamedTuple):
    statistic: Untyped
    minmax: Untyped
    ...


class Variance(NamedTuple):
    statistic: Untyped
    minmax: Untyped
    ...


class Std_dev(NamedTuple):
    statistic: Untyped
    minmax: Untyped
    ...


def bayes_mvs(data, alpha: float = ...) -> Untyped:
    ...

def mvsdist(data) -> Untyped:
    ...

def kstat(data, n: int = ..., *, axis: Untyped | None = ...) -> Untyped:
    ...

def kstatvar(data, n: int = ..., *, axis: Untyped | None = ...) -> Untyped:
    ...

def probplot(x, sparams=..., dist: str = ..., fit: bool = ..., plot: Untyped | None = ..., rvalue: bool = ...) -> Untyped:
    ...

def ppcc_max(x, brack=..., dist: str = ...) -> Untyped:
    ...

def ppcc_plot(x, a, b, dist: str = ..., plot: Untyped | None = ..., N: int = ...) -> Untyped:
    ...

def boxcox_llf(lmb, data) -> Untyped:
    ...

def boxcox(x, lmbda: Untyped | None = ..., alpha: Untyped | None = ..., optimizer: Untyped | None = ...) -> Untyped:
    ...

class _BigFloat:
    ...


def boxcox_normmax(x, brack: Untyped | None = ..., method: str = ..., optimizer: Untyped | None = ..., *, ymax=...) -> Untyped:
    ...

def boxcox_normplot(x, la, lb, plot: Untyped | None = ..., N: int = ...) -> Untyped:
    ...

def yeojohnson(x, lmbda: Untyped | None = ...) -> Untyped:
    ...

def yeojohnson_llf(lmb, data) -> Untyped:
    ...

def yeojohnson_normmax(x, brack: Untyped | None = ...) -> Untyped:
    ...

def yeojohnson_normplot(x, la, lb, plot: Untyped | None = ..., N: int = ...) -> Untyped:
    ...

class ShapiroResult(NamedTuple):
    statistic: Untyped
    pvalue: Untyped
    ...


def shapiro(x) -> Untyped:
    ...

AndersonResult: Untyped
def anderson(x, dist: str = ...) -> Untyped:
    ...

Anderson_ksampResult: Untyped
def anderson_ksamp(samples, midrank: bool = ..., *, method: Untyped | None = ...) -> Untyped:
    ...

class AnsariResult(NamedTuple):
    statistic: Untyped
    pvalue: Untyped
    ...


class _ABW:
    m: Untyped
    n: Untyped
    astart: Untyped
    total: Untyped
    freqs: Untyped
    def __init__(self) -> None:
        ...
    
    def pmf(self, k, n, m) -> Untyped:
        ...
    
    def cdf(self, k, n, m) -> Untyped:
        ...
    
    def sf(self, k, n, m) -> Untyped:
        ...
    


def ansari(x, y, alternative: str = ...) -> Untyped:
    ...

class BartlettResult(NamedTuple):
    statistic: Untyped
    pvalue: Untyped
    ...


def bartlett(*samples, axis: int = ...) -> Untyped:
    ...

class LeveneResult(NamedTuple):
    statistic: Untyped
    pvalue: Untyped
    ...


def levene(*samples, center: str = ..., proportiontocut: float = ...) -> Untyped:
    ...

class FlignerResult(NamedTuple):
    statistic: Untyped
    pvalue: Untyped
    ...


def fligner(*samples, center: str = ..., proportiontocut: float = ...) -> Untyped:
    ...

def mood(x, y, axis: int = ..., alternative: str = ...) -> Untyped:
    ...

WilcoxonResult: Untyped
def wilcoxon_result_unpacker(res) -> Untyped:
    ...

def wilcoxon_result_object(statistic, pvalue, zstatistic: Untyped | None = ...) -> Untyped:
    ...

def wilcoxon_outputs(kwds) -> Untyped:
    ...

def wilcoxon(x, y: Untyped | None = ..., zero_method: str = ..., correction: bool = ..., alternative: str = ..., method: str = ..., *, axis: int = ...) -> Untyped:
    ...

MedianTestResult: Untyped
def median_test(*samples, ties: str = ..., correction: bool = ..., lambda_: int = ..., nan_policy: str = ...) -> Untyped:
    ...

def circmean(samples, high=..., low: int = ..., axis: Untyped | None = ..., nan_policy: str = ...) -> Untyped:
    ...

def circvar(samples, high=..., low: int = ..., axis: Untyped | None = ..., nan_policy: str = ...) -> Untyped:
    ...

def circstd(samples, high=..., low: int = ..., axis: Untyped | None = ..., nan_policy: str = ..., *, normalize: bool = ...) -> Untyped:
    ...

class DirectionalStats:
    mean_direction: Untyped
    mean_resultant_length: Untyped
    def __init__(self, mean_direction, mean_resultant_length) -> None:
        ...
    


def directional_stats(samples, *, axis: int = ..., normalize: bool = ...) -> Untyped:
    ...

def false_discovery_control(ps, *, axis: int = ..., method: str = ...) -> Untyped:
    ...

