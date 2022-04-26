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



def draw():
    global game_run
    global i
    global size
    global angle
    global time_left
    if game_run == True:
        screen.fill((255,255,255))

        screen.draw.text(str(time_left // 60), (10, 10), color=(0,0,0))
        time_left -= 2
        screen.draw.text(stagetext[i], (WIDTH / 2, HEIGHT / 2), color=stagecolor[i], fontsize=size, angle=angle)
        if size >= 100:
            size -= 10
        if angle > 0:
            angle -= 5
            print(angle)


    else:
        if i == len(stagetext) - 1:
            screen.fill((0, 0, 0))
            screen.draw.text('oldTV 101', (WIDTH / 2, HEIGHT / 2), fontsize=100)
        else:
            screen.fill((0, 0, 0))
            screen.draw.text('8', (WIDTH / 2 - 100, HEIGHT / 2), fontsize=400, color='red', angle=90)
            screen.draw.text('game over', (WIDTH / 2 - 100, HEIGHT / 2 + 20), fontsize=100, color='red')




pgzrun.go()