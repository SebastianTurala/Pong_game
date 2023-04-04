import sys
import pygame
import random

pygame.init()
clock = pygame.time.Clock()

# window
width = 250
height = 260
window = pygame.display.set_mode([width, height], pygame.NOFRAME)
fps = 60

# player_1
score_1 = 0
start_1 = [100, 255]
end_1 = [150, 255]
def move_L1():
    global start_1, end_1
    if start_1[0] < 0:
        pass
    else:
        start_1[0] -= 2
        end_1[0] -= 2
def move_R1():
    global start_1, end_1
    if end_1[0] + 5 > 255:
        pass
    else:
        start_1[0] += 2
        end_1[0] += 2

# player_2
score_2 = 0
start_2 = [100, 5]
end_2 = [150, 5]
def move_L2():
    global start_2, end_2
    if start_2[0] < 0:
        pass
    else:
        start_2[0] -= 2
        end_2[0] -= 2
def move_R2():
    global start_2, end_2
    if end_2[0] + 5 > 255:
        pass
    else:
        start_2[0] += 2
        end_2[0] += 2

# ball
ball_pos = [125, 130]
ball_status = True
def ball_move(dir):
    global ball_pos, ball_status
    if ball_status:
        if dir == 0:
            ball_pos[0] -= 1
            ball_pos[1] -= 2
        elif dir == 1:
            ball_pos[0] += 1
            ball_pos[1] -= 2
        elif dir == 2:
            ball_pos[0] -= 1
            ball_pos[1] += 2
        elif dir == 3:
            ball_pos[0] += 1
            ball_pos[1] += 2
    else:
        pass

def ball_hit(dir):
    global ball_direction, ball_pos, ball_status, score_2, score_1, start_1, start_2, end_1, end_2
    # hitting the wall
    if dir == 0 and ball_pos[0] - 5 <= 0:
        ball_direction = 1
    elif dir == 1 and ball_pos[0] + 5 >= 250:
        ball_direction = 0
    elif dir == 2 and ball_pos[0] - 5 <= 0:
        ball_direction = 3
    elif dir == 3 and ball_pos[0] + 5 >= 250:
        ball_direction = 2

    # hitting the player 1
    if dir == 2 and ball_pos[0] >= start_1[0] and ball_pos[0] <= end_1[0] and ball_pos[1] == 250:
        ball_direction = 0
    elif dir == 3 and ball_pos[0] >= start_1[0] and ball_pos[0] <= end_1[0] and ball_pos[1] == 250:
        ball_direction = 1
    elif (ball_pos[0] < start_1[0] or ball_pos[1] > end_1[0]) and ball_pos[1] >= 260:
        ball_pos = [125, 130]
        score_2 += 1
        start_1 = [100, 255]
        end_1 = [150, 255]
        start_2 = [100, 5]
        end_2 = [150, 5]
        ball_direction = random.choice([0, 1, 2, 3])
        ball_status = False

    # hitting the player 2
    if dir == 0 and ball_pos[0] >= start_2[0] and ball_pos[0] <= end_2[0] and ball_pos[1] == 10:
        ball_direction = 2
    elif dir == 1 and ball_pos[0] >= start_2[0] and ball_pos[0] <= end_2[0] and ball_pos[1] == 10:
        ball_direction = 3
    elif (ball_pos[0] < start_2[0] or ball_pos[0] > end_2[0]) and ball_pos[1] <= 0:
        ball_pos = [125, 130]
        score_1 += 1
        start_1 = [100, 255]
        end_1 = [150, 255]
        start_2 = [100, 5]
        end_2 = [150, 5]
        ball_direction = random.choice([0, 1, 2, 3])
        ball_status = False

# game_loop
game_over = False
ball_direction = random.choice([0, 1, 2, 3])
while not game_over:
    clock.tick(fps)
    # events
    for events in pygame.event.get():
        # keyboard
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_ESCAPE:
                sys.exit()
    pressed_keys = pygame.key.get_pressed()
    # player_1 keys
    if pressed_keys[pygame.K_LEFT]:
        move_L1()
        ball_status = True
    if pressed_keys[pygame.K_RIGHT]:
        move_R1()
        ball_status = True
    # player_2 keys
    if pressed_keys[pygame.K_a]:
        move_L2()
        ball_status = True
    if pressed_keys[pygame.K_d]:
        move_R2()
        ball_status = True

# draw
    # player_1
    pygame.draw.line(window, 'black', start_1, end_1, 5)
    # player_2
    pygame.draw.line(window, 'blue', start_2, end_2, 5)
    # ball
    pygame.draw.circle(window, 'red', [ball_pos[0], ball_pos[1]], 5)
    ball_move(ball_direction)
    ball_hit(ball_direction)

    pygame.display.update()
    window.fill("white")