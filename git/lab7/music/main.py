import pygame

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

songs = [
    "music/Black Veil Brides - Ritual.mp3",
    "music/Black Veil Brides - In The End.mp3",
    "music/Ramones - Blitzkrieg Bop (Mono Version) [Single Version].mp3"
]
current_song = 0

pygame.mixer.music.load(songs[current_song])
pygame.mixer.music.play(-1)

running = True
play = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if play:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                play = not play
            elif event.key == pygame.K_LEFT:
                current_song = (current_song - 1) % len(songs)
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play(-1)
            elif event.key == pygame.K_RIGHT:
                current_song = (current_song + 1) % len(songs)
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play(-1)

    pygame.display.flip()

pygame.quit()
