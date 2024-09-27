"""
This type stub file was generated by pyright.
"""

from scipy._typing import Untyped

class Storage:
    def __init__(self, minres) -> None:
        ...
    
    def update(self, minres) -> Untyped:
        ...
    
    def get_lowest(self) -> Untyped:
        ...
    


class BasinHoppingRunner:
    x: Untyped
    minimizer: Untyped
    step_taking: Untyped
    accept_tests: Untyped
    disp: Untyped
    nstep: int
    res: Untyped
    energy: Untyped
    incumbent_minres: Untyped
    storage: Untyped
    def __init__(self, x0, minimizer, step_taking, accept_tests, disp: bool = ...) -> None:
        ...
    
    xtrial: Untyped
    energy_trial: Untyped
    accept: Untyped
    def one_cycle(self) -> Untyped:
        ...
    
    def print_report(self, energy_trial, accept):
        ...
    


class AdaptiveStepsize:
    takestep: Untyped
    target_accept_rate: Untyped
    interval: Untyped
    factor: Untyped
    verbose: Untyped
    nstep: int
    nstep_tot: int
    naccept: int
    def __init__(self, takestep, accept_rate: float = ..., interval: int = ..., factor: float = ..., verbose: bool = ...) -> None:
        ...
    
    def __call__(self, x) -> Untyped:
        ...
    
    def take_step(self, x) -> Untyped:
        ...
    
    def report(self, accept, **kwargs):
        ...
    


class RandomDisplacement:
    stepsize: Untyped
    random_gen: Untyped
    def __init__(self, stepsize: float = ..., random_gen: Untyped | None = ...) -> None:
        ...
    
    def __call__(self, x) -> Untyped:
        ...
    


class MinimizerWrapper:
    minimizer: Untyped
    func: Untyped
    kwargs: Untyped
    def __init__(self, minimizer, func: Untyped | None = ..., **kwargs) -> None:
        ...
    
    def __call__(self, x0) -> Untyped:
        ...
    


class Metropolis:
    beta: Untyped
    random_gen: Untyped
    def __init__(self, T, random_gen: Untyped | None = ...) -> None:
        ...
    
    def accept_reject(self, res_new, res_old) -> Untyped:
        ...
    
    def __call__(self, *, res_new, res_old) -> Untyped:
        ...
    


def basinhopping(func, x0, niter: int = ..., T: float = ..., stepsize: float = ..., minimizer_kwargs: Untyped | None = ..., take_step: Untyped | None = ..., accept_test: Untyped | None = ..., callback: Untyped | None = ..., interval: int = ..., disp: bool = ..., niter_success: Untyped | None = ..., seed: Untyped | None = ..., *, target_accept_rate: float = ..., stepwise_factor: float = ...) -> Untyped:
    ...

