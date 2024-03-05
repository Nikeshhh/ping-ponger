from abc import ABC
from dataclasses import dataclass
from src.common.types import Vector


@dataclass(frozen=True)
class DataTransferObject(ABC):
    """
    Base interface for DTO.
    Should be implemented as simple as possible.
    FROZEN = TRUE.
    """
    ...


@dataclass
class GameObject(ABC):
    """Base interface for game objects with coordinates"""
    x: int = 0
    y: int = 0

    velocity_x: int = 0
    velocity_y: int = 0
    
    @property
    def coords(self) -> Vector:
        """Returns object's coordinates as a Vector"""
        return (self.x, self.y)

    @property
    def center_coords(self) -> Vector:
        """Returns object's center coordinates as a Vector"""
        ...

    @property
    def center_x(self) -> int:
        """Returns object's center coordinate on X axis"""
        ...

    @property
    def center_y(self) -> int:
        """Returns object's center coordinate on Y axis"""
        ...

    @property
    def left(self) -> int:
        """Returns object's left border coordinate on X axis"""
        ...

    @property
    def right(self) -> int:
        """Returns object's right border coordinate on X axis"""
        ...

    @property
    def top(self) -> int:
        """Returns object's top border coordinate on Y axis"""
        ...

    @property
    def bottom(self) -> int:
        """Returns object's bottom border coordinate on Y axis"""
        ...

    @property
    def velocity(self) -> Vector:
        """Returns object's velocity in Vector form"""
        return (self.velocity_x, self.velocity_y)
    
    @velocity.setter
    def velocity(self, val: Vector):
        """Allows to set velocity as vector"""
        self.velocity_x, self.velocity_y = val
    
    def move(self):
        """Move object's coordinates, based on current velocity"""
        self.x += self.velocity_x
        self.y += self.velocity_y

    @classmethod
    def check_collision(cls, object_1: 'GameObject', object_2: 'GameObject') -> bool:
        """
        Checks collision between 2 game objects.
        Returns True, if objects there is a collision.
        Returns False, if there is no collision.
        """
        # TODO: implement, think about making it object method
        ... 

    def to_dto(self) -> DataTransferObject:
        """Returns object, converted into it's DTO"""
        ...

    @classmethod
    def from_dto(cls, object: DataTransferObject) -> 'GameObject':
        """
        Classmethod.
        Returns object, converted from it's DTO.
        """
        ...