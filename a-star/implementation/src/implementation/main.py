import sys
import pygame
import random
import numpy as np
import heapq

pygame.init()

# helpers
# calculate Manhattan distance between two points
def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# reconstruct the path from start to end using parent pointers
def reconstruct_path(parent, current):
    path = [current]
    while current in parent:
        current = parent[current]
        path.append(current)
    return path[::-1] # Return reversed path (start to end)

# initialize graphics & drawing
CELL_SIZE = 32
GRID_SIZE = 10
WINDOW_SIZE = CELL_SIZE * GRID_SIZE

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("A* algorithm implementation")
clock = pygame.time.Clock()

COLOR_BACKGROUND = (0, 0, 0) # black
COLOR_GRID_LINE = (255, 255, 255) # white
COLOR_START_DOT = (255, 0, 0) # red
COLOR_END_DOT = (0, 255, 0) # green
COLOR_PATH_NODE = (0, 0, 255) # blue
COLOR_PATH_LINE = (255, 255, 0) # yellow
COLOR_OBSTACLE = (128, 128, 128) # gray

NEIGHBOR_OFFSETS = [
    (0, -1),  # up
    (0, 1),   # down
    (1, 0),   # right
    (-1, 0)   # left
]

# start and end points
start = (0, 0)
end = (GRID_SIZE - 1, GRID_SIZE - 1)

# create random obstacles
obstacles = np.zeros((GRID_SIZE, GRID_SIZE), dtype=bool)

for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        if random.random() < 0.2: # 20% chance of obstacle
            obstacles[i, j] = True
obstacles[start] = False
obstacles[end] = False



# f = total estimated cost (g + h)
f = np.full((GRID_SIZE, GRID_SIZE), np.inf)
f[start] = manhattan_distance(start, end)

# g = cost so far
g = np.full((GRID_SIZE, GRID_SIZE), np.inf)
g[start] = 0

# --- TRACKING STRUCTURES ---
# OPEN list as a priority queue (min-heap): stores tuples of (f_score, (x, y))
open_heap = []
heapq.heappush(open_heap, (f[start], start))

# Track visited nodes (CLOSED list) and parent pointers to reconstruct the final path
closed_set = set()
parent = {}
path_found = False

while open_heap:
    current_f, q = heapq.heappop(open_heap)

    if q in closed_set:
        continue

    if q == end:
        print("Goal reached!")
        final_path = reconstruct_path(parent, q)
        path_found = True
        break

    closed_set.add(q)

    qx, qy = q
    for dx, dy in NEIGHBOR_OFFSETS:
        nx, ny = qx + dx, qy + dy
        neighbor = (nx, ny)
        step_cost = 1

        # check if neighbor is within bounds and not an obstacle
        if not (0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE):
            continue
        if obstacles[nx, ny]:
            continue

        # check if neighbor is already in closed set
        if neighbor in closed_set:
            continue

        
        tentative_g = g[q] + step_cost

        if tentative_g < g[neighbor]:
            parent[neighbor] = q
            g[neighbor] = tentative_g
            f[neighbor] = tentative_g + manhattan_distance(neighbor, end)

            # Push updated node to OPEN list
            heapq.heappush(open_heap, (f[neighbor], neighbor))

if not path_found:
    print("No path found to goal.")

# main graphics loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(COLOR_BACKGROUND)

    # draw grid
    for i in range(GRID_SIZE):
        pygame.draw.line(screen, COLOR_GRID_LINE, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE), 1)
        pygame.draw.line(screen, COLOR_GRID_LINE, (0, i * CELL_SIZE), (WINDOW_SIZE, i * CELL_SIZE), 1)

    # draw obstacles
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if obstacles[i, j]:
                pygame.draw.rect(screen, COLOR_OBSTACLE, (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # draw start and end points
    pygame.draw.circle(screen, COLOR_START_DOT, (start[0] * CELL_SIZE + CELL_SIZE // 2, start[1] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)
    pygame.draw.circle(screen, COLOR_END_DOT, (end[0] * CELL_SIZE + CELL_SIZE // 2, end[1] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)

    # draw lines to path and circles(nodes) on turning points if found
    if path_found:
        for i in range(len(final_path) - 1):
            x1, y1 = final_path[i]
            x2, y2 = final_path[i + 1]
            pygame.draw.line(screen, COLOR_PATH_LINE, (x1 * CELL_SIZE + CELL_SIZE // 2, y1 * CELL_SIZE + CELL_SIZE // 2), (x2 * CELL_SIZE + CELL_SIZE // 2, y2 * CELL_SIZE + CELL_SIZE // 2), 3)
            pygame.draw.circle(screen, COLOR_PATH_NODE, (x1 * CELL_SIZE + CELL_SIZE // 2, y1 * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 4)

    pygame.display.flip()
    clock.tick(60)