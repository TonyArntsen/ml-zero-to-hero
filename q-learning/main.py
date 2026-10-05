import pygame
import random

WINDOW_SIZE = 512
CELL_SIZE = 32
GRID_SIZE = WINDOW_SIZE // CELL_SIZE

COLOR_BACKGROUND = (0, 0, 0) # black
COLOR_GRID_LINE = (255, 255, 255) # white
AGENT_COLOR = (0, 255, 0) # green
clock_speed = 1000

# a small passage in the middle of the map
danger_zones = [(5, 0),(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 10), (5, 11), (5, 12), (5, 13), (5, 14), (5, 15)]
finish_zone = (1, 8)
agent_position = (15, 5)

# Q-learning parameters
state = agent_position
reward = 0
actions = [0, 1, 2, 3]
epsilon = 1.0
epsilon_decay = 0.995

# a matrix where each cell represents a state and the value represents the Q-value for that state-action pair
q_table = [[[0 for _ in range(len(actions))] for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def move_agent(position, action):
    x, y = position
    if action == 0: # up
        return (x - 1, y)
    elif action == 1: # down
        return (x + 1, y)
    elif action == 2: # left
        return (x, y - 1)
    elif action == 3: # right
        return (x, y + 1)
    return position # no movement if action is invalid

def is_danger_zone(position):
    return position in danger_zones

def is_out_of_bounds(position):
    x, y = position
    return x < 0 or x >= GRID_SIZE or y < 0 or y >= GRID_SIZE

def update_q_table(state, action, reward, next_state, done=False, alpha=0.1, gamma=0.9):
    x, y = state
    
    if done:
        best_next_action = 0
    else:
        next_x, next_y = next_state
        best_next_action = max(q_table[next_x][next_y])
        
    q_table[x][y][action] += alpha * (reward + gamma * best_next_action - q_table[x][y][action])

def reset_agent():
    global agent_position, state
    agent_position = (15, 5)
    state = agent_position

pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                clock_speed = 10 if clock_speed == 1000 else 1000

    screen.fill(COLOR_BACKGROUND)

    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        pygame.draw.line(screen, COLOR_GRID_LINE, (x, 0), (x, WINDOW_SIZE))
    for y in range(0, WINDOW_SIZE, CELL_SIZE):
        pygame.draw.line(screen, COLOR_GRID_LINE, (0, y), (WINDOW_SIZE, y))

    agent_rect = pygame.Rect(agent_position[1] * CELL_SIZE, agent_position[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, AGENT_COLOR, agent_rect)

    for zone in danger_zones:
        zone_rect = pygame.Rect(zone[1] * CELL_SIZE, zone[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (255, 0, 0), zone_rect) # red for danger zones
        pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(finish_zone[1] * CELL_SIZE, finish_zone[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)) # yellow for finish zone
    pygame.display.flip()

    #epsilon decay over time to reduce exploration as the agent learns
    epsilon *= epsilon_decay
    if random.uniform(0, 1) < epsilon:  # exploration
        action = random.choice(actions)
    else:  # exploitation
        x, y = state
        action = q_table[x][y].index(max(q_table[x][y]))

    new_position = move_agent(agent_position, action)

    if is_out_of_bounds(new_position):
        reward = -5
        update_q_table(state, action, reward, next_state=new_position, done=True)
        reset_agent()
    elif is_danger_zone(new_position):
        reward = -10
        update_q_table(state, action, reward, next_state=new_position, done=True)
        reset_agent()
    elif new_position == finish_zone:
        reward = 10
        update_q_table(state, action, reward, next_state=new_position, done=True)
        reset_agent()
    else:
        reward = -0.1
        update_q_table(state, action, reward, next_state=new_position, done=False)
        agent_position = new_position
        state = agent_position

    clock.tick(clock_speed)