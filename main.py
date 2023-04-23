import pygame as pg
from pygame import mixer
import random
import sys
from button import Button

pg.init()
mixer.init()
mixer.music.load("music/bg.wav")  
mixer.music.set_volume(0.7)  
mixer.music.play(-1)

clock = pg.time.Clock()

# Default settings
SPEED = 3
RADIUS = 30
NUMBER_OF_OBJECTS = 10
SPEED3_BASE_COLOR = 'Blue'
SPEED1_BASE_COLOR = '#d7fcd4'
SPEED5_BASE_COLOR = '#d7fcd4'

# SCREEN settings
(WIDTH, HEIGHT) = (1280, 720)
SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Menu')

objects = []

# Object Class


class Object:
    def __init__(self, x, y, image, name, speed, radius):
        self.x = x
        self.y = y
        self.image = image
        self.name = name
        self.radius = radius
        self.velocity = [
            random.randint(-speed, speed), random.randint(-speed, speed)]
        self.rect = pg.Rect(x, y, radius, radius)
        objects.append(self)

    # Draw on the screen
    def draw(self):
        SCREEN.blit(pg.transform.scale(self.image, (self.radius, self.radius)),
                    (self.x, self.y))

    # Moving objects
    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        # Check if the object has hit a boundary
        if self.x < 0 or self.x > WIDTH - self.radius:
            self.velocity[0] *= -1
        if self.y < 0 or self.y > HEIGHT - self.radius:
            self.velocity[1] *= -1

        self.rect.x = self.x
        self.rect.y = self.y

        # Check for collisions with other objects
        for obj in objects:
            # Don't collide with itself
            if obj == self:
                continue
            # Check if the two objects overlap
            if self.rect.colliderect(obj.rect):
                if self.name == 'rock' and obj.name == 'paper':
                    self.name = obj.name
                    self.image = obj.image
                elif self.name == 'paper' and obj.name == 'rock':
                    obj.name = self.name
                    obj.image = self.image
                elif self.name == 'paper' and obj.name == 'scissors':
                    self.name = obj.name
                    self.image = obj.image
                elif self.name == 'scissors' and obj.name == 'paper':
                    obj.name = self.name
                    obj.image = self.image
                elif self.name == 'scissors' and obj.name == 'rock':
                    self.name = obj.name
                    self.image = obj.image
                elif self.name == 'rock' and obj.name == 'scissors':
                    obj.name = self.name
                    obj.image = self.image

                self.velocity[0] *= -1
                self.velocity[1] *= -1
                obj.velocity[0] *= -1
                obj.velocity[1] *= -1

        self.draw()


def get_font(size):
    return pg.font.Font("fonts/Sigmar-Regular.ttf", size)

# Functions to change default settings of game

SPEED3_BASE_COLOR='Blue'
SPEED1_BASE_COLOR='#d7fcd4'
SPEED5_BASE_COLOR='#d7fcd4'

