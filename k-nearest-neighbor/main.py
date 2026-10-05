import numpy as np
import pygame
pygame.font.init()

def euclidian_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# create random points, chance of point being unclassified
def create_random_points(num_points):
    points = []
    for _ in range(num_points):
        x = np.random.rand()
        y = np.random.rand()
        color = -1

        chance_of_being_unclassified = np.random.rand()
        if chance_of_being_unclassified < 0.2:
            color = -1 # set as unclassified

        # for easier visualization, we can make the points to red or blue
        # based on their x position
        elif x < 0.5:
            color = 0 # team red
        elif x >= 0.5:
            color = 1 # team blue
        points.append([x*10, y*10, color])
    return points

def find_k_nearest_neighbors(point, points, k):
    distances = []
    for p in points:
        if p[2] != -1:  # only consider classified points
            dist = euclidian_distance(point[0], point[1], p[0], p[1])
            distances.append((dist, p))
    distances.sort(key=lambda x: x[0])
    return [p for _, p in distances[:k]]

def classify_all_points(points):
    new_classes = {}
    for i, point in enumerate(points):
        if point[2] == -1:
            neighbors = find_k_nearest_neighbors(point, points, k)
            red_count = sum(1 for n in neighbors if n[2] == 0)
            blue_count = sum(1 for n in neighbors if n[2] == 1)
            new_classes[i] = 0 if red_count > blue_count else 1
            
    for i, new_color in new_classes.items():
        points[i][2] = new_color

starting_points = create_random_points(50)
k = 5 # number of neighbors to consider

WINDOW_SIZE = 512
COLOR_BACKGROUND = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_UNCLASSIFIED = (100, 100, 100)
view_state = "unclassified"

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("K-Nearest Neighbors Algorithm Visualization")
clock = pygame.time.Clock()

# main loop, toggle between unclassified and classified view with spacebar, reset with r
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if view_state == "unclassified":
                    classify_all_points(starting_points)
                    view_state = "classified"
            elif event.key == pygame.K_r:
                starting_points = create_random_points(50)
                view_state = "unclassified"
    screen.fill(COLOR_BACKGROUND)

    for point in starting_points:
        color = COLOR_UNCLASSIFIED
        if point[2] == 0:
            color = COLOR_RED
        elif point[2] == 1:
            color = COLOR_BLUE
        pygame.draw.circle(screen, color, (int(point[0] * 50), int(point[1] * 50)), 10)

    font = pygame.font.SysFont("Arial", 18)
    text_surface = font.render("UNCLASSIFIED: GRAY, press SPACE to classify", True, (0, 0, 0))
    screen.blit(text_surface, (10, 10))
    pygame.display.flip()
    clock.tick(60)