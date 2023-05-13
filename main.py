# import menu_main_file as menu
from menu.main_menu import MainMenu
from game.game_parameters import GameParameters as gp


if __name__ == "__main__":
    print("Hello Mello Alermeko")
    print("assalamu alaikum")
    # menu_check = menu.MainMenu()
    # menu_check.menus()

    menu_start = MainMenu()
    menu_start.menus()
