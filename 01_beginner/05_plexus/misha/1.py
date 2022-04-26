import pygame, random
pygame.init()

W, H = 1920, 1080
sc = pygame.display.set_mode((W, H))


SPEED = 20


COLOR = [0, 255, 255]

points = []

for i in range(100):
    x, y = random.randint(0, W), random.randint(0, H)
    vx, vy = random.uniform(-SPEED, SPEED), random.uniform(-SPEED, SPEED)
    points.append([x, y, vx, vy])

sc.fill('black')

flag = True

while flag:
    for i in range(len(points)):
        if points[i][0] > W:
            points[i][0] = 0
        if points[i][0] < 0:
            points[i][0] = W
        if points[i][1] > H:
            points[i][1] = 0
        if points[i][1] < 0:
            points[i][1] = H

        points[i][0] += points[i][2]
        points[i][1] += points[i][3]

        pygame.draw.circle(sc, 'white',(points[i][0], points[i][1]), 3)

    for i in points:
        for j in points:
            MAX_DISTANCE = random.randint(1, H // 5)
            distance = (abs(i[0] - j[0]) ** 2 + abs(i[1] - j[1]) ** 2) ** 0.5
            if distance <= MAX_DISTANCE:
                color = int((MAX_DISTANCE - distance) / MAX_DISTANCE * 255)
                pygame.draw.line(sc, (0, 248, 255), [i[0], i[1]], [j[0], j[1]])

    pygame.display.update()
    sc.fill('black')