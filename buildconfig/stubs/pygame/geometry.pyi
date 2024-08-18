from typing import (
    overload,
    Union,
    Callable,
    Protocol,
    Tuple,
)

from pygame import Rect, FRect
from pygame.typing import Coordinate, RectLike, SequenceLike
from .rect import Rect, FRect
from .math import Vector2

_CanBeCircle = Union[Circle, Tuple[Coordinate, float], SequenceLike[float]]

class _HasCirclettribute(Protocol):
    # An object that has a circle attribute that is either a circle, or a function
    # that returns a circle
    circle: Union[_CanBeCircle, Callable[[], _CanBeCircle]]

_CircleValue = Union[_CanBeCircle, _HasCirclettribute]
_CanBeCollided = Union[Circle, Rect, FRect, Coordinate, Vector2]

class Circle:
    @property
    def x(self) -> float: ...
    @x.setter
    def x(self, value: float) -> None: ...
    @property
    def y(self) -> float: ...
    @y.setter
    def y(self, value: float) -> None: ...
    @property
    def r(self) -> float: ...
    @r.setter
    def r(self, value: float) -> None: ...
    @property
    def radius(self) -> float: ...
    @radius.setter
    def radius(self, value: float) -> None: ...
    @property
    def r_sqr(self) -> float: ...
    @r_sqr.setter
    def r_sqr(self, value: float) -> None: ...
    @property
    def d(self) -> float: ...
    @d.setter
    def d(self, value: float) -> None: ...
    @property
    def diameter(self) -> float: ...
    @diameter.setter
    def diameter(self, value: float) -> None: ...
    @property
    def area(self) -> float: ...
    @area.setter
    def area(self, value: float) -> None: ...
    @property
    def circumference(self) -> float: ...
    @circumference.setter
    def circumference(self, value: float) -> None: ...
    @property
    def center(self) -> Tuple[float, float]: ...
    @center.setter
    def center(self, value: Coordinate) -> None: ...
    @overload
    def __init__(self, x: float, y: float, r: float) -> None: ...
    @overload
    def __init__(self, pos: Coordinate, r: float) -> None: ...
    @overload
    def __init__(self, circle: _CircleValue) -> None: ...
    @overload
    def move(self, x: float, y: float, /) -> Circle: ...
    @overload
    def move(self, move_by: Coordinate, /) -> Circle: ...
    @overload
    def move_ip(self, x: float, y: float, /) -> None: ...
    @overload
    def move_ip(self, move_by: Coordinate, /) -> None: ...
    @overload
    def collidepoint(self, x: float, y: float, /) -> bool: ...
    @overload
    def collidepoint(self, point: Coordinate, /) -> bool: ...
    @overload
    def collidecircle(self, circle: _CircleValue, /) -> bool: ...
    @overload
    def collidecircle(self, x: float, y: float, r: float, /) -> bool: ...
    @overload
    def collidecircle(self, center: Coordinate, r: float, /) -> bool: ...
    @overload
    def colliderect(self, rect: RectLike, /) -> bool: ...
    @overload
    def colliderect(self, x: float, y: float, w: float, h: float, /) -> bool: ...
    @overload
    def colliderect(self, topleft: Coordinate, size: Coordinate, /) -> bool: ...
    def collideswith(self, other: _CanBeCollided, /) -> bool: ...
    def contains(self, shape: _CanBeCollided) -> bool: ...
    @overload
    def update(self, circle: _CircleValue, /) -> None: ...
    @overload
    def update(self, x: float, y: float, r: float, /) -> None: ...
    @overload
    def update(self, center: Coordinate, r: float, /) -> None: ...
    @overload
    def rotate(self, angle: float, rotation_point: Coordinate, /) -> Circle: ...
    @overload
    def rotate(self, angle: float, /) -> Circle: ...
    @overload
    def rotate_ip(self, angle: float, rotation_point: Coordinate, /) -> None: ...
    @overload
    def rotate_ip(self, angle: float, /) -> None: ...
    def as_rect(self) -> Rect: ...
    def as_frect(self) -> FRect: ...
    def __copy__(self) -> Circle: ...
    copy = __copy__
