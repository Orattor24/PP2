import pygame
import random
import time
import psycopg2
from config import load_config
from color_palette import *

pygame.init()

# Размер окна
WIDTH = 600
HEIGHT = 600

# Экран
screen = pygame.display.set_mode((WIDTH, HEIGHT))
CELL = 30
pygame.display.set_caption("Snake Game")

def get_user(username):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM users WHERE username = %s", (username,))
            result = cur.fetchone()
            if result:
                user_id = result[0]
                cur.execute("SELECT score, level FROM user_scores WHERE user_id = %s", (user_id,))
                score_data = cur.fetchone()
                if score_data:
                    return user_id, 0, 1  # Начинаем заново
                else:
                    cur.execute("INSERT INTO user_scores (user_id, score, level) VALUES (%s, 0, 1)", (user_id,))
                    conn.commit()
                    return user_id, 0, 1
            else:
                cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
                user_id = cur.fetchone()[0]
                cur.execute("INSERT INTO user_scores (user_id, score, level) VALUES (%s, 0, 1)", (user_id,))
                conn.commit()
                return user_id, 0, 1

def save_score(user_id, score, level):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT score, level FROM user_scores WHERE user_id = %s", (user_id,))
            current = cur.fetchone()
            if current:
                current_score, current_level = current
                if score > current_score or (score == current_score and level > current_level):
                    cur.execute("UPDATE user_scores SET score = %s, level = %s WHERE user_id = %s", (score, level, user_id))
                    conn.commit()
            else:
                cur.execute("INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
                conn.commit()

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (j * CELL, i * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self, score=0, level=1):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13), Point(10, 14), Point(10, 15)]
        self.dx, self.dy = 1, 0
        self.score, self.level = score, level
        self.eat = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy
        return self.check_collision_with_self() or self.check_wall_collision()


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
            if food.kind == "normal":
                self.score += 1
                growth = 1
            elif food.kind == "bonus":
                self.score += 2
                growth = 2

            self.eat += 1
            for _ in range(growth):
                self.body.append(Point(self.body[-1].x, self.body[-1].y))

            food.generate_new_position(self)
            return True
        return False
class Wall:
    def __init__(self):
        self.pos = None

    def generate_new_position(self, snake, food, walls):
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            if not any(segment.x == x and segment.y == y for segment in snake.body) and \
               not (food.pos.x == x and food.pos.y == y) and \
               not any(w.pos.x == x and w.pos.y == y for w in walls):
                self.pos = Point(x, y)
                break

    def draw(self):
        pygame.draw.rect(screen, colorBLACK, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

class Food:
    def __init__(self, kind="normal"):
        self.kind = kind
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
        self.timer = time.time() + random.randint(5, 10)

    def draw(self):
        color = colorGREEN if self.kind == "normal" else colorORANGE
        pygame.draw.rect(screen, color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_new_position(self, snake):
        while True:
            new_x = random.randint(0, WIDTH // CELL - 1)
            new_y = random.randint(0, HEIGHT // CELL - 1)
            if not any(segment.x == new_x and segment.y == new_y for segment in snake.body):
                self.pos = Point(new_x, new_y)
                self.timer = time.time() + random.randint(5, 10)
                break

# Инициализация
username = input("Введите имя пользователя: ")
user_id, score, level = get_user(username)
snake = Snake(score=score, level=level)
FPS = 5
clock = pygame.time.Clock()
food = Food("normal")
bonus_food = None
paused = False
walls = []
current_level = snake.level  # Чтобы отслеживать смену уровня

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_score(user_id, snake.score, snake.level)
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
                if paused:
                    save_score(user_id, snake.score, snake.level)
            if not paused:
                if event.key == pygame.K_d:
                    snake.dx, snake.dy = 1, 0
                elif event.key == pygame.K_a:
                    snake.dx, snake.dy = -1, 0
                elif event.key == pygame.K_s:
                    snake.dx, snake.dy = 0, 1
                elif event.key == pygame.K_w:
                    snake.dx, snake.dy = 0, -1

    if not paused:
        game_over = snake.move()
        for wall in walls:
            if snake.body[0].x == wall.pos.x and snake.body[0].y == wall.pos.y:
                game_over = True
                break
        if game_over:
            print("Game Over")
            save_score(user_id, snake.score, snake.level)
            running = False
            continue

        # Появление бонусной еды на 2 уровне
        if snake.level >= 2 and bonus_food is None:
            bonus_food = Food("bonus")

        if snake.level > current_level:
            current_level = snake.level
            wall = Wall()
            wall.generate_new_position(snake, food, walls)
            walls.append(wall)

        if snake.check_collision(food):
            snake.level = 1 + snake.score // 5
            FPS = 5 + (snake.level - 1)

        if bonus_food and snake.check_collision(bonus_food):
            snake.level = 1 + snake.score // 5
            FPS = 5 + (snake.level - 1)

        if time.time() > food.timer:
            food.generate_new_position(snake)
        if bonus_food and time.time() > bonus_food.timer:
            bonus_food.generate_new_position(snake)

        draw_grid_chess()
        snake.draw()
        food.draw()
        for wall in walls:
            wall.draw()

        if bonus_food:
            bonus_food.draw()

        font = pygame.font.SysFont("Verdana", 20)
        score_text = font.render(f"Score: {snake.score}", True, colorBLACK)
        level_text = font.render(f"Level: {snake.level}", True, colorBLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 40))
        pygame.display.flip()
        clock.tick(FPS)

pygame.quit()
