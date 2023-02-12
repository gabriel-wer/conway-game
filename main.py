#!/usr/bin/env python

import random 
import pygame

SIZE_X = 20
SIZE_Y = 20
ROWS = 20
COLUMNS = 20

def draw_map(arr, canvas):
    for i, _ in enumerate(arr):
        for j, _ in enumerate(arr[i]):
            if arr[i][j] == 1:
                pygame.draw.rect(canvas, (0,255,0),
                                 pygame.Rect(j*ROWS, i*COLUMNS, SIZE_X, SIZE_Y))

def calculate(neigh, c):
    if neigh < 2:
        return 0
    if c == 1 and neigh == 2:
        return 1
    if c == 0 and neigh == 2:
        return 0
    if neigh == 3:
        return 1
    if neigh >= 3:
        return 0

def detect_collision(arr, i, j, c):
    count = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            try:
                if arr[x][y] == 1:
                    count += 1
                    continue
            except IndexError:
                pass
    if c == 1:
        count -= 1
    return calculate(count, c)




pygame.init()
canvas = pygame.display.set_mode((ROWS*SIZE_X, COLUMNS*SIZE_Y))
pygame.display.set_caption("Conway's Game of Life")

#populates array with values from 0-1
arr = [[random.randint(0,1) for _ in range(ROWS)] for _ in range(COLUMNS)]


clock = pygame.time.Clock()
running = True
while running:
    draw_map(arr, canvas)
    canvas.fill((0,0,0))
    for i, _ in enumerate(arr):
        for j, c in enumerate(arr[i]):
            arr[i][j] = detect_collision(arr, i, j, c)
            draw_map(arr, canvas)
            pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


"""
[[0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
 [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1],
 [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
 [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
 [0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0],
 [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1],
 [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
 [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
 [0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0],
 [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1],
 [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
 [1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0],
 [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
 [1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
 [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
 [0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1],
 [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
 [1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1],
 [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0],
 [0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0]]

"""
