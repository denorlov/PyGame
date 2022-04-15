import random
import pgzrun
right = True
play = 0
WIDTH, HEIGHT = 1080, 720
colors = ['red', 'green', 'purple', 'blue', 'yellow']
text = ['red', 'green', 'purple', 'blue', 'yellow']
stagecolor = []
stagetext = []
stagetext.append("blue")
stagecolor.append("blue")
for i in range(10):
    stagetext.append(colors[random.randint(0, len(colors) - 1)])
    stagecolor.append(colors[random.randint(0, len(colors) - 1)])
print(stagetext)
print(stagecolor)
def update():
   pass


i = 0
inpuut = False

def on_mouse_down(button):
    print("Mouse button", button, "clicked")
    global play
    global i
    inpuut = True
    if button == mouse.RIGHT:
        play = True
    elif button == mouse.LEFT:
        play = False
    else:
        pass
    print(play)

game_run = True
t = 0
def draw():
    global play
    global right
    global t
    global game_run
    global i
    global inpuut
    if game_run == True:
        screen.fill((255,255,255))

        # screen.draw.text(t, (10, 10), color=(0,0))
        screen.draw.text(stagetext[i],(100, 100), color=stagecolor[i], fontsize=100)
        if stagetext[i] == stagecolor[i]:
            right = True
        else:
            right = False

        if right == play:
            i += 1
        else:
            game_run = False
        if i == 9:
            game_run = False

    # else:
    #     if i == 9:
    #         screen.fill((0, 0, 0))
    #         screen.draw.text('ты капец умный', (100, 100), fontsize=100)
    #     else:
    #         screen.fill((0, 0, 0))
    #         screen.draw.text('ты капец тупой', (100, 100), fontsize=100)

pgzrun.go()