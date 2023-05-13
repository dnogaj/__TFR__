import time

import pygame
import os
import sys
import math
import keyboard

from hive import Ants, Tre, Ancestors
from utils import detect_stat_dyn_collide
from game.game_parameters import GameParameters as gp
from game.cars import PlayerCar, ComputerCar


class Game:
    """Modulacja z funkcjami pygame -> dużo miesza bo razem z załadowaniem obrazka długi ciąg się robi"""

    @staticmethod
    def draw_static(window, images: list):
        window.fill((29, 130, 34))
        for image, position in images:
            window.blit(image, position)

    @staticmethod
    def draw_static_algo2(window, images: list, timer, generation_counter):
        """draw_static_algo2 -> draws board (track and satatic fragments) for play_algo_v2"""
        window.fill((29, 130, 34))
        for image, position in images:
            window.blit(image, position)
        font = pygame.font.Font("freesansbold.ttf", 32)
        time_counter = font.render("Time  ->  " + str(round(time.time() - timer, 3)), True, "white")
        gp.GAME_WINDOW.blit(time_counter, (800, 200))
        generation_counter = font.render("Count  ->  " + str(generation_counter), True, "white")
        gp.GAME_WINDOW.blit(generation_counter, (800, 160))
        # time_counter = Button('timer', (Button.WIDTH/2 - 75, Button.HEIGHT - 100), Button.screen, Button.font)
        # time_counter.draw()
        # text = font.render("Randomized Game Option  ->  " + str(timer), True, 'white')
        # self.screen.blit(self.text, (150, 100))

    @staticmethod
    def draw_static_algo1(window, images: list, timer):
        """draw_static_algo1 -> draws board (track and satatic fragments) for play_algo"""
        window.fill((29, 130, 34))
        for image, position in images:
            window.blit(image, position)
        font = pygame.font.Font("freesansbold.ttf", 32)
        time_counter = font.render("Time  ->  " + str(round(time.time() - timer, 3)), True, "white")
        gp.GAME_WINDOW.blit(time_counter, (800, 200))

    @staticmethod
    def draw_static_solo(window, images: list, timer):
        """draw_static_solo -> draws board (track and satatic fragments) for play_solo"""
        window.fill((29, 130, 34))
        for image, position in images:
            window.blit(image, position)
        font = pygame.font.Font("freesansbold.ttf", 32)
        time_counter = font.render("Time  ->  " + str(round(time.time() - timer, 3)), True, "white")
        gp.GAME_WINDOW.blit(time_counter, (800, 200))

    @staticmethod
    def draw_static_info(window, images: list):
        """draw_static_info -> draws information how to start game and how to exit it"""
        window.fill((29, 130, 34))
        for image, position in images:
            window.blit(image, position)
        font = pygame.font.Font("freesansbold.ttf", 32)
        text = font.render("To start game press ENTER", True, "white")
        gp.GAME_WINDOW.blit(text, (800, 160))
        text = font.render("To exit game press ESC", True, "white")
        gp.GAME_WINDOW.blit(text, (800, 200))

    @staticmethod
    def draw_dynamic(window, all_cars):
        for car in all_cars:
            car.draw_rotated_car(window)
            car.control()
            col = car.collision(gp.RACE_TRACK_BORDER_MASK)
        #     print(f"border: {col[0]}")

        pygame.display.update()

    @staticmethod
    def play_algo():
        """play_algo -> first algorithm that overcomes the track by itself"""
        # car1 = PlayerCar(rotation_vel=2, start_pos_y=200, start_pos_x=200)
        run = True
        FPS = 300  # klatki na sekunde
        timer = pygame.time.Clock()  # tworzenie instancji zegara
        # player_cars = []
        # player_cars.append(PlayerCar(rotation_vel=2, start_pos_y=200, start_pos_x=200))
        cars2 = []
        cars2.append(
            ComputerCar(rotation_vel=2, start_pos_y=380, start_pos_x=750, max_velocity=10)
        )  # self

        # size = gp.RACE_TRACK_IMG.get_size()        #unused
        # ants = Ants(size)                          #unused
        tre = Tre(1)
        stime = time.time()

        while run:
            timer.tick(FPS)
            all_cars = cars2
            Game.draw_static_algo1(
                window=gp.GAME_WINDOW, images=gp.IMAGES_AND_SIZES, timer=stime
            )  # self
            Game.draw_dynamic(window=gp.GAME_WINDOW, all_cars=all_cars)  # self
            # key = pygame.key.get_pressed()
            # if key[pygame.K_c]:
            #     player_cars.append(PlayerCar(rotation_vel=2, start_pos_y=200, start_pos_x=200))
            #     time.sleep(0.5)
            cars2 = tre.next_step(cars2)
            # print(cars2[0].colide)
            if len(cars2) < 1000:
                cars2.append(
                    ComputerCar(rotation_vel=10, start_pos_y=380, start_pos_x=750, max_velocity=10)
                )  # self

            if keyboard.is_pressed("esc"):  # esc closing application
                run = False

            Game.exit_game()
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         # ants.show_matrix()
            #         pygame.quit()
            #         sys.exit()

    @staticmethod
    def exit_game():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    @staticmethod
    def play_solo():
        """play_solo -> main loop function for driving a car and trying to cross the finish line"""
        run = True
        FPS = 60  # klatki na sekunde
        timer = pygame.time.Clock()  # tworzenie instancji zegara

        player_car = []
        player_car.append(
            PlayerCar(rotation_vel=1, start_pos_y=380, start_pos_x=750, max_velocity=1)
        )

        # while True:
        #     timer.tick(FPS)
        #     Game.draw_static_info(window=gp.GAME_WINDOW, images=gp.IMAGES_AND_SIZES)
        #     keys = pygame.key.get_pressed()
        #     #time.sleep(2)
        #     if keys[pygame.K_KP_ENTER] or keys[pygame.K_SPACE]:
        #         break
        # TU MIAŁ BYĆ EKRAN NACIŚNIJ PRZYCISK ABY ZACZĄĆ

        stime = time.time()
        while run:
            timer.tick(FPS)
            Game.draw_static_solo(window=gp.GAME_WINDOW, images=gp.IMAGES_AND_SIZES, timer=stime)
            Game.draw_dynamic(window=gp.GAME_WINDOW, all_cars=player_car)
            player_car[0].control()
            # print(player_car[0].collide)
            car_pos = (player_car[0].x_cord, player_car[0].y_cord)
            finish_pos = (gp.FINISH_X_CORD, gp.FINISH_Y_CORD)
            collision_with_meta = detect_stat_dyn_collide(
                gp.FINISH_LINE, player_car[0].IMG, car_pos, finish_pos
            )
            etime = time.time()
            if collision_with_meta and (etime - stime) > 2.0:
                while run:
                    Game.draw_static(window=gp.GAME_WINDOW, images=gp.IMAGES_AND_SIZES_DEAD)
                    pygame.display.update()
                    Game.exit_game()
                    if keyboard.is_pressed("enter"):
                        Game.play_solo()
                    elif keyboard.is_pressed("esc"):
                        run = False
            if player_car[0].collide is not None:
                while run:
                    Game.draw_static_info(window=gp.GAME_WINDOW, images=gp.IMAGES_AND_SIZES_DEAD)
                    pygame.display.update()
                    Game.exit_game()
                    if keyboard.is_pressed("enter"):
                        Game.play_solo()
                    elif keyboard.is_pressed("esc"):
                        run = False

            Game.exit_game()

    @staticmethod
    def play_algo_v2():
        """play_algo_v2 -> second algorithm that overcomes the track by itself"""
        ancestors = Ancestors()

        run = True
        FPS = 60  # klatki na sekunde
        timer = pygame.time.Clock()  # tworzenie instancji zegara

        cars2 = []

        for i in range(1000):
            car = ComputerCar(rotation_vel=8, start_pos_y=380, start_pos_x=750, max_velocity=5)
            cars2.append(car)

        time_counter = time.time()
        generation_counter = 1

        while run:
            timer.tick(FPS)
            all_cars = cars2
            Game.draw_static_algo2(
                window=gp.GAME_WINDOW,
                images=gp.IMAGES_AND_SIZES,
                timer=time_counter,
                generation_counter=generation_counter,
            )
            Game.draw_dynamic(window=gp.GAME_WINDOW, all_cars=all_cars)
            # key = pygame.key.get_pressed()
            # if key[pygame.K_c]:
            #     player_cars.append(PlayerCar(rotation_vel=2, start_pos_y=200, start_pos_x=200))
            #     time.sleep(0.5)
            cars2 = ancestors.next_step(cars2)
            # print(cars2[0].colide)
            if len(cars2) == 0:
                for i in range(500):
                    cars2.append(
                        ComputerCar(
                            rotation_vel=8, start_pos_y=380, start_pos_x=750, max_velocity=5
                        )
                    )
                # print(ancestors.set_of_sets_all)
                ancestors.reduce_sets()
                ancestors.who_to_follow(cars2)
                generation_counter += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # ants.show_matrix()
                    pygame.quit()
                    sys.exit()
