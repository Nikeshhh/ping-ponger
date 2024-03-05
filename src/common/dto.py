from src.common.abstracts import DataTransferObject


class CanvasObject(DataTransferObject):
    x: int = 0
    y: int = 0

    @property
    def coords(self):
        return (self.x, self.y)


class PaddleDTO(CanvasObject):
    ...


class BallDTO(CanvasObject):
    ...


class PlayerDTO(DataTransferObject):
    score: int = 0
    paddle: PaddleDTO = PaddleDTO()
    

class GameDTO(DataTransferObject):
    ball_data: BallDTO = BallDTO()
    player1_data: PlayerDTO = PlayerDTO()
    player2_data: PlayerDTO = PlayerDTO()


class InputDTO(DataTransferObject):
    key_up: bool = False
    key_down: bool = False
    connected: bool = None

    def __str__(self) -> str:
        return f'key_up: {self.key_up}, key_down: {self.key_down}'
    

class LightGameDTO(DataTransferObject):
    x: int
    y: int