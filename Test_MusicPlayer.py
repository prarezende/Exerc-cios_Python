#pip install pygame

from pygame import mixer
print("Olá, ouça Sublime.mp3!")
mixer.init() #initializing pygame mixer
print("mixer.init()")
mixer.music.load('Test_MusicPlayer.mp3') #Loading audio file
print("ouvindo Sublime.mp3")
mixer.music.play() #Playing Music with Pygame
#Assim a gente ouve a música em background, mas vamos incluir um stop
mixer.music.wait()
 
print("Você acabou de ouvir Sublime.mp3!")

#import pygame
#pygame.init()
#pygame.mixer.music.load('Test_MusicPlayer.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()
#Esse código acima funciona tb. 
