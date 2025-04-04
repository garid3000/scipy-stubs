"""
This type stub file was generated by pyright.
"""

from scipy._typing import Untyped

def differential_evolution(func, bounds, args=..., strategy: str = ..., maxiter: int = ..., popsize: int = ..., tol: float = ..., mutation=..., recombination: float = ..., seed: Untyped | None = ..., callback: Untyped | None = ..., disp: bool = ..., polish: bool = ..., init: str = ..., atol: int = ..., updating: str = ..., workers: int = ..., constraints=..., x0: Untyped | None = ..., *, integrality: Untyped | None = ..., vectorized: bool = ...) -> Untyped:
    ...

class DifferentialEvolutionSolver:
    mutation_func: Untyped
    strategy: Untyped
    callback: Untyped
    polish: Untyped
    vectorized: Untyped
    scale: Untyped
    dither: Untyped
    cross_over_probability: Untyped
    func: Untyped
    args: Untyped
    limits: Untyped
    maxiter: Untyped
    maxfun: Untyped
    parameter_count: Untyped
    random_number_generator: Untyped
    integrality: Untyped
    num_population_members: Untyped
    population_shape: Untyped
    constraints: Untyped
    total_constraints: Untyped
    constraint_violation: Untyped
    feasible: Untyped
    disp: Untyped
    def __init__(self, func, bounds, args=..., strategy: str = ..., maxiter: int = ..., popsize: int = ..., tol: float = ..., mutation=..., recombination: float = ..., seed: Untyped | None = ..., maxfun=..., callback: Untyped | None = ..., disp: bool = ..., polish: bool = ..., init: str = ..., atol: int = ..., updating: str = ..., workers: int = ..., constraints=..., x0: Untyped | None = ..., *, integrality: Untyped | None = ..., vectorized: bool = ...) -> None:
        ...
    
    population: Untyped
    population_energies: Untyped
    def init_population_lhs(self):
        ...
    
    def init_population_qmc(self, qmc_engine):
        ...
    
    def init_population_random(self):
        ...
    
    def init_population_array(self, init):
        ...
    
    @property
    def x(self) -> Untyped:
        ...
    
    @property
    def convergence(self) -> Untyped:
        ...
    
    def converged(self) -> Untyped:
        ...
    
    def solve(self) -> Untyped:
        ...
    
    def __iter__(self) -> Untyped:
        ...
    
    def __enter__(self) -> Untyped:
        ...
    
    def __exit__(self, *args) -> Untyped:
        ...
    
    def __next__(self) -> Untyped:
        ...
    


class _ConstraintWrapper:
    constraint: Untyped
    fun: Untyped
    num_constr: Untyped
    parameter_count: Untyped
    bounds: Untyped
    def __init__(self, constraint, x0) -> None:
        ...
    
    def __call__(self, x) -> Untyped:
        ...
    
    def violation(self, x) -> Untyped:
        ...
    


