import pygame
import os
import sys
import math

from utils import resize_img, blit_rotate_center
from game.game_parameters import GameParameters as gp

pygame.init()

"""Modulacja z funkcjami pygame -> dużo miesza bo razem z załadowaniem obrazka długi ciąg się robi"""
# RACE_TRACK_IMG = pygame.transform.scale_by(RACE_TRACK_IMG, 1.1)
# CAR_IMG = pygame.transform.scale_by(CAR_IMG, 2.0)


class AbstractCar:
    IMG = ""  # ścieżka do pliku obrazka
    START_POS_X = 0  # zobaczę co będzie lepsze
    START_POS_Y = 0

    def __init__(self, rotation_vel, start_pos_x, start_pos_y):
        self.x_cord = start_pos_x
        self.y_cord = start_pos_y
        self.pos_top_left = (
            self.x_cord,
            self.y_cord,
        )  # zapamiętaj idioto że init wykonuje się tylko raz więc nie przypisuj w nim zmiennych które chcesz żeby się zmieniały
        self.image = self.IMG
        self.velocity = 0
        self.max_velocity = 2
        self.rotation_vel = rotation_vel
        self.angle = 84

        """W takim układzie współrzędnych, kąt zero stopni odpowiada orientacji obiektu wzdłuż osi X,
         z "górą" obiektu skierowaną w górę ekranu (w kierunku przeciwnym do rosnącej wartości na osi Y)."""

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel  # chce iść w lewo zmniejszam kąt
        if right:
            self.angle -= self.rotation_vel  # chce iść w prawo zmniejszam kąt

    def move(self):
        radians = math.radians(self.angle)
        # x_move = self.max_velocity * math.cos(math.pi/2 - radians) # jakby patrzyć na prędkość względem osi x
        # y_move = self.max_velocity * math.sin(math.pi/2 - radians) # jakby patrzyć na prędkość względem osi x
        x_move = self.max_velocity * math.sin(radians)  # jakby patrzyć na prędkość względem osi y
        y_move = self.max_velocity * math.cos(radians)  # jakby patrzyć na prędkość względem osi y
        # wszystko to dlatego że mój kąt 0 jest ustawiony wzlgędem osi y a nie x
        self.x_cord -= x_move
        self.y_cord -= y_move

    def draw_rotated_car(self, window):
        blit_rotate_center(
            surf=window, image=self.image, topleft=(self.x_cord, self.y_cord), angle=self.angle
        )


class ComputerCar(AbstractCar):
    pass


class PlayerCar(AbstractCar):
    IMG = gp.CAR_IMG

    def __init__(self, rotation_vel, start_pos_x, start_pos_y):
        super().__init__(rotation_vel, start_pos_x, start_pos_y)
        
    def control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            super().rotate(left=True)
        if keys[pygame.K_d]:
            super().rotate(right=True)
        if keys[pygame.K_w]:
            super().move()


def draw(window, images: list, car_obj):
    window.fill((29, 130, 34))
    for image, position in images:
        window.blit(image, position)

    car_obj.draw_rotated_car(window)
    car_obj.control()
    pygame.display.update()


car1 = PlayerCar(rotation_vel=2, start_pos_y=200, start_pos_x=200)
run = True
FPS = 60  # klatki na sekunde
timer = pygame.time.Clock()  # tworzenie instancji zegara

while run:
    timer.tick(FPS)
    draw(gp.GAME_WINDOW, gp.IMAGES_AND_SIZES, car1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