def change_speed():
    global SPEED3_BASE_COLOR
    global SPEED5_BASE_COLOR
    global SPEED1_BASE_COLOR

    while True:
        SCREEN.fill('black')

        SPEED_MOUSE_POS = pg.mouse.get_pos()

        SPEED3_BUTTON = Button(image=None, pos=(640, 250),
                               text_input="1x", font=get_font(75), base_color=SPEED3_BASE_COLOR, hovering_color="White")
        SPEED1_BUTTON = Button(image=None, pos=(640, 400),
                               text_input="0.5x", font=get_font(75), base_color=SPEED1_BASE_COLOR, hovering_color="White")
        SPEED5_BUTTON = Button(image=None, pos=(640, 550),
                               text_input="2x", font=get_font(75), base_color=SPEED5_BASE_COLOR, hovering_color="White")
        SPEED_BACK = Button(image=None, pos=(640, 660),
                            text_input="BACK", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SPEED_TEXT = get_font(100).render("SPEED", True, "#b68f40")
        SPEED_RECT = SPEED_TEXT.get_rect(center=(640, 100))

        SCREEN.blit(SPEED_TEXT, SPEED_RECT)

        for button in [SPEED3_BUTTON, SPEED1_BUTTON, SPEED5_BUTTON, SPEED_BACK]:
            button.changeColor(SPEED_MOUSE_POS)
            button.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                global SPEED
                if SPEED3_BUTTON.checkForInput(SPEED_MOUSE_POS):
                    SPEED = 3
                    SPEED3_BASE_COLOR = 'Blue'
                    SPEED1_BASE_COLOR = '#d7fcd4'
                    SPEED5_BASE_COLOR = '#d7fcd4'
                if SPEED1_BUTTON.checkForInput(SPEED_MOUSE_POS):
                    SPEED = 1
                    SPEED3_BASE_COLOR = '#d7fcd4'
                    SPEED1_BASE_COLOR = 'Blue'
                    SPEED5_BASE_COLOR = '#d7fcd4'
                if SPEED5_BUTTON.checkForInput(SPEED_MOUSE_POS):
                    SPEED = 10
                    SPEED3_BASE_COLOR = '#d7fcd4'
                    SPEED1_BASE_COLOR = '#d7fcd4'
                    SPEED5_BASE_COLOR = 'Blue'
                if SPEED_BACK.checkForInput(SPEED_MOUSE_POS):
                    options()

        pg.display.update()

NUMBER10_BASE_COLOR = 'Blue'
NUMBER50_BASE_COLOR = '#d7fcd4'
NUMBER100_BASE_COLOR = '#d7fcd4'

def change_number_of_objects():
    global NUMBER10_BASE_COLOR
    global NUMBER50_BASE_COLOR
    global NUMBER100_BASE_COLOR

    while True:
        SCREEN.fill('black')

        NUMBER_OF_OBJECTS_MOUSE_POS = pg.mouse.get_pos()

        NUMBER_OF_OBJECTS_MOUSE_TEXT = get_font(100).render(
            "NUMBER OF OBJECTS", True, "#b68f40")
        NUMBER_OF_OBJECTS_MOUSE_RECT = NUMBER_OF_OBJECTS_MOUSE_TEXT.get_rect(
            center=(640, 100))

        NUMBER10_BUTTON = Button(image=None, pos=(640, 250),
                                 text_input="10", font=get_font(75), base_color=NUMBER10_BASE_COLOR, hovering_color="White")
        NUMBER50_BUTTON = Button(image=None, pos=(640, 400),
                                 text_input="50", font=get_font(75), base_color=NUMBER50_BASE_COLOR, hovering_color="White")
        NUMBER100_BUTTON = Button(image=None, pos=(640, 550),
                                  text_input="100", font=get_font(75), base_color=NUMBER100_BASE_COLOR, hovering_color="White")
        NUMBER_OF_OBJECTS_BACK = Button(image=None, pos=(640, 660),
                                        text_input="BACK", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(NUMBER_OF_OBJECTS_MOUSE_TEXT, NUMBER_OF_OBJECTS_MOUSE_RECT)

        for button in [NUMBER10_BUTTON, NUMBER50_BUTTON, NUMBER100_BUTTON, NUMBER_OF_OBJECTS_BACK]:
            button.changeColor(NUMBER_OF_OBJECTS_MOUSE_POS)
            button.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                global NUMBER_OF_OBJECTS
                if NUMBER10_BUTTON.checkForInput(NUMBER_OF_OBJECTS_MOUSE_POS):
                    NUMBER_OF_OBJECTS = 10
                    NUMBER10_BASE_COLOR = 'Blue'
                    NUMBER50_BASE_COLOR = '#d7fcd4'
                    NUMBER100_BASE_COLOR = '#d7fcd4'
                if NUMBER50_BUTTON.checkForInput(NUMBER_OF_OBJECTS_MOUSE_POS):
                    NUMBER_OF_OBJECTS = 50
                    NUMBER10_BASE_COLOR = '#d7fcd4'
                    NUMBER50_BASE_COLOR = 'Blue'
                    NUMBER100_BASE_COLOR = '#d7fcd4'
                if NUMBER100_BUTTON.checkForInput(NUMBER_OF_OBJECTS_MOUSE_POS):
                    NUMBER_OF_OBJECTS = 100
                    NUMBER10_BASE_COLOR = '#d7fcd4'
                    NUMBER50_BASE_COLOR = '#d7fcd4'
                    NUMBER100_BASE_COLOR = 'Blue'
                if NUMBER_OF_OBJECTS_BACK.checkForInput(NUMBER_OF_OBJECTS_MOUSE_POS):
                    options()

        pg.display.update()

RADIUS30_BASE_COLOR = 'Blue'
RADIUS60_BASE_COLOR = '#d7fcd4'
RADIUS90_BASE_COLOR = '#d7fcd4'

def change_radius():
    global RADIUS30_BASE_COLOR
    global RADIUS60_BASE_COLOR
    global RADIUS90_BASE_COLOR

    while True:
        SCREEN.fill('black')

        RADIUS_MOUSE_POS = pg.mouse.get_pos()

        RADIUS_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        RADIUS_RECT = RADIUS_TEXT.get_rect(center=(640, 100))

        RADIUS30_BUTTON = Button(image=None, pos=(640, 250),
                                 text_input="30", font=get_font(75), base_color=RADIUS30_BASE_COLOR, hovering_color="White")
        RADIUS60_BUTTON = Button(image=None, pos=(640, 400),
                                 text_input="60", font=get_font(75), base_color=RADIUS60_BASE_COLOR, hovering_color="White")
        RADIUS90_BUTTON = Button(image=None, pos=(640, 550),
                                 text_input="90", font=get_font(75), base_color=RADIUS90_BASE_COLOR, hovering_color="White")
        RADIUS_BACK = Button(image=None, pos=(640, 660),
                             text_input="BACK", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(RADIUS_TEXT, RADIUS_RECT)

        for button in [RADIUS30_BUTTON, RADIUS60_BUTTON, RADIUS90_BUTTON, RADIUS_BACK]:
            button.changeColor(RADIUS_MOUSE_POS)
            button.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                global RADIUS
                if RADIUS30_BUTTON.checkForInput(RADIUS_MOUSE_POS):
                    RADIUS = 30
                    RADIUS30_BASE_COLOR = 'Blue'
                    RADIUS60_BASE_COLOR = '#d7fcd4'
                    RADIUS90_BASE_COLOR = '#d7fcd4'
                if RADIUS60_BUTTON.checkForInput(RADIUS_MOUSE_POS):
                    RADIUS = 60
                    RADIUS30_BASE_COLOR = '#d7fcd4'
                    RADIUS60_BASE_COLOR = 'Blue'
                    RADIUS90_BASE_COLOR = '#d7fcd4'
                if RADIUS90_BUTTON.checkForInput(RADIUS_MOUSE_POS):
                    RADIUS = 90
                    RADIUS30_BASE_COLOR = '#d7fcd4'
                    RADIUS60_BASE_COLOR = '#d7fcd4'
                    RADIUS90_BASE_COLOR = 'Blue'
                if RADIUS_BACK.checkForInput(RADIUS_MOUSE_POS):
                    options()

        pg.display.update()


# Main menu
def main_menu():
    while True:
        SCREEN.fill('black')

        MENU_MOUSE_POS = pg.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=None, pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=None, pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pg.quit()
                    sys.exit()

        pg.display.update()

# Options menu


def options():
    while True:
        OPTIONS_MOUSE_POS = pg.mouse.get_pos()

        SCREEN.fill("blue")

        OPTIONS_TEXT = get_font(45).render(
            "This is the OPTIONS screen.", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 60))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_SPEED = Button(image=None, pos=(640, 210),
                               text_input="SPEED", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_NUMBER_OF_OBJECTS = Button(image=None, pos=(640, 360),
                                           text_input="NUMBER OF OBJECTS", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_RADIUS = Button(image=None, pos=(640, 510),
                                text_input="RADIUS", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_BACK = Button(image=None, pos=(640, 660),
                              text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        for button in [OPTIONS_SPEED, OPTIONS_NUMBER_OF_OBJECTS, OPTIONS_RADIUS, OPTIONS_BACK]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if OPTIONS_SPEED.checkForInput(OPTIONS_MOUSE_POS):
                    change_speed()
                if OPTIONS_NUMBER_OF_OBJECTS.checkForInput(OPTIONS_MOUSE_POS):
                    change_number_of_objects()
                if OPTIONS_RADIUS.checkForInput(OPTIONS_MOUSE_POS):
                    change_radius()
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pg.display.update()

# Game


def game():
    # Initialize objects
    mixer.music.load("music/game.wav")  
    mixer.music.play(-1)
    for i in ['rock', 'paper', 'scissors']:
        for j in range(0, NUMBER_OF_OBJECTS):
            if (i == 'rock'):
                temp = Object(random.randint(0, WIDTH - RADIUS),
                              random.randint(0, HEIGHT - RADIUS), pg.image.load('imgs/rock.png'), 'rock', SPEED, RADIUS)
            elif (i == 'paper'):
                temp = Object(random.randint(0, WIDTH - RADIUS),
                              random.randint(0, HEIGHT - RADIUS), pg.image.load('imgs/paper.png'), 'paper', SPEED, RADIUS)
            else:
                temp = Object(random.randint(0, WIDTH - RADIUS),
                              random.randint(0, HEIGHT - RADIUS), pg.image.load('imgs/scissors.png'), 'scissors', SPEED, RADIUS)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if Game_BACK.checkForInput(GAME_MOUSE_POS):
                        mixer.music.load("music/bg.wav")   
                        mixer.music.play(-1)
                        objects.clear()
                        main_menu()

        SCREEN.fill('white')

        GAME_MOUSE_POS = pg.mouse.get_pos()

        Game_BACK = Button(image=None, pos=(640, 660),
                              text_input="BACK", font=get_font(45), base_color="Blue", hovering_color="Green")

        Game_BACK.changeColor(GAME_MOUSE_POS)
        Game_BACK.update(SCREEN)

        for obj in objects:
            obj.update()

        object_counts = {'rock': 0, 'paper': 0, 'scissors': 0}

        for obj in objects:
            object_counts[obj.name] += 1

        # Check if the count of any type of object is equal to the total number of objects

        if object_counts['rock'] == 0 and object_counts['paper'] == 0:
            font = pg.font.Font(None, 50)
            text = font.render("SCISSORS win!", True, (255, 0, 0))
            text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
            SCREEN.blit(text, text_rect)
            pg.display.update()
            pg.time.delay(1000)
            mixer.music.load("music/bg.wav")   
            mixer.music.play(-1)
            objects.clear()
            main_menu()
        elif object_counts['scissors'] == 0 and object_counts['paper'] == 0:
            font = pg.font.Font(None, 50)
            text = font.render("ROCKS win!", True, (255, 0, 0))
            text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
            SCREEN.blit(text, text_rect)
            pg.display.update()
            pg.time.delay(1000)
            mixer.music.load("music/bg.wav")   
            mixer.music.play(-1)
            objects.clear()
            main_menu()
        elif object_counts['scissors'] == 0 and object_counts['rock'] == 0:
            font = pg.font.Font(None, 50)
            text = font.render("PAPERS win!", True, (255, 0, 0))
            text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
            SCREEN.blit(text, text_rect)
            pg.display.update()
            pg.time.delay(1000)
            mixer.music.load("music/bg.wav")   
            mixer.music.play(-1)
            objects.clear()
            main_menu()

        clock.tick(60)
        pg.display.update()


main_menu()
