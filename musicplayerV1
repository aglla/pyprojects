import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 400
WINDOWHEIGHT = 200
TEXTCOLOR = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

BACKGROUNDCOLOR = (0,0,0)


def terminate():
    pygame.quit()
    sys.exit()

def drawText(text, font, windowSurface, x, y):
    textobj = font.render(text, 1, RED, GREEN)
    textrect = textobj.get_rect()
    global buttons
    newButton = {'rect':textrect, 'text':text}
    buttons.append(newButton)
    textrect.topleft = (x,y)
    windowSurface.blit(textobj, textrect)

def doSomething(button):
    global playlist
    global songIndex
    if button['text'] == 'Play':
        songIndex = 0
        pygame.mixer.music.stop()
        pygame.mixer.music.load(playlist[songIndex])

    elif button['text'] == 'Prev':
        pygame.mixer.music.stop()
        if(songIndex == 0):
            songIndex = len(playlist)-1 #go to last song if cursong is song 1
            pygame.mixer.music.load(playlist[songIndex])         
        else:
            songIndex = songIndex - 1
            pygame.mixer.music.load(playlist[songIndex])
            pygame.mixer.music.play(0, 0.0)

    elif button['text'] == 'Next':
        pygame.mixer.music.stop()
        if songIndex == len(playlist)-1:
            songIndex = 0
        else:
            songIndex = songIndex + 1
        pygame.mixer.music.load(playlist[songIndex])
        pygame.mixer.music.play(0,0.0)
            
    elif button['text'] == 'Loop':
        pygame.mixer.music.stop()
        pygame.mixer.music.load(playlist[songIndex])
        pygame.mixer.music.play(-1,0.0)

pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Music Player')
pygame.mouse.set_visible(True)

font = pygame.font.SysFont(None, 20)


playlist = ['song1.mp3', 'song2.mp3', 'song3.mp3', 'song4.mp3']
buttons = []
songIndex = 0

#make text 'buttons'
drawText('Play', font, windowSurface, 200, 100)
drawText('Prev', font, windowSurface, 150, 100)
drawText('Next', font, windowSurface, 250, 100)
drawText('Loop', font, windowSurface, 300, 100)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()

        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            for button in buttons:
                if button['rect'].collidepoint(x,y):
                    doSomething(button)
    pygame.display.update()            
            
            
    
    
