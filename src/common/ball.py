from src.common.abstracts import GameObject


class Ball(GameObject):
    """
    Ball object.
    Contains all data and logic related to ball.
    Should not contain ANY PYGAME LOGIC.
    """
    x: int
    y: int
    radius: int