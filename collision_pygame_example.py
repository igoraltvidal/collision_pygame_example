import pygame
from pygame.locals import *
from random import randint

pygame.init()

screen = pygame.display.set_mode((600, 600), 0, 32)
background_colour = (255,255,255)  
clock = pygame.time.Clock()

class Car:

    def __init__(self,color,pos_y):
        self.image_filename = 'car_' + color + '.png'
        self.image = pygame.image.load(self.image_filename).convert()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect_def = self.image.get_rect()
        self.rect_def.y = pos_y 
        self.rect_def.x = 50
        self.color = color + ' car'
        screen.blit(self.image,self.rect_def)
          
    def move(self):
        self.dx = randint(10, 25)
        self.rect_def.x = self.dx + self.rect_def.x
        screen.blit(self.image,self.rect_def)

        
        
class Line:

    def __init__(self,pos_x):
        self.image_filename = 'line.png'
        self.image = pygame.image.load(self.image_filename).convert()
        self.image = pygame.transform.scale(self.image, (50, 400))
        self.rect_def = self.image.get_rect()
        self.rect_def.y = 100
        self.rect_def.x = pos_x
        screen.blit(self.image,self.rect_def)
        
    def reset_image(self):
        screen.blit(self.image,self.rect_def)       
        

car1 = Car('red',200)
car2 = Car('yellow', 300)
car3 = Car('blue',400)
line = Line(550)

list_cars = [car1,car2,car3]  #create a list with the objects that you want to check

while True:

    screen.fill(background_colour)
    line.reset_image()
    car1.move()
    car2.move()
    car3.move()
    
    for i in range(0,3):
    
        if line.rect_def.colliderect(list_cars[i].rect_def) == True:    #compare if some of the objects collide
        
            winner = list_cars[i].color          #do something
            print("%s WIN!" %winner)         #now you know identify what of the object colided
            raise SystemExit

    pygame.display.update()
    time_passed = clock.tick(10)
    

