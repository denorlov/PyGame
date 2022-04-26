import random
import pgzrun

game_state = "game"
items = []
gems = 0
collected_gems = 0

for r in range(0, 15):
    row = []
    for c in range(0, 20):
        itype = "soil"
        if (r == 0 or r == 14 or c == 0 or c == 19):
            itype = "wall"
        elif random.randint(0, 4) == 1:
            itype = "rock"
        elif random.randint(0, 20) == 1:
            itype = "gem"
            gems += 1
        row.append(itype)
    items.append(row)
items[1][1] = "rockford"

for row in items:
    print(row)
    print()

r_col, r_row = 1, 1
r_dcol, r_drow = 0, 0

count = 0

def draw():
    global count
    screen.fill((0, 0, 0))

    for r in range(0, 15):
        for c in range(0, 20):
            if items[r][c] != "" and items[r][c] != "rockford":
                rect = Rect(c * 40, (r * 40), 39, 39)
                if items[r][c] == "wall":
                    color = 'grey'
                    screen.draw.filled_rect(rect, color)
                elif items[r][c] == "soil":
                    color='tan'
                    screen.draw.filled_rect(rect, color)
                elif items[r][c] == "gem":
                    color = "green"
                    screen.draw.line((c * 40, r * 40), (c * 40 + 40, r * 40), color)
                    screen.draw.line((c * 40, r * 40), (c * 40 + 20, r * 40 + 40), color)
                    screen.draw.line((c * 40 + 20, r * 40 + 40), (c * 40 + 40, r * 40), color)
                elif items[r][c] == "rock":
                    color = "dodgerblue4"
                    screen.draw.filled_circle((c * 40 + 20, r * 40 + 20), 18, color)

    rockford_rect = Rect(r_col * 40 + 1, r_row * 40 + 1, 37, 37)

    if game_state == "game":
        color = "gold"
        screen.draw.filled_rect(rockford_rect, color)
    elif game_state == "dead":
        count = count + 1
        if count % 4 == 0 and count < 100:
            color = "red"
            screen.draw.filled_rect(rockford_rect, color)

    screen.draw.text(f"GEMS: {collected_gems} / {gems}", center=(400, 20), color=(0, 0, 255), fontsize=40)

    if gems == collected_gems:
        screen.draw.text("WIN!", center=(400, 300), fontsize=80)
    elif game_state == "dead":
        screen.draw.text("GAME OVER!", center=(400, 300), fontsize=80)


def on_key_up(key):
    global r_dcol, r_drow

    if key == keys.LEFT:
        r_dcol = -1
    if key == keys.RIGHT:
        r_dcol = 1

    if key == keys.UP:
        r_drow = -1
    if key == keys.DOWN:
        r_drow = 1


def update():
    global r_dcol, r_drow, collected_gems

    for r in range(14, -1, -1):
        for c in range(19, -1, -1):
            if items[r][c] == "rock":
                if items[r + 1][c] == "":
                    moveRock(r, c, r + 1, c)
                elif items[r + 1][c] == "rock" and items[r + 1][c - 1] == "" and items[r][c - 1] == "":
                    moveRock(r, c, r + 1, c - 1)
                elif items[r + 1][c] == "rock" and items[r + 1][c + 1] == "" and items[r][c + 1] == "":
                    moveRock(r, c, r + 1, c + 1)

    if game_state == "game":
        global r_col, r_row

        new_pos_item = items[r_row + r_drow][r_col + r_dcol]
        if new_pos_item != "rock" and new_pos_item != "wall":
            if new_pos_item == "gem":
                collected_gems += 1
            items[r_row][r_col] = ""
            items[r_row + r_drow][r_col + r_dcol] = "rockford"
            r_col += r_dcol
            r_row += r_drow
        if new_pos_item == "rock" and r_drow == 0:
            if items[r_row][r_col + (r_dcol * 2)] == "":
                items[r_row][r_col] = ""
                items[r_row][r_col + (r_dcol * 2)] = "rock"
                items[r_row + r_drow][r_col + r_dcol] = "rockford"
                r_col += r_dcol
        r_dcol = 0
        r_drow = 0


def moveRock(r1, c1, r2, c2):
    global game_state
    items[r2][c2] = items[r1][c1]
    items[r1][c1] = ""
    if items[r2 + 1][c2] == "rockford":
        game_state = "dead"


pgzrun.go()
