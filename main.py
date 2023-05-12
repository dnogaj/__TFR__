import time

import pygame
import os
import sys
import math

from hive import Ants, Tre, Ancestors
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

    def colision(self, track_mask, x=0, y=0):
        offset = int(self.x_cord), int(self.y_cord)
        car_mask = pygame.mask.from_surface(self.current_image)
        self.colide = track_mask.overlap(car_mask, offset)
        # print(self.colide)
        return self.colide

    def get_colide(self):
        print(self.colide)
        return self.colide

    def __init__(self, rotation_vel, start_pos_x, start_pos_y, max_velocity):
        self.x_cord = start_pos_x
        self.y_cord = start_pos_y
        self.pos_top_left = (
            self.x_cord,
            self.y_cord,
        )  # zapamiętaj idioto że init wykonuje się tylko raz więc nie przypisuj w nim zmiennych które chcesz żeby się zmieniały
        self.image = self.IMG
        self.velocity = 0
        self.max_velocity = max_velocity
        self.rotation_vel = rotation_vel
        self.angle = 84
        self.current_image = None  # BADZIEW ALERT
        self.colide = None
        self.scent_of_death = []
        self.path = []
        self.follow_path = []
        self.jump = 0.1
        self.follow_ancestor_path = True
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
        self.current_image = blit_rotate_center(  # BADZIEW ALERT
            surf=window, image=self.image, top_left=(self.x_cord, self.y_cord), angle=self.angle
        )


class ComputerCar(AbstractCar):
    IMG = gp.CAR_IMG

    def __init__(self, rotation_vel, start_pos_x, start_pos_y, max_velocity):
        super().__init__(rotation_vel, start_pos_x, start_pos_y, max_velocity)
        self.turn = 0

    def control(self):
        if self.turn == 0:
            pass
        elif self.turn == 1:
            super().rotate(right=True)
        elif self.turn == -1:
            super().rotate(left=True)
        super().move()

    def set_turn(self, turn):
        self.turn = turn


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


def draw_static(window, images: list):
    window.fill((29, 130, 34))
    for image, position in images:
        window.blit(image, position)


def draw_dynamic(window, car_obj):
    for car in all_cars:
        car.draw_rotated_car(window)
        car.control()
        car.colision(gp.RACE_TRACK_BORDER_MASK)

    pygame.display.update()


# car1 = PlayerCar(rotation_vel=2, start_pos_y=200, start_pos_x=200)
run = True
FPS = 300  # klatki na sekunde
timer = pygame.time.Clock()  # tworzenie instancji zegara
# player_cars = []
# player_cars.append(PlayerCar(rotation_vel=2, start_pos_y=200, start_pos_x=200))
cars2 = []
cars2.append(ComputerCar(rotation_vel=2, start_pos_y=200, start_pos_x=200, max_velocity=2))
cars2.append(ComputerCar(rotation_vel=10, start_pos_y=200, start_pos_x=200, max_velocity=10))

size = gp.RACE_TRACK_IMG.get_size()
ants = Ants(size)
tre = Tre(1)

while run:
    timer.tick(FPS)
    all_cars = cars2
    draw_static(window=gp.GAME_WINDOW, images=gp.IMAGES_AND_SIZES)
    draw_dynamic(window=gp.GAME_WINDOW, car_obj=all_cars)
    # key = pygame.key.get_pressed()
    # if key[pygame.K_c]:
    #     player_cars.append(PlayerCar(rotation_vel=2, start_pos_y=200, start_pos_x=200))
    #     time.sleep(0.5)
    cars2 = tre.next_step(cars2)
    # print(cars2[0].colide)
    if len(cars2) < 1000:
        cars2.append(ComputerCar(rotation_vel=10, start_pos_y=200, start_pos_x=250, max_velocity=10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("SAVED PATH:")
            tre.save_path_to_file()
            tre.save_path_to_file_pickle()
            pygame.quit()
            sys.exit()

# ancestors = Ancestors()
#
# for i in range(1000):
#     car = ComputerCar(rotation_vel=8, start_pos_y=200, start_pos_x=250, max_velocity=5)
#     cars2.append(car)
#
# while run:
#     timer.tick(FPS)
#     all_cars = cars2
#     draw_static(window=gp.GAME_WINDOW, images=gp.IMAGES_AND_SIZES)
#     draw_dynamic(window=gp.GAME_WINDOW, car_obj=all_cars)
#     # key = pygame.key.get_pressed()
#     # if key[pygame.K_c]:
#     #     player_cars.append(PlayerCar(rotation_vel=2, start_pos_y=200, start_pos_x=200))
#     #     time.sleep(0.5)
#     cars2 = ancestors.next_step(cars2)
#     # print(cars2[0].colide)
#     if len(cars2) == 0:
#         for i in range(500):
#             cars2.append(ComputerCar(rotation_vel=8, start_pos_y=200, start_pos_x=250, max_velocity=5))
#         # print(ancestors.set_of_sets_all)
#         ancestors.reduce_sets()
#         ancestors.who_to_follow(cars2)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
