from abc import ABC
from dataclasses import dataclass
from src.common.abstracts import SettingsABC
from src.common.types import Vector, RgbVector


class ScreenSettings(SettingsABC):
    width: int = 800
    height: int = 800

    def resolution(self) -> Vector:
        return (self.width, self.height)
    

class PaddleSettings(SettingsABC):
    width: int = 30
    height: int = 200
    default_position_x: int = 0
    default_position_y: int = 400

    @property
    def default_position(self) -> Vector:
        return (self.default_position_x, self.default_position_y)
    

class BallSettings(SettingsABC):
    radius: int = 50
    color: RgbVector = (0, 255, 255)
    default_position_x: int = 400
    default_position_y: int = 400
    default_velocity_x: int = 1
    default_velocity_y: int = 0


    @property
    def default_velocity(self) -> Vector:
        return (self.default_velocity_x, self.default_velocity_y)

    @property
    def default_position(self) -> Vector:
        return (self.default_position_x, self.default_position_y)


class GameSettings(SettingsABC):
    screen_settings: ScreenSettings = ScreenSettings()
    ball_settings: BallSettings = BallSettings()
    paddle_settings: PaddleSettings = PaddleSettings()
