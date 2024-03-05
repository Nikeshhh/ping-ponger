from pygame.locals import *
from pygame.color import Color
from pygame.font import Font
from src.common.dto import InputDTO, LightGameDTO
import pygame
import socket
import pickle


class App:

    def __init__(self) -> None:
        pygame.init()
        flags = RESIZABLE
        App.screen = pygame.display.set_mode((800, 800), flags)
        App.client_socket: socket.socket = self._init_socket()
        App.t = Text('PingPong', (400, 400))


        App.running = True


    def _init_socket(self):
        return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def send_input(self, input: InputDTO):
        data = pickle.dumps(input)
        self.client_socket.sendto(data, self.server_address)

    def get_state(self) -> LightGameDTO:
        data, address = App.client_socket.recvfrom(1024)
        if address == self.server_address:
            return pickle.loads(data)
    
    def connect(self, host: str, port: int): # Удивительно но работает
        msg = pickle.dumps(InputDTO(connected=True))
        App.client_socket.sendto(msg, (host, port))
        data, self.server_address = App.client_socket.recvfrom(1024)
        if data.decode('utf-8') == 'connected':
            print('connected')
        else:
            print(f'some error: {data.decode("utf-8")}')
        return True

    def disconnect(self): # TODO: Не работает
        msg = pickle.dumps(InputDTO(connected=False))
        App.client_socket.sendto(msg, self.server_address)
        data, _ = App.client_socket.recvfrom(1024)
        if data.decode('utf-8') == 'disconnected':
            print('disconnected')
        else:
            print('error while disconnecting')
        return True

    def run(self):
        while not(self.connect('192.168.0.101', 1488)):
            pygame.time.wait(500)
            continue
        rect = pygame.Rect(0, 0, 30, 200)

        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False


            keys = pygame.key.get_pressed()
            input = InputDTO(bool(keys[K_UP]), bool(keys[K_DOWN]))
            self.send_input(input)
            state = self.get_state()
            rect.x = state.x
            rect.y = state.y


            App.screen.fill(Color('gray'))
            
            pygame.draw.rect(App.screen, (255, 0, 255), rect)
            App.t.draw()
            pygame.display.update()
            pygame.time.wait(1000 // 60)
        while not(self.disconnect()):
            pygame.time.wait(500)
            continue
        pygame.quit()


class Text:

    def __init__(self, text: str, pos: tuple[int, int], **options) -> None:
        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = 72
        self.fontcolor = Color('black')
        self.get_font()
        self.render()

    def set_text(self, text: str):
        self.__init__(text, self.pos)

    def get_font(self):
        self.font = Font(self.fontname, self.fontsize)

    def render(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.center = self.pos

    def draw(self):
        App.screen.blit(self.img, self.rect)


class Scene:
    id = 0
    color = Color('grey')

    def __init__(self, *args, **kwargs) -> None:
        App.scenes.append(self)
        App.scene = self

        self.id = Scene.id
        Scene.id += 1
        self.nodes = []
        self.bg = Scene.bg

    def draw(self):
        App.screen.fill(self.bg)
        for node in self.nodes:
            node.draw()
        pygame.display.flip()


if __name__ == '__main__':
    App().run()