import pygame
import os
from utils import resize_img


class GameParameters:
    """This class defines the static game parameters"""

    """Creating system paths to images"""
    RACE_TRACK_PATH = os.path.join("images", "racetrack1.png")
    RACE_TRACK_BORDER_PATH = os.path.join("images", "racetrack-borders.png")
    CAR_PATH = os.path.join("images", "carYellow.png")
    CAR_PATH2 = os.path.join("images", "car2.png")
    RACE_END_DEAD_PATH = os.path.join("images", "InkedMcQueen_DEAD_cp.jpg")
    FINISH_LINE_PATH = os.path.join("images", "finish_line.jpg")

    """Loading images to program and resizing images to fit them on screen"""
    RACE_TRACK_BORDER = resize_img(pygame.image.load(RACE_TRACK_BORDER_PATH), 1.1)
    RACE_TRACK_IMG = resize_img(pygame.image.load(RACE_TRACK_PATH), 1.1)
    CAR_IMG = resize_img(pygame.image.load(CAR_PATH), 0.04)
    CAR_IM4G = resize_img(pygame.image.load(CAR_PATH2), 0.04)
    RACE_TRACK_BORDER_MASK = pygame.mask.from_surface(RACE_TRACK_BORDER)
    RACE_END_DEAD = resize_img(pygame.image.load(RACE_END_DEAD_PATH), 1.2)
    FINISH_LINE = pygame.transform.rotate(resize_img(pygame.image.load(FINISH_LINE_PATH), 0.07), 90)
    FINISH_MASK = pygame.mask.from_surface(FINISH_LINE)
    WIDTH, HIGH = RACE_TRACK_IMG.get_width(), RACE_TRACK_IMG.get_height()
    GAME_WINDOW = pygame.display.set_mode((WIDTH, HIGH))

    """Setting static cords to objects on screen and adding them to lists that are displayed on the in-game screen"""
    IMG_CORD_X = 0
    IMG_CORD_Y = 0
    FINISH_X_CORD = 700
    FINISH_Y_CORD = 365
    FINISH_POS = (FINISH_X_CORD, FINISH_Y_CORD)
    IMAGES_AND_SIZES = [(RACE_TRACK_IMG, (IMG_CORD_X, IMG_CORD_Y)), (FINISH_LINE, (FINISH_X_CORD, FINISH_Y_CORD))]
    IMAGES_AND_SIZES_DEAD = [(RACE_END_DEAD, (IMG_CORD_X, IMG_CORD_Y))]

    #FONT = pygame.font.Font('freesansbold.ttf', 24)