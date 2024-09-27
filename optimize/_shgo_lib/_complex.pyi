"""
This type stub file was generated by pyright.
"""

from collections.abc import Generator
from scipy._typing import Untyped

class Complex:
    dim: Untyped
    domain: Untyped
    bounds: Untyped
    symmetry: Untyped
    sfield: Untyped
    sfield_args: Untyped
    min_cons: Untyped
    g_cons: Untyped
    g_args: Untyped
    gen: int
    perm_cycle: int
    H: Untyped
    V: Untyped
    V_non_symm: Untyped
    def __init__(self, dim, domain: Untyped | None = ..., sfield: Untyped | None = ..., sfield_args=..., symmetry: Untyped | None = ..., constraints: Untyped | None = ..., workers: int = ...) -> None:
        ...
    
    def __call__(self) -> Untyped:
        ...
    
    def cyclic_product(self, bounds, origin, supremum, centroid: bool = ...) -> Generator[Untyped, None, Untyped]:
        ...
    
    origin: Untyped
    supremum: Untyped
    cp: Untyped
    triangulated_vectors: Untyped
    def triangulate(self, n: Untyped | None = ..., symmetry: Untyped | None = ..., centroid: bool = ..., printout: bool = ...):
        ...
    
    rls: Untyped
    def refine(self, n: int = ...):
        ...
    
    def refine_all(self, centroids: bool = ...):
        ...
    
    def refine_local_space(self, origin, supremum, bounds, centroid: int = ...) -> Generator[Untyped, None, None]:
        ...
    
    def refine_star(self, v):
        ...
    
    def split_edge(self, v1, v2) -> Untyped:
        ...
    
    def vpool(self, origin, supremum) -> Untyped:
        ...
    
    def vf_to_vv(self, vertices, simplices):
        ...
    
    def connect_vertex_non_symm(self, v_x, near: Untyped | None = ...) -> Untyped:
        ...
    
    def in_simplex(self, S, v_x, A_j0: Untyped | None = ...) -> Untyped:
        ...
    
    def deg_simplex(self, S, proj: Untyped | None = ...) -> Untyped:
        ...
    


