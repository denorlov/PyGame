# Boulder Dash
import random
import pgzrun
from pgzero.actor import Actor


def headerText(t):
    screen.draw.text(
        t,
        center=(400, 20),
        owidth=0.5, ocolor=(255, 255, 255),
        color=(0, 0, 255),
        fontsize=40
    )


def bigTitleText(t):
    screen.draw.text(
        t,
        center=(400, 300),
        owidth=0.5, ocolor=(255, 255, 255),
        color=(255, 0, 0), fontsize=80
    )


rockford = Actor('rockford-1', center=(60, 100))
game_state = "game"
items = []
gems = 0
collected = 0

for r in range(0, 14):
    row = []
    for c in range(0, 20):
        itype = "soil"
        if (r == 0 or r == 13 or c == 0 or c == 19):
            itype = "wall"
        elif random.randint(0, 4) == 1:
            itype = "rock"
        elif random.randint(0, 20) == 1:
            itype = "gem"
            gems += 1
        row.append(itype)
    items.append(row)
items[1][1] = "rockford"

count = 0

def draw():
    global count
    screen.fill((0, 0, 0))

    for r in range(0, 14):
        for c in range(0, 20):
            if items[r][c] != "" and items[r][c] != "rockford":
                screen.blit(items[r][c], ((c * 40), 40 + (r * 40)))

    if game_state == "game":
        rockford.draw()

    if game_state == "dead":
        count = count + 1
        if count % 4 == 0 and count < 100:
            rockford.draw()

    headerText("GEMS : " + str(collected))
    if gems == collected:
        bigTitleText("WIN!")
    elif game_state == "dead":
        bigTitleText("GAME OVER!")


mx = my = 0


def on_key_up(key):
    global mx, my

    if key == keys.LEFT:
        mx = -1
    if key == keys.RIGHT:
        mx = 1

    if key == keys.UP:
        my = -1
    if key == keys.DOWN:
        my = 1


def update():
    global mx, my

    for r in range(13, -1, -1):
        for c in range(19, -1, -1):
            if items[r][c] == "rock":
                testRock(r, c)

    rockford.image = "rockford" + str(mx)

    if game_state == "game":
        moveRockford(mx, my)
        mx = 0
        my = 0


def moveRockford(x, y):
    global collected
    rx = int((rockford.x - 20) / 40)
    ry = int((rockford.y - 40) / 40)
    if items[ry + y][rx + x] != "rock" and items[ry + y][rx + x] != "wall":
        if items[ry + y][rx + x] == "gem":
            collected += 1
        items[ry][rx] = ""
        items[ry + y][rx + x] = "rockford"
        rockford.pos = (rockford.x + (x * 40), rockford.y + (y * 40))
    if items[ry + y][rx + x] == "rock" and y == 0:
        if items[ry][rx + (x * 2)] == "":
            items[ry][rx] = ""
            items[ry][rx + (x * 2)] = "rock"
            items[ry + y][rx + x] = "rockford"
            rockford.x += x * 40


def testRock(r, c):
    if items[r + 1][c] == "":
        moveRock(r, c, r + 1, c)
    elif items[r + 1][c] == "rock" and items[r + 1][c - 1] == "" and items[r][c - 1] == "":
        moveRock(r, c, r + 1, c - 1)
    elif items[r + 1][c] == "rock" and items[r + 1][c + 1] == "" and items[r][c + 1] == "":
        moveRock(r, c, r + 1, c + 1)


def moveRock(r1, c1, r2, c2):
    global game_state
    items[r2][c2] = items[r1][c1]
    items[r1][c1] = ""
    if items[r2 + 1][c2] == "rockford":
        game_state = "dead"


pgzrun.go()
