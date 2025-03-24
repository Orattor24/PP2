import pygame
import random
from color_palette import *

pygame.init()
#Размер окна
WIDTH = 600
HEIGHT = 600
#Сам экран
screen = pygame.display.set_mode((HEIGHT, WIDTH))
#Размер клеток
CELL = 30
#Делаем шахматную доску
def draw_grid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"
#Змея
class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13), Point(10, 14), Point(10, 15)]
        self.dx, self.dy = 1, 0
        self.score, self.level = 0, 1

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x, self.body[i].y = self.body[i - 1].x, self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        if self.check_collision_with_self() or self.check_wall_collision():
            pygame.quit()
            quit()

    def draw(self):
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision_with_self(self):
        head = self.body[0]
        return any(segment.x == head.x and segment.y == head.y for segment in self.body[1:])

    def check_wall_collision(self):
        head = self.body[0]
        return head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL

    def check_collision(self, food):
        if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
            self.body.append(Point(self.body[-1].x, self.body[-1].y))
            self.score += 1
            food.generate_new_position(self)
            if self.score % 3 == 0:
                self.level += 1
                return True
        return False
#Еда
class Food:
    def __init__(self):
        #Позиция. Рандом нужен для создания случайной клетки , наверное
        self.pos = Point(random.randint(0,19), random.randint(0,19))

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    #Создание совсем нвоого фрукта после того как его схватили
    def generate_new_position(self, snake):
        while True:
            new_x = random.randint(0, WIDTH // CELL - 1)
            new_y = random.randint(0, HEIGHT // CELL - 1)
            # Проверка, чтобы еда не появилась на змейке
            if not any(segment.x == new_x and segment.y == new_y for segment in snake.body):
                self.pos = Point(new_x, new_y)
                break

FPS = 5
clock = pygame.time.Clock()

food = Food()
snake = Snake()

running = True
while running:
    #события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1
    #отрисовка карты
    draw_grid_chess()
    #логика основная
    snake.move()
    snake.check_collision(food)
    if snake.check_collision(food):
        FPS += 1
    #отрисовка змеи
    snake.draw()
    food.draw()
    #текст
    font = pygame.font.SysFont("Verdana", 20)
    score_text = font.render(f"Score: {snake.score}", True, colorBLACK)
    level_text = font.render(f"Level: {snake.level}", True, colorBLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()