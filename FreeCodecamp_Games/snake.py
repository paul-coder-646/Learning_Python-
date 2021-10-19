import pygame
pygame.init()
import math
import random
import tkinter as tk
from tkinter import messagebox

# Simple Snake Game
# Base Game from freecodecamp Tech With Tim's Tutorial
# Todo 
# 1) Base Game
# 2) In Game Stats / Score
# 3) Getting Fancy :D
# 4) Colliders and additional obstacles


class cube(object):
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny = 0, color=(255, 0, 0)):
        self.position = start

        # dirnx and dirny are the directions the snake is moving towards...only movement on one axis allowed (1,0);(0,1);(-1,0);(0,-1)
        # 1: positive movement
        # -1: negative movement
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color
    
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.position = (self.position[0] + self.dirnx, self.position[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows

        i = self.position[0]
        j = self.position[1]

        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))

        if eyes:
            centre = dis // 2
            radius = 3
            # depending on what direction the snake is moving, its gaze shifts direction too :D

            if self.dirny == -1: # eyes up
                circleMiddle = (i*dis + 1 + radius*2, j*dis +1 +8)
                circleMiddle2 = (i*dis + 1 + dis -(radius*2+2), j*dis +1 +8)
            elif self.dirny == 1: # eyes down
                circleMiddle = (i*dis + 1 + radius*2, j*dis +1 + dis -10)
                circleMiddle2 = (i*dis + 1 + dis -(radius*2+2), j*dis +1 + dis -10)
            elif self.dirnx == -1: # eyes left
                circleMiddle = (i*dis + 1 + radius*2, j*dis + 1 + radius*2)
                circleMiddle2 = (i*dis + 1 + radius*2, j*dis + 1 + dis -(radius*2+2))
            elif self.dirnx == 1: # eyes right
                circleMiddle = (i*dis +1 + dis -(radius*2 +2), j*dis + 1 + radius*2)
                circleMiddle2 = (i*dis +1 + dis -(radius*2 +2), j*dis + 1 + dis -(radius*2+2))

            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)


class snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.dirnx = -1
                self.dirny = 0
                self.turns[self.head.position[:]] = (self.dirnx, self.dirny)

            elif keys[pygame.K_RIGHT]:
                self.dirnx = 1
                self.dirny = 0
                self.turns[self.head.position[:]] = (self.dirnx, self.dirny)

            elif keys[pygame.K_UP]:
                self.dirnx = 0
                self.dirny = -1
                self.turns[self.head.position[:]] = (self.dirnx, self.dirny)

            elif keys[pygame.K_DOWN]:
                self.dirnx = 0
                self.dirny = 1
                self.turns[self.head.position[:]] = (self.dirnx, self.dirny)
        
        # we need to make sure, that every part of the snake turns at the point where the head first turned, so we save a map of all squares, with 
        # its turns, that should take place at that point 
        for i, c in enumerate(self.body):
            p = c.position[:]

            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])

                # if we are the last body part of the snake we can remove the turn instruction
                if i == len(self.body)-1:
                    self.turns.pop(p)

            else:
                # bounds checking and correctiong
                if c.dirnx == -1 and c.position[0] <= 0: c.position = (c.rows-1, c.position[1])
                elif c.dirnx == 1 and c.position[0] >= c.rows-1: c.position = (0, c.position[1]) 
                elif c.dirny == 1 and c.position[1] >= c.rows-1: c.position = (c.position[0], 2) # y-offset of 2 rows so we account for the scoreboard
                elif c.dirny == -1 and c.position[1] <= 2: c.position = (c.position[0], c.rows-1) # y-offset of 2 rows so we account for the scoreboard
                else: c.move(c.dirnx,c.dirny)

    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        tail = self.body[-1]
        dirnx = tail.dirnx
        dirny = tail.dirny

        # adding cubes to the tail of the snaked
        if dirnx == 1 and dirny == 0:
            self.body.append(cube((tail.position[0]-1, tail.position[1]), dirnx, dirny))
        if dirnx == -1 and dirny == 0:
            self.body.append(cube((tail.position[0]+1, tail.position[1]), dirnx, dirny))
        if dirnx == 0 and dirny == -1:
            self.body.append(cube((tail.position[0], tail.position[1]+1), dirnx, dirny))
        if dirnx == 0 and dirny == 1:
            self.body.append(cube((tail.position[0], tail.position[1]-1), dirnx, dirny))

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True) # draw eyes if its the first block
            else:
                c.draw(surface)



def drawGrid(width, rows, surface):
    sizeBtwn = width // rows

    x = 0
    y = 25 # we don't start from 0 to make space for the scoreboard, and 5 is offset as we need to alighn the Block with the gridlines :)
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        # draw lines on the surface to divide into squaresds
        pygame.draw.line(surface, (255,255,255), (x, 44), (x, width)) # draw vertical gridline
        pygame.draw.line(surface, (255,255,255), (0, y), (width+25, y)) # draw horizontal gridline

def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill((0,0,0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    show_score(len(s.body), 175, 5, surface)
    pygame.display.update()
    

def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(2,rows)

        # basically check if in the list of positions of the snake body, any of them are the same as our random snake location
        # thereby prevents weird behavior (spawning snacks on snake :) )
        if len(list(filter(lambda z:z.position == (x,y), positions))) > 0:
            continue
        else:
            break
    
    return (x,y)

score_value = 0
font = pygame.font.Font('/Users/waverider/Desktop/Programming/Python-Projects/Learning/FreeCodecamp_Games/dcandles .ttf', 20)
def show_score(s, x, y, screen):
    global score_value
    score_value = s
    score = font.render(f"Your Score: {str(score_value)}", True, (255, 255, 255))
    screen.blit(score, (x, y))



#This seems to be having problems on macos 
''' 
def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass
    '''

def main():
    global width, rows, s, snack

    width = 500
    rows = 20

    # initializes a 500x500 window
    win = pygame.display.set_mode((width, width))
    flag = True
    clock = pygame.time.Clock()

    s = snake((255, 0, 0), (10,10))
    snack = cube(start=randomSnack(rows, s), color=(0, 255, 0))

    while flag:

        pygame.time.delay(100)
        clock.tick(10)
        s.move()

        if s.body[0].position == snack.position:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(0, 255, 0))


        for x in range(len(s.body)):
            if s.body[x].position in list(map(lambda z:z.position, s.body[x+1:])):
                # message_box('You lost', 'Play again :)')
                print(f'Sorry, you lost with a score of {len(s.body)} but you can try again :D')
                s.reset((10, 10))
                break

        redrawWindow(win)

        # if we press the (x) Button to close the window, then it should close 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False

main()