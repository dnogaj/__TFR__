import time

import pygame
import os
import sys
import math
import keyboard

from hive import Ants, Tre
from utils import resize_img, blit_rotate_center
from game.game_parameters import GameParameters as gp


class Game:



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
        IMG = gp.CAR_IM4G

        def __init__(self, rotation_vel, start_pos_x, start_pos_y, max_velocity):
            super().__init__(rotation_vel, start_pos_x, start_pos_y, max_velocity)

        def control(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                super().rotate(left=True)
            if keys[pygame.K_d]:
                super().rotate(right=True)
            if keys[pygame.K_w]:
                super().move()


    def draw_static(self, window, images: list):            #self
        window.fill((29, 130, 34))
        for image, position in images:
            window.blit(image, position)


    # def draw_dynamic(window, car_obj):
    #     for car in all_cars:
    #         car.draw_rotated_car(window)
    #         car.control()
    #         car.colision(gp.RACE_TRACK_BORDER_MASK)

    def draw_dynamic(self, window, all_cars):               #self
        for car in all_cars:
            car.draw_rotated_car(window)
            car.control()
            car.colision(gp.RACE_TRACK_BORDER_MASK)

        pygame.display.update()


    def play_algo(self):
        # car1 = PlayerCar(rotation_vel=2, start_pos_y=200, start_pos_x=200)
        run = True
        FPS = 300  # klatki na sekunde
        timer = pygame.time.Clock()  # tworzenie instancji zegara
        # player_cars = []
        # player_cars.append(PlayerCar(rotation_vel=2, start_pos_y=200, start_pos_x=200))
        cars2 = []
        cars2.append(self.ComputerCar(rotation_vel=2, start_pos_y=200, start_pos_x=200, max_velocity=10))            #self

        #size = gp.RACE_TRACK_IMG.get_size()        #unused
        #ants = Ants(size)                          #unused
        tre = Tre(1)

        while run:
            timer.tick(FPS)
            all_cars = cars2
            self.draw_static(window=gp.GAME_WINDOW, images=gp.IMAGES_AND_SIZES)         #self
            self.draw_dynamic(window=gp.GAME_WINDOW, all_cars=all_cars)                 #self
            # key = pygame.key.get_pressed()
            # if key[pygame.K_c]:
            #     player_cars.append(PlayerCar(rotation_vel=2, start_pos_y=200, start_pos_x=200))
            #     time.sleep(0.5)
            cars2 = tre.next_step(cars2)
            # print(cars2[0].colide)
            if len(cars2) < 1000:
                cars2.append(self.ComputerCar(rotation_vel=10, start_pos_y=200, start_pos_x=250, max_velocity=10))      #self

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # ants.show_matrix()
                    pygame.quit()
                    sys.exit()

    def play_solo(self):
        run = True
        FPS = 60  # klatki na sekunde
        timer = pygame.time.Clock()  # tworzenie instancji zegara

        player_car = []
        player_car.append(self.PlayerCar(rotation_vel=1, start_pos_y=200, start_pos_x=200, max_velocity=1))

        while run:
            timer.tick(FPS)
            self.draw_static(window=gp.GAME_WINDOW, images=gp.IMAGES_AND_SIZES)
            self.draw_dynamic(window=gp.GAME_WINDOW, all_cars=player_car)
            player_car[0].control()
            print(player_car[0].colide)
            if player_car[0].colide is not None:
                self.draw_static(window=gp.GAME_WINDOW, images=gp.IMAGES_AND_SIZES_DEAD)
                #gp.GAME_WINDOW.blit(gp.RACE_END_DEAD, dest=(0, 0))
                run = False
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # ants.show_matrix()
                    pygame.quit()
                    sys.exit()


        #time.sleep(10)
        #end_button = True
        #print(pygame.event.get())


        ##NOT WORKIN - im pissed little bit -> pbly small mistake
        while True:
            self.draw_static(window=gp.GAME_WINDOW, images=gp.IMAGES_AND_SIZES_DEAD)
            #gp.GAME_WINDOW.blit(gp.RACE_END_DEAD, dest=(0, 0))
            if keyboard.is_pressed('enter') or keyboard.is_pressed('esc'):
                break




        # gp.GAME_WINDOW.blit(gp.RACE_END_DEAD, dest=(0, 0))
        # while end_button:
        #     #if pygame.event.get():
        #         #end_button = False
        #     for event in pygame.event.get():
        #         print(event.type)
        #         # print(event.key)
        #         if event.type == 379 or event.type == 1024:
        #             end_button = False

        # for event in pygame.event.get():
        #     if event.type == QUIT:
        #         return
        #     elif event.type == KEYDOWN:
        #         if event.key == K_ESCAPE:
        #             return
