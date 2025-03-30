import pygame


def cool_rec(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x1 - x2)
    h = abs(y1 - y2)
    return (x, y, w, h)


def coolest_rec(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x1 - x2)
    h = abs(y1 - y2)
    z = min(w, h)
    return (x, y, z, z)


def right_tri(x1, y1, x2, y2):
    xS = min(x1, x2)
    xE = max(x1, x2)
    yS = min(y1, y2)
    yE = max(y1, y2)
    pygame.draw.line(screen, colors[index], (xS, yS), (xS, yE), 1)
    pygame.draw.line(screen, colors[index], (xS, yE), (xE, yE), 1)
    pygame.draw.line(screen, colors[index], (xE, yE), (xS, yS), 1)


def equilateral_triangle(x1, y1, x2, y2):
    xS = min(x1, x2)
    yS = min(y1, y2)
    w = abs(x1 - x2)
    h = abs(y1 - y2)
    z = min(w, h)
    xE = xS + z
    yE = yS + z
    pygame.draw.line(screen, colors[index], (xS + 0.5 * z, yS), (xE, yE), 1)
    pygame.draw.line(screen, colors[index], (xE, yE), (xS, yE), 1)
    pygame.draw.line(screen, colors[index], (xS, yE), (xS + 0.5 * z, yS), 1)


def rhombus(x1, y1, x2, y2):
    xS = min(x1, x2)
    xE = max(x1, x2)
    yS = min(y1, y2)
    yE = max(y1, y2)
    xM = (xE + xS) / 2
    yM = (yE + yS) / 2
    pygame.draw.line(screen, colors[index], (xM, yS), (xE, yM), 1)
    pygame.draw.line(screen, colors[index], (xE, yM), (xM, yE), 1)
    pygame.draw.line(screen, colors[index], (xM, yE), (xS, yM), 1)
    pygame.draw.line(screen, colors[index], (xS, yM), (xM, yS), 1)


pygame.init()
screen = pygame.display.set_mode((800, 600))
second_screen = pygame.Surface((800, 600))

done = False
clock = pygame.time.Clock()
Fps = 8
xStart = 10
yStart = 10
xEnd = 10
yEnd = 10
index = 0
index2 = 0
MouseMoving = False

screen.fill((0, 0, 0))

colors = ["Red", "Orange", "Blue", "White", "Green", "Yellow", "Brown"]
tools = ["Rectangle", "Circle", "Square", "Right Triangle", "Equilateral triangle", "Rhombus", "Eraser"]

font = pygame.font.SysFont("comicsansms", 20)
txt = str("Color: " + str(colors[index]))
text = font.render(txt, True, "Magenta")

txt2 = str("Tool: " + str(tools[index2]))
text2 = font.render(txt2, True, "Magenta")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Fps = 60
                if (index2 == 6):
                    xStart = event.pos[0]
                    yStart = event.pos[1]
                    xEnd = xStart
                    yEnd = yStart
                if (index2 == 0 or index2 == 1 or index2 == 2 or index2 == 3 or index2 == 4 or index2 == 5):
                    xStart = event.pos[0]
                    yStart = event.pos[1]
                MouseMoving = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                Fps = 60
                second_screen.blit(screen, (0, 0))
                MouseMoving = False

        if event.type == pygame.MOUSEMOTION:
            if (MouseMoving == True):
                Fps = 60
                if (index2 == 6):
                    xStart = xEnd
                    yStart = yEnd
                    xEnd = event.pos[0]
                    yEnd = event.pos[1]
                if (index2 == 0 or index2 == 1 or index2 == 2 or index2 == 3 or index2 == 4 or index2 == 5):
                    xEnd = event.pos[0]
                    yEnd = event.pos[1]
                    screen.blit(second_screen, (0, 0))
                if (index2 == 0):
                    pygame.draw.rect(screen, colors[index], pygame.Rect(cool_rec(xStart, yStart, xEnd, yEnd)), 1)
                if (index2 == 1):
                    pygame.draw.ellipse(screen, colors[index], pygame.Rect(cool_rec(xStart, yStart, xEnd, yEnd)), 1)
                if (index2 == 2):
                    pygame.draw.rect(screen, colors[index], pygame.Rect(coolest_rec(xStart, yStart, xEnd, yEnd)), 1)
                if (index2 == 3):
                    right_tri(xStart, yStart, xEnd, yEnd)
                if (index2 == 4):
                    equilateral_triangle(xStart, yStart, xEnd, yEnd)
                if (index2 == 5):
                    rhombus(xStart, yStart, xEnd, yEnd)
                if (index2 == 6):
                    pygame.draw.line(screen, "Black", (xStart, yStart), (xEnd, yEnd), 7)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        Fps = 7
        index += 1
        if (index == (len(colors))):
            index = 0
        txt = str("Color: " + str(colors[index]))
        text = font.render(txt, True, "Magenta")

    if pressed[pygame.K_LEFT]:
        Fps = 7
        index -= 1
        if (index == -1):
            index = (len(colors) - 1)
        txt = str("Color: " + str(colors[index]))
        text = font.render(txt, True, "Magenta")

    if pressed[pygame.K_UP]:
        Fps = 7
        index2 += 1
        if (index2 == (len(tools))):
            index2 = 0
        txt2 = str("Tool: " + str(tools[index2]))
        text2 = font.render(txt2, True, "Magenta")

    if pressed[pygame.K_DOWN]:
        Fps = 7
        index2 -= 1
        if (index2 == -1):
            index2 = (len(tools) - 1)
        txt2 = str("Tool: " + str(tools[index2]))
        text2 = font.render(txt2, True, "Magenta")

    pygame.draw.rect(screen, "White", (0, 0, 800, 30))
    screen.blit(text, (1, 1))
    screen.blit(text2, (201, 1))
    pygame.display.flip()
    clock.tick(Fps)