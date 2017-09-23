#------------ modules used ---------------- #
import pygame,os,sys,time,mutagen
from pygame.locals import * 
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
pygame.init()
pygame.mixer.init()


""" This is a program for a audio player made using pygame and mutagen."""


#-------------------- global variables ------------------#
"""COLOURS FOR TEXT TO BE DISPLAYED ON THE SCREEN"""
GREY = 180,180,180  
BLACK = 0,0,0

""" MAIN LOOP VARIBLES"""
Exit = False
not_over = True     
working = True

""" FOR MOUSEBUTTONDOWN EVENT"""
LEFT = 1            

#-------------------- functions and classes ----------------- #
def path():
    """FOR GETTING THE SAVED DIRECTORY PATH SAVED IN THE LAST RUN."""
    with open('path_name.txt','r+') as f:
        return f.read()

class audio:
    """CLASS FOR AUDIO FILE EXTRACTION, LOAD AND CLASS_ASSIGN"""
    extension = ['mp3','ogg','flac']
    name,directory = [],[]
   
    @staticmethod #decorator
    def check(audio_file):
        try:
            if audio_file.split('.')[1] in audio.extension:
                return True
        except:
            return False

    @staticmethod  #decorator
    def extract(path):
        for files in os.listdir(path):
            try:
                files = audio.extract(path + '/' + files)
            except:
                if audio.check(files) is True:
                    audio.directory.append(path + '/' + files)
                    audio.name.append(files)

    @staticmethod  #decorator
    def class_assign(n):
         

        if audio.name[n].split('.')[1] == 'mp3':
            return mp3(audio.directory[n])
        elif audio.name[n].split('.')[1] == 'ogg':
            return ogg(audio.directory[n])
        elif audio.name[n].split('.')[1] == 'flac':
            return flac(audio.directory[n])

    @staticmethod   #decorator
    def load(n):
        pygame.mixer.music.load(audio.directory[n])
        pygame.mixer.music.play()


"""CLASS FOR mp3 FILES. METADATA IS THE INFO EMBEDDED IN THE MUSIC FILE """  
class mp3:

    def __init__(self,path):
        self.file = MP3(path)
        self.metadata()
        
    def metadata(self):
        try:
            self.artist = 'ARTIST :' + self.file['TPE2'][0]
            self.title = 'TITLE :' + self.file['TIT2'][0]
            self.album = 'ALBUM :' + self.file['TALB'][0]
        except:
            self.artist = 'ARTIST : N/A'
            self.title = 'TITLE : N/A'
            self.album = 'ALBUM : N/A'

""" CLASS FOR ogg TYPE FILE"""        
class ogg:

    def __init__(self,path):
        self.file = mutagen.File(path)
        self.metadata()
        
    def metadata(self):
        try:
            self.artist = 'ARTIST :' + self.file['artist'][0]
            self.title = 'TITLE :' + self.file['title'][0]
            self.album = 'ALBUM :' + self.file['album'][0]
        except:
            self.artist = 'ARTIST : N/A'
            self.title = 'TITLE : N/A'
            self.album = 'ALBUM : N/A'

"""CLASS FOR flac TYPE FILE"""
class flac:
    def __init__(self,path):
        self.file = FLAC(path)
        self.metadata()

    def metadata(self):
        try:
            self.artist = 'ARTIST :' + self.file['artist'][0]
            self.title = 'TITLE :' + self.file['title'][0]
            self.album = 'ALBUM :' + self.file['album'][0]
        except:
            self.artist = ' ARTIST : N/A'
            self.title = 'TITLE : N/A'
            self.album = 'ALBUM : N/A'


