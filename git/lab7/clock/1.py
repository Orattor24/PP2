import pygame
import time


pygame.init()

screen = pygame.display.set_mode((800, 600))

done = False

clock = pygame.time.Clock()

clock_image = pygame.image.load("clock.png")
min_hand_image = pygame.image.load("min_hand.png")
sec_hand_image = pygame.image.load("sec_hand.png")

rect_clock = screen.get_rect()
rect_clock.center = screen.get_rect().center

while not done:
    screen.fill((255,255,255))
    screen.blit(clock_image, rect_clock)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    nastoyashee_vrema = time.localtime()
    sec_angle = -(nastoyashee_vrema.tm_sec * 360 / 60)
    min_angle = -(nastoyashee_vrema.tm_min * 360 / 60)


    sec_hand = pygame.transform.rotate(sec_hand_image, sec_angle)
    min_hand = pygame.transform.rotate(min_hand_image, min_angle)

    rect_sec = sec_hand.get_rect()
    rect_sec.center = screen.get_rect().center
    screen.blit(sec_hand, rect_sec)

    rect_min = min_hand.get_rect()
    rect_min.center = screen.get_rect().center
    screen.blit(min_hand, rect_min)




    pygame.display.flip()
    clock.tick(60)