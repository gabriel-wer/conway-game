#!/usr/bin/env python

import random 
import pygame

CELLSIZE = 20
ROWS = 30
COLUMNS = 30

def draw_map(i, j, canvas):
    if arr[i][j] == 1:
        pygame.draw.rect(canvas, (0,255,0),
                         pygame.Rect(i*CELLSIZE, j*CELLSIZE, CELLSIZE-2, CELLSIZE-2))

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
canvas = pygame.display.set_mode(((CELLSIZE *  COLUMNS), (CELLSIZE * ROWS)))
pygame.display.set_caption("Conway's Game of Life")

#populates array with values from 0-1
arr = [[random.randint(0,1) for _ in range(ROWS)] for _ in range(COLUMNS)]
print(arr)

clock = pygame.time.Clock()
running = True
while running:
    canvas.fill((0,0,0))
    clock.tick(10)
    for i, _ in enumerate(arr):
        for j, c in enumerate(arr[i]):
            arr[i][j] = detect_collision(arr, i, j, c)
            draw_map(i, j, canvas)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False 
