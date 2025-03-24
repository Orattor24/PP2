import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

brush_size = 10
DRAWING_COLOR = (0, 0, 0)
clock = pygame.time.Clock()

drawing = False
last_pos = (0, 0)
shape = 'line'
lines = []
rectangles = []
circles = []
temp_rectangle = None
temp_circle = None
start_pos = None

color_palette = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (0, 0, 0),  # Black
    (255, 0, 255),  # Magenta
    (0, 255, 255)  # Cyan
]
color_index = 0


def draw_objects():
    screen.fill(BACKGROUND_COLOR)
    for rectangle in rectangles:
        pygame.draw.rect(screen, rectangle[1], rectangle[0], rectangle[2])
    for circle in circles:
        pygame.draw.circle(screen, circle[1], circle[0][0], circle[0][1], circle[2])
    for line in lines:
        pygame.draw.line(screen, line[2], line[0], line[1], line[3])
    if temp_rectangle:
        pygame.draw.rect(screen, DRAWING_COLOR, temp_rectangle, brush_size)
    if temp_circle:
        pygame.draw.circle(screen, DRAWING_COLOR, temp_circle[0], int(temp_circle[1]), brush_size)
    pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if shape == 'rectangle' and temp_rectangle:
                rectangles.append((temp_rectangle, DRAWING_COLOR, brush_size))
                temp_rectangle = None
            elif shape == 'circle' and temp_circle:
                circles.append(((temp_circle[0], int(temp_circle[1])), DRAWING_COLOR, brush_size))
                temp_circle = None

        elif event.type == pygame.MOUSEMOTION and drawing:
            if shape == 'line':
                lines.append((last_pos, event.pos, DRAWING_COLOR, brush_size))
            elif shape == 'erase':
                lines.append((last_pos, event.pos, BACKGROUND_COLOR, brush_size))
            elif shape == 'rectangle':
                temp_rectangle = (
                min(start_pos[0], event.pos[0]), min(start_pos[1], event.pos[1]), abs(event.pos[0] - start_pos[0]),
                abs(event.pos[1] - start_pos[1]))
            elif shape == 'circle':
                radius = ((event.pos[0] - start_pos[0]) ** 2 + (event.pos[1] - start_pos[1]) ** 2) ** 0.5
                temp_circle = (start_pos, radius)
            last_pos = event.pos

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                shape = 'erase'
            elif event.key == pygame.K_r:
                shape = 'rectangle'
            elif event.key == pygame.K_c:
                shape = 'circle'
            elif event.key == pygame.K_l:
                shape = 'line'
            elif event.key == pygame.K_1:
                color_index = 0
                DRAWING_COLOR = color_palette[color_index]
            elif event.key == pygame.K_2:
                color_index = 1
                DRAWING_COLOR = color_palette[color_index]
            elif event.key == pygame.K_3:
                color_index = 2
                DRAWING_COLOR = color_palette[color_index]
            elif event.key == pygame.K_4:
                color_index = 3
                DRAWING_COLOR = color_palette[color_index]
            elif event.key == pygame.K_5:
                color_index = 4
                DRAWING_COLOR = color_palette[color_index]
            elif event.key == pygame.K_6:
                color_index = 5
                DRAWING_COLOR = color_palette[color_index]
            elif event.key == pygame.K_o:
                brush_size += 1
                if brush_size > 50:
                    brush_size = 50
            elif event.key == pygame.K_p:
                brush_size -= 1
                if brush_size < 1:
                    brush_size = 1

    draw_objects()
    clock.tick(60)