import pygame
import random
import time

pygame.init()

# Размеры окон, скорость и сколько очков
WIDTH, HEIGHT = 400, 600
PLAYER_SPEED = 5
ENEMY_SPEED = 5
MONEY_SPEED = 5
FPS = 60
SCORE = 0

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game")

# Загрузка ресурсов
background = pygame.image.load('resources/AnimatedStreet.png')
player_img = pygame.image.load('resources/Player.png')
enemy_img = pygame.image.load('resources/Enemy.png')
money_img = pygame.image.load('resources/Coin.png')
background_music = pygame.mixer.music.load('resources/background.wav')
crash_sound = pygame.mixer.Sound('resources/crash.wav')

# Настройки текста
font = pygame.font.SysFont("Verdana", 30)
game_over_text = font.render("Game Over", True, "black")

# Включаем фоновую музыку
pygame.mixer.music.play(-1)


# Классы
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img #Фотка
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 10))

    #Чтобы двигалось на кнопки жать всякие
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += PLAYER_SPEED

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect(midtop=(random.randint(40, WIDTH - 40), 0))

    def move(self):
        self.rect.y += ENEMY_SPEED
        if self.rect.top > HEIGHT: #Если высота больше размера окна, то создаем новую копию рандомно с 0 координат
            self.rect.midtop = (random.randint(40, WIDTH - 40), 0)



class Money(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = money_img
        self.rect = self.image.get_rect(midtop=(random.randint(40, WIDTH - 40), 0))

    def move(self):
        self.rect.y += MONEY_SPEED
        if self.rect.top > HEIGHT:
            self.reset_position()

    def reset_position(self):
        self.rect.midtop = (random.randint(40, WIDTH - 40), 0)


# Создание объектов
player = Player()
enemy = Enemy()
money = Money()

# Группы спрайтов
all_sprites = pygame.sprite.Group(player, enemy, money)
enemy_sprites = pygame.sprite.Group(enemy)
money_sprites = pygame.sprite.Group(money)

# Игровой цикл
clock = pygame.time.Clock()
running = True
#Основная часть
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Движение
    player.move()
    enemy.move()
    money.move()

    # Отрисовка спрайтов
    all_sprites.draw(screen)

    # Проверка столкновений
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        crash_sound.play()
        time.sleep(1)
        screen.fill("red")
        screen.blit(game_over_text, game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        pygame.display.flip()
        time.sleep(2)
        running = False

    if pygame.sprite.spritecollideany(player, money_sprites):
        SCORE += 1
        print(f"Score: {SCORE}")
        money.reset_position()
    if pygame.sprite.spritecollideany(enemy, money_sprites):
        money.reset_position()

    # Отображение счета
    score_text = font.render(f"Score: {SCORE}", True, "black")
    screen.blit(score_text, (250, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
