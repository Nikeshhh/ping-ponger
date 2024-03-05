from src.common.abstracts import GameObject
from src.common.dto import PaddleDTO, PlayerDTO
from src.common.types import Vector
from src.common.settings import PaddleSettings
from dataclasses import dataclass


class Paddle(GameObject):
    # SHOULD NOT IMPLEMENT ANY PYGAME RELATED LOGIC
    """
    Class for player's paddle.
    """
    # TODO: incapsulate paddle logic into this class
    width: int = PaddleSettings.width
    height: int = PaddleSettings.height
    # Pygame axis coordinates (starting as top left)
    x: int = PaddleSettings.default_position_x
    y: int = PaddleSettings.default_position_y
    # Paddle's velocity values
    velocity_x: int = 0
    velocity_y: int = 0
    
    @property
    def center_x(self) -> int:
        return (self.x + self.width) // 2
    
    @property
    def center_y(self) -> int:
        return (self.y + self.height) // 2
    
    @property
    def center_coords(self) -> Vector:
        return (self.center_x, self.center_y)
    
    @property
    def top(self) -> int:
        return self.y
    
    @property
    def bottom(self) -> int:
        return self.y + self.height

    def move(self):
        self.y += self.velocity_y

    def to_dto(self) -> PaddleDTO:
        """Converts Paddle object into PaddleDTO object"""
        return PaddleDTO(self.x, self.y)
    
    @classmethod
    def from_dto(cls, paddle_dto: PaddleDTO) -> 'Paddle':
        """Converts PaddleDTO object into Paddle object"""
        return Paddle(x=paddle_dto.x, y=paddle_dto.y)


@dataclass
class Player:
    """
    Class for game player's, holding all related data.
    Player should have it's own paddle and a score.
    """
    paddle: Paddle
    number: int
    score: int = 0

    def to_dto(self) -> PlayerDTO:
        """Converts Player object into PlayerDTO object"""
        return PlayerDTO(
            score=self.score,
            paddle=self.paddle.to_dto()
        )
    
    def from_dto(cls, player_dto: PlayerDTO) -> 'Player':
        """Converts PlayerDTO object into Player object"""
        return Player(
            paddle=Paddle.from_dto(player_dto.paddle),
            score=player_dto.score,
        )