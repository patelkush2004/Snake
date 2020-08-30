import pygame
import time
import random

pygame.init()

# Creates Global Variables for each colour
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Set display size
dis_width = 600
dis = pygame.display.set_mode((dis_width, dis_width))
pygame.display.set_caption('Play Snake')

timer = pygame.time.Clock()

SnakeBlock = 10
SnakeSpeed = 15

# Font for score and quit prompt
font_style = pygame.font.SysFont("centurygothic", 16)
score_label = pygame.font.SysFont("centurygothic", 16)

# Score label at the bottom of display
def Score(score):
    label = score_label.render("Your Score: " + str(score), True, white)
    dis.blit(label, [260, 560])

# Creates the snake
def our_snake(SnakeBlock, SnakeList):
    for x in SnakeList:
        pygame.draw.rect(dis, green, [x[0], x[1], SnakeBlock, SnakeBlock])

# End game message
def message(msg, color):
    msg = font_style.render(msg, True, color)
    dis.blit(msg, [dis_width / 6, dis_width / 3])


def gameLoop():
    GameOver = False
    GameClose = False

    x_ = dis_width / 2
    y_ = dis_width / 2

    x_change = 0
    y_change = 0

    SnakeList = []
    SnakeLength = 1

    foodx = round(random.randrange(0, dis_width - SnakeBlock) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - SnakeBlock) / 10.0) * 10.0

    while not GameOver:

        while GameClose == True:
            dis.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Score(SnakeLength - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        GameOver = True
                        GameClose = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -SnakeBlock
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = SnakeBlock
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -SnakeBlock
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = SnakeBlock
                    x_change = 0

        if x_ >= dis_width or x_ < 0 or y_ >= dis_width or y_ < 0:
            GameClose = True
        x_ += x_change
        y_ += y_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, SnakeBlock, SnakeBlock])
        snakeHead = []
        snakeHead.append(x_)
        snakeHead.append(y_)
        SnakeList.append(snakeHead)
        if len(SnakeList) > SnakeLength:
            del SnakeList[0]

        for x in SnakeList[:-1]:
            if x == snakeHead:
                GameClose = True

        our_snake(SnakeBlock, SnakeList)
        Score(SnakeLength - 1)

        pygame.display.update()

        if x_ == foodx and y_ == foody:
            foodx = round(random.randrange(0, dis_width - SnakeBlock) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_width - SnakeBlock) / 10.0) * 10.0
            SnakeLength += 1

        timer.tick(SnakeSpeed)

    pygame.quit()
    quit()


gameLoop()