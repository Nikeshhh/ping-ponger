from src.common.abstracts import GameObject
from src.common.dto import BallDTO
from src.common.types import Vector
from src.common.settings import BallSettings


class Ball(GameObject):
    """
    Ball object.
    Contains all data and logic related to ball.
    Should not contain ANY PYGAME LOGIC.
    """
    # Coordinates of center
    x: int = BallSettings.default_position_x
    y: int = BallSettings.default_position_y
    radius: int = BallSettings.radius

    @property
    def center_coords(self) -> Vector:
        return (self.center_x, self.center_y)
    
    @property
    def center_x(self) -> int:
        return self.x
    
    @property
    def center_y(self) -> int:
        return self.y
    
    @property
    def left(self) -> int:
        return self.x - self.radius
    
    @property
    def right(self) -> int:
        return self.x + self.radius
    
    @property
    def top(self) -> int:
        return self.y + self.radius
    
    @property
    def bottom(self) -> int:
        return self.y + self.radius
    
    def to_dto(self) -> BallDTO:
        return BallDTO(x=self.x, y=self.y)
    
    @classmethod
    def from_dto(cls, ball_dto: BallDTO) -> 'Ball':
        return Ball(x=ball_dto.x, y=ball_dto.y)
    