"""
This type stub file was generated by pyright.
"""

import numpy as np
import numpy.typing as npt
from typing import Any, TypeAlias
from typing_extensions import final

__all__ = ["ConvexHull", "Delaunay", "HalfspaceIntersection", "QhullError", "Voronoi", "tsearch"]
class QhullError(RuntimeError):
    ...


_Array_i: TypeAlias = npt.NDArray[np.intc]
_Array_n: TypeAlias = npt.NDArray[np.intp]
_Array_f8: TypeAlias = npt.NDArray[np.float64]
@final
class _Qhull:
    @property
    def ndim(self) -> int:
        ...
    
    mode_option: bytes
    options: bytes
    furthest_site: bool
    def __init__(self, mode_option: bytes, points: _Array_f8, options: None | bytes = ..., required_options: None | bytes = ..., furthest_site: bool = ..., incremental: bool = ..., interior_point: None | _Array_f8 = ...) -> None:
        ...
    
    def check_active(self) -> None:
        ...
    
    def close(self) -> None:
        ...
    
    def get_points(self) -> _Array_f8:
        ...
    
    def add_points(self, points: npt.ArrayLike, interior_point: npt.ArrayLike = ...) -> None:
        ...
    
    def get_paraboloid_shift_scale(self) -> tuple[float, float]:
        ...
    
    def volume_area(self) -> tuple[float, float]:
        ...
    
    def triangulate(self) -> None:
        ...
    
    def get_simplex_facet_array(self) -> tuple[_Array_i, _Array_i, _Array_f8, _Array_i, _Array_i]:
        ...
    
    def get_hull_points(self) -> _Array_f8:
        ...
    
    def get_hull_facets(self) -> tuple[list[list[int]], _Array_f8]:
        ...
    
    def get_voronoi_diagram(self) -> tuple[_Array_f8, _Array_i, list[list[int]], list[list[int]], _Array_n]:
        ...
    
    def get_extremes_2d(self) -> _Array_i:
        ...
    


class _QhullUser:
    ndim: int
    npoints: int
    min_bound: _Array_f8
    max_bound: _Array_f8
    def __init__(self, qhull: _Qhull, incremental: bool = ...) -> None:
        ...
    
    def close(self) -> None:
        ...
    


class Delaunay(_QhullUser):
    furthest_site: bool
    paraboloid_scale: float
    paraboloid_shift: float
    simplices: _Array_i
    neighbors: _Array_i
    equations: _Array_f8
    coplanar: _Array_i
    good: _Array_i
    nsimplex: int
    vertices: _Array_i
    def __init__(self, points: npt.ArrayLike, furthest_site: bool = ..., incremental: bool = ..., qhull_options: None | str = ...) -> None:
        ...
    
    def add_points(self, points: npt.ArrayLike, restart: bool = ...) -> None:
        ...
    
    @property
    def points(self) -> _Array_f8:
        ...
    
    @property
    def transform(self) -> _Array_f8:
        ...
    
    @property
    def vertex_to_simplex(self) -> _Array_i:
        ...
    
    @property
    def vertex_neighbor_vertices(self) -> tuple[_Array_i, _Array_i]:
        ...
    
    @property
    def convex_hull(self) -> _Array_i:
        ...
    
    def find_simplex(self, xi: npt.ArrayLike, bruteforce: bool = ..., tol: float = ...) -> _Array_i:
        ...
    
    def plane_distance(self, xi: npt.ArrayLike) -> _Array_f8:
        ...
    
    def lift_points(self, x: npt.ArrayLike) -> _Array_f8:
        ...
    


def tsearch(tri: Delaunay, xi: npt.ArrayLike) -> _Array_i:
    ...

class ConvexHull(_QhullUser):
    simplices: _Array_i
    neighbors: _Array_i
    equations: _Array_f8
    coplanar: _Array_i
    good: None | npt.NDArray[np.bool_]
    volume: float
    area: float
    nsimplex: int
    def __init__(self, points: npt.ArrayLike, incremental: bool = ..., qhull_options: None | str = ...) -> None:
        ...
    
    def add_points(self, points: npt.ArrayLike, restart: bool = ...) -> None:
        ...
    
    @property
    def points(self) -> _Array_f8:
        ...
    
    @property
    def vertices(self) -> _Array_i:
        ...
    


class Voronoi(_QhullUser):
    vertices: _Array_f8
    ridge_points: _Array_i
    ridge_vertices: list[list[int]]
    regions: list[list[int]]
    point_region: _Array_n
    furthest_site: bool
    def __init__(self, points: npt.ArrayLike, furthest_site: bool = ..., incremental: bool = ..., qhull_options: None | str = ...) -> None:
        ...
    
    def add_points(self, points: npt.ArrayLike, restart: bool = ...) -> None:
        ...
    
    @property
    def points(self) -> _Array_f8:
        ...
    
    @property
    def ridge_dict(self) -> dict[tuple[int, int], list[int]]:
        ...
    


class HalfspaceIntersection(_QhullUser):
    interior_point: _Array_f8
    dual_facets: list[list[int]]
    dual_equations: _Array_f8
    dual_points: _Array_f8
    dual_volume: float
    dual_area: float
    intersections: _Array_f8
    ndim: int
    nineq: int
    def __init__(self, halfspaces: npt.ArrayLike, interior_point: npt.ArrayLike, incremental: bool = ..., qhull_options: None | str = ...) -> None:
        ...
    
    def add_halfspaces(self, halfspaces: npt.ArrayLike, restart: bool = ...) -> None:
        ...
    
    @property
    def halfspaces(self) -> _Array_f8:
        ...
    
    @property
    def dual_vertices(self) -> npt.NDArray[np.integer[Any]]:
        ...
    


