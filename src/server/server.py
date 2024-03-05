import pickle
from .game import Game
from src.common.dto import InputDTO, LightGameDTO
import socket
import pygame


class PingPongServer:
    _server_socket: socket.socket
    _game: Game

    def __init__(self, host: str = '10.154.3.36', port: int = 1488) -> None:
        self.host = host
        self.port = port
        self._game = Game()
        self._server_socket = self._init_socket(host, port)
        self._clients = []
        self.running = True

    def _init_socket(self, host: str, port: int) -> socket.socket:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind((host, port))
        return server_socket
    
    def get_inputs(self) -> InputDTO:
        data, address = self._server_socket.recvfrom(1024)
        input: InputDTO = pickle.loads(data)
        if input.connected is True:
            self._clients.append(address)
            self._server_socket.sendto('connected'.encode(), address)
            print(f'Client<{address}> has connected')
        elif input.connected is False:
            self._clients.remove(address)
            self._server_socket.sendto('disconnected'.encode(), address)
            print(f'Client<{address}> has disconnected')
        print(f'Client<{address}> sent {input}')
        return input

    def update_game_state(self, input: InputDTO):
        vel_y = 0
        if input.key_up:
            vel_y -= 10
        if input.key_down:
            vel_y += 10

        self._game.tick((0, vel_y))

    def send_out_game_state(self):
        state = pickle.dumps(LightGameDTO(self._game.paddle.x, self._game.paddle.y))
        for client in self._clients:
            self._server_socket.sendto(state, client)
    
    def run(self):
        while self.running:
            print('loop')
            input = self.get_inputs()
            self.update_game_state(input)
            self.send_out_game_state()
            pygame.time.wait(1000 // 60)
