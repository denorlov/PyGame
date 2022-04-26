import random
import pgzrun

right = True
play = 0
time_left = 600
WIDTH, HEIGHT = 1080, 720
size = 150
angle = 45

colors = ['red', 'green', 'purple', 'blue', 'yellow']
text = ['red', 'green', 'purple', 'blue', 'yellow']
stagecolor = []
stagetext = []
stagetext.append("blue")
stagecolor.append("blue")
for i in range(25):
    stagetext.append(colors[random.randint(0, len(colors) - 1)])
    stagecolor.append(colors[random.randint(0, len(colors) - 1)])
print(stagetext)
print(stagecolor)
i = 0
game_run = True


def update():
    global time_left
    global game_run
    if time_left == 0:
        game_run = False
    pass


def on_mouse_down(pos, button):
    global time_left
    global i
    global game_run
    global size
    global angle
    if i + 1 <= len(stagetext) - 1:
        if mouse.LEFT == button:
            print("Left button clicked!")

            if stagetext[i] == stagecolor[i]:
                print("They matches, score increase")
                size = 150
                angle = 45
                i += 1
                time_left += 120
            else:
                print("They don't, score decrease")
                game_run = False


        elif mouse.RIGHT == button:
            print("Right button clicked!")

            if stagetext[i] == stagecolor[i]:
                print("They matches, score decrease")
                game_run = False
            else:
                print("They don't, score increase")
                size = 150
                angle = 45
                i += 1
                time_left += 120
    else:
        game_run = False