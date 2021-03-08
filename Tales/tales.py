from pygame import mixer

import random
import gtts

mixer.init()

name = input("Введи свое имя: ")
place = input("Назови свою любимую станцию метро: ")
sport = input("Что ты любишь делать:")
exclamation = input("Придумай какое нибудь восклицание: ")
tell = input("Придумай фразу для мутанта:")
adjective = input("Привумайте название мутанта: ")
random_year = random.randint(1, 100)

if random_year <= 16:
  zhil_text = "Жил он НЕ очень долго"
if random_year < 60 and random_year > 16:
  zhil_text = "Жил он да был"
if random_year > 59:
  zhil_text = "Жил он очень долго"

text = 'Жил в метрополитене один интересный персонаж, его звали ' + name + '. ' + zhil_text +', около ' + str(random_year) + ' лет, ' + name + ' очень любил ' + sport + ' на своей станции, под названием ' + place + '. Но однажды когда начал '+ sport + ' пришел '+ adjective + ', откусил ему ногу и убежал с криками '+ tell + '. "Ух, '  + exclamation + '!" сказал ' + name + '. Конец истории'

print("Подождите...")

gtts_result = gtts.gTTS(text, lang = "ru")
gtts_result.save("audio.mp3")

mixer.music.load('audio.mp3')
mixer.music.play()

print(text)

input("Прослушайте сообщение...")

