from dataclasses import dataclass
from src.common.types import Vector
import pygame
import sys

screen = pygame.display.set_mode((800, 800))


class PyGameRectangleObject:
    _x: int = 0
    _y: int = 0
    width: int = 0
    height: int = 0

    @property
    def center_x(self):
        return self._x + self.width / 2
    
    @property
    def center_y(self):
        return self._y + self.height / 2
    
    @property
    def coords(self):
        return (self._x, self._y)
    
    @coords.setter
    def coords(self, value: Vector):
        self._x, self._y = value

    @property
    def center_coords(self):
        return (self.center_x, self.center_y)
    
    @center_coords.setter
    def center_coords(self, value: Vector):
        self._x = value[0] - self.width / 2
        self._y = value[1] - self.height / 2
        
    @property
    def top(self):
        return self._y
    
    @property
    def bottom(self):
        return self._y + self.height
    
    @property
    def left(self):
        return self._x
    
    @property
    def right(self):
        return self._x + self.width

@dataclass
class MovementKeys:
    key_up: int
    key_down: int


class Ball:
    def __init__(self, x: int, y: int, radius: float) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = (10, 0)
        self.color = (0, 0, 255)
        self._obj = pygame.Rect(0, 0, 0, 0)

    def draw(self):
        self._obj = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self._obj.move_ip(*self.velocity)
        self.x, self.y = self._obj.centerx, self._obj.centery

    def check_wall_collision(self):
        print(self.top, self.bottom)
        if self.top < 0 or self.bottom > screen.get_height():
            vx, vy = self.velocity
            offset = (self.center_x - screen.get_width() / 2) / (screen.get_width() / 2)
            bounced = (vx, -1 * vy)
            self.velocity = (bounced[0] + offset, bounced[1])


    @property
    def center_x(self):
        return self._obj.centerx
    
    @property
    def center_y(self):
        return self._obj.centery

    @property
    def top(self):
        return self.y - self.radius

    @property
    def bottom(self):
        return self.y + self.radius
    
    @property
    def left(self):
        return self.x + self.radius
    
    @property
    def right(self):
        return self.x - self.radius


class Paddle(PyGameRectangleObject):
    def __init__(self, x: int, y: int, width: int, height: int, keys: MovementKeys) -> None:
        self.width = width
        self.height = height
        self.keys = keys
        self.center_coords = (x, y)
        self.color = (255, 0, 0)
        self.speed = 10
        self._obj = pygame.Rect(self._x, self._y, self.width, self.height)

    def draw(self):
        self._obj = pygame.draw.rect(screen, self.color, self._obj)

    def move(self, x, y):
        if self.top > 0 and y < 0:
            self._obj.move_ip(x, y)
            self.coords = (self._obj.x, self._obj.y)
        if self.bottom < screen.get_height() and y > 0:
            self._obj.move_ip(x, y)
            self.coords = (self._obj.x, self._obj.y)

    def check_collision(self, ball: Ball):
        if self._obj.collidepoint(ball.left, ball.y) or self._obj.collidepoint(ball.right, ball.y):
            vx, vy = ball.velocity
            offset = ((ball.center_y - self.center_y) / (self.height / 2)) * 10
            bounced = (-1 * vx, vy)
            ball.velocity = (bounced[0], bounced[1] + offset)

    def handle_keys(self, keys: dict):
        if keys[self.keys.key_up]:
            self.move(0, -self.speed)
        elif keys[self.keys.key_down]:
            self.move(0, self.speed)


pygame.init()

movement1 = MovementKeys(pygame.K_w, pygame.K_s)
paddle1 = Paddle(0, 400, 25, 200, movement1)

movement2 = MovementKeys(pygame.K_UP, pygame.K_DOWN)
paddle2 = Paddle(800, 400, 25, 200, movement2)

ball = Ball(400, 400, 25)
ball.draw()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    
    keys = pygame.key.get_pressed()
    paddle1.handle_keys(keys)
    paddle2.handle_keys(keys)
    ball.move()
    ball.check_wall_collision()

    paddle1.check_collision(ball)
    paddle2.check_collision(ball)

    screen.fill((0, 0, 0))
    paddle1.draw()
    paddle2.draw()
    ball.draw()

    pygame.display.flip()
    pygame.time.wait(60)