""" CLASS FOR PYGAME WINDOW AND DISPLAYING TEXT ON THE SCREEN"""
class game_window():
    def __init__(self,width,height,color,caption):
        self.resolution = width,height
        self.bckg_color = color
        self.caption = caption

    def Pygame_init(self):
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption(self.caption)
        self.screen.fill(self.bckg_color)
        pygame.display.update()

    def display_text(self,text,color,size,font,x,y):
        self.font = pygame.font.SysFont(font,size)
        self.label = self.font.render(text,1,color)
        self.screen.blit(self.label,(x,y))
        pygame.display.update()


""" CLASS FOR DISPLAYING MUSIC CONTROL BUTTONS"""
class Button():

    def __init__(self,image,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = self.transform(image)
        

    def transform(self,image):
        image_load = pygame.image.load(image)
        return pygame.transform.scale(image_load,(self.width,self.height))
        
    def blit(self,surface):
        surface.blit(self.image,(self.x,self.y))
        pygame.display.update()



""" THIS FUNCTION CALLS ALL THE ABOVE CLASSES AND DISPLAYS THE BUTTONS AND TEXT\
ON THE SCREEN"""
def screen_status():


    play = Button('play.png',0,100,50,50)
    play.blit(set1.screen)

    pause = Button('pause.png',50,100,50,50)
    pause.blit(set1.screen)

    previous = Button('back.png',100,100,50,50)
    previous.blit(set1.screen)
    
    Next = Button('next.png',150,100,50,50)
    Next.blit(set1.screen)
    
    volume_up = Button('v_up.png',200,100,50,50)
    volume_up.blit(set1.screen)
    
    mute = Button('mute.png',250,100,50,50)
    mute.blit(set1.screen)
    
    volume_down = Button('v_down.png',300,100,50,50)
    volume_down.blit(set1.screen)
    
    rewind = Button('rewind.png',350,100,50,50)
    rewind.blit(set1.screen)

    new_path = Button('plus.png',400,100,50,50)
    new_path.blit(set1.screen)

    set1.display_text(song.title,BLACK,20,'Times New Roman',0,0) 
    set1.display_text(song.album,BLACK,20,'Times New Roman',0,30) 
    set1.display_text(song.artist,BLACK,20,'Times New Roman',0,50)




path_name = path()


#---------------------- MAIN LOOP() ----------------------#

while not_over:
    audio.extract(path_name)
    
    n = -1
    working = True


    while working:
        set1 = game_window(450,150,GREY,'AUDIO PLAYER')
        set1.Pygame_init()

        n += 1
        if n == len(audio.directory):
            n = 0
        
        song = audio.class_assign(n)
        audio.load(n)

        screen_status()
        running = True

        while running :
            
            for event in pygame.event.get():
                
                if event.type == MOUSEBUTTONDOWN \
                   and event.button == LEFT:

                    x,y = event.pos
                    index = (x/50)

                    if index == 0:
                        pygame.mixer.music.unpause()
                    elif index == 1:
                        pygame.mixer.music.pause()
                    elif index == 2:
                        n -= 2
                        running = False
                        break
                    elif index == 3:
                        running = False
                        break
                    elif index == 4:
                        volume = pygame.mixer.music.get_volume() + 0.1
                        if volume <= 1:
                            pygame.mixer.music.set_volume(volume)
                    elif index == 5:
                        pygame.mixer.music.set_volume(0)
                    elif index == 6:
                        volume = pygame.mixer.music.get_volume() - 0.1
                        if volume >= 0:
                            pygame.mixer.music.set_volume(volume)
                    elif index == 7:
                        pygame.mixer.music.rewind()

                    elif index == 8:
                        path_name = raw_input('enter new path')
                        with open('path_name.txt','w') as f:
                            f.write(path_name)
                            f.close()
                        
                        running, working = False,False
                        audio.directory,audio.name = [],[]
                        break
                        
                        
                elif event.type == pygame.QUIT:
                    running = False
                    not_over = False
                    pygame.mixer.quit()
                    pygame.quit()
                    sys.exit()
                    
                if  not pygame.mixer.music.get_busy():
                    running = False
                    break
                pygame.display.update()

    
            

        























