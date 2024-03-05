from src.common.settings import GameSettings
from src.common.game import Paddle, Player
from src.common.ball import Ball


class Game:
    settings: GameSettings
    player_1: Player
    player_2: Player
    ball: Ball
    
    def __init__(self) -> None:
        self.settings = GameSettings()
        self.player_1 = Paddle(
            width=self.settings.paddle_settings.width,
            height=self.settings.paddle_settings.height,
            x=self.settings.paddle_settings.default_position_x,
            y=self.settings.paddle_settings.default_position_y
        )
        self.player_2 = Paddle(
            width=self.settings.paddle_settings.width,
            height=self.settings.paddle_settings.height,
            x=self.settings.paddle_settings.default_position_x + self.settings.screen_settings.width,
            y=self.settings.paddle_settings.default_position_y
        )
        self.paddle_velocity = (0, 0)

    def tick(self, velocity: tuple[int, int] = (0, 0)):
        self.paddle_velocity = velocity
        if (velocity[1] > 0 and self.paddle.bottom < self.settings.screen_settings.height) or (velocity[1] < 0 and self.paddle.top > 0):
            self.paddle.x += self.paddle_velocity[0]
            self.paddle.y += self.paddle_velocity[1]
        
        print(f'Current position: ({self.paddle.x}, {self.paddle.y})')