import sys
import pygame
import numpy as np

pygame.init()

CELL_SIZE = 16
GRID_SIZE = 32
WINDOW_SIZE = CELL_SIZE * GRID_SIZE

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Linear Regression Playground")
clock = pygame.time.Clock()

COLOR_BACKGROUND = (15, 15, 15)
COLOR_GRID_LINE = (35, 35, 35)
COLOR_DOT = (0, 255, 128)
COLOR_LINE = (255, 100, 100)

data_points = np.array([
    [2, 3],
    [5, 7],
    [9, 11],
    [13, 16],
    [17, 21],
    [21, 25],
    [26, 29]
])

# linear regression calculation
sum_of_x = 0;
sum_of_y = 0;
for value in data_points:
    sum_of_x += value[0]
    sum_of_y += value[1]
mean_of_x = sum_of_x / len(data_points)
mean_of_y = sum_of_y / len(data_points)

a = 0
b = 0
for value in data_points:
   a += (value[0] - mean_of_x)*(value[1] - mean_of_y)

for value in data_points:
   b +=  (value[0] - mean_of_x) ** 2

m = a / b # m is slope (rate of change)
intercept = mean_of_y - (m * mean_of_x)

# origo perspective: y = 0 at bottom
def world_to_screen(x, y):
    return int(x * CELL_SIZE), int(WINDOW_SIZE - (y * CELL_SIZE))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill(COLOR_BACKGROUND)

    for i in range(GRID_SIZE):
        pygame.draw.line(screen, COLOR_GRID_LINE, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE), 1)
        pygame.draw.line(screen, COLOR_GRID_LINE, (0, i * CELL_SIZE), (WINDOW_SIZE, i * CELL_SIZE), 1)

    x_start, x_end = 0, GRID_SIZE
    y_start = m * x_start + intercept
    y_end = m * x_end + intercept
    
    p1 = world_to_screen(x_start, y_start)
    p2 = world_to_screen(x_end, y_end)
    pygame.draw.line(screen, COLOR_LINE, p1, p2, 3)

    for point in data_points:
        screen_x, screen_y = world_to_screen(point[0], point[1])
        pygame.draw.circle(screen, COLOR_DOT, (screen_x, screen_y), 6, width=0)

    pygame.display.flip()
    clock.tick(60)