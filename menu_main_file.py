# Find/Use Mouse Position in Pygame
import pygame
import game_main_fun
import game_main_fun as gmf


class Menu:
    pygame.init()

    # WIDTH = 950
    # HEIGHT = 540
    # screen = pygame.display.set_mode([WIDTH, HEIGHT])
    # font = pygame.font.Font('freesansbold.ttf', 24)

    def __init__(self):
        #pygame.init()
        #self.WIDTH = 950
        #self.HEIGHT = 540
        self.WIDTH = 1400
        self.HEIGHT = 860   #800
        self.fps = 60
        self.timer = pygame.time.Clock()
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        pygame.display.set_caption('Menus TFR')
        self.main_menu = False
        self.font = pygame.font.Font('freesansbold.ttf', 24)
        #bg = pygame.transform.scale(pygame.image.load('zygzzlom.jpg'), (WIDTH, HEIGHT))
        self.bg = pygame.transform.scale(pygame.image.load('images/autaRace.jpg'), (self.WIDTH, self.HEIGHT))
        self.ball = pygame.transform.scale(pygame.image.load('images/tfrBallLogo.png'), (150, 150))
        self.background = pygame.transform.scale(pygame.image.load('images/CarsOldOne.webp'), (self.WIDTH, self.HEIGHT))
        self.menu_command = 0



    class Button:
        def __init__(self, txt, pos, screen, font):
            self.text = txt
            self.pos = pos
            self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (230, 40))   #WIDTH/3
            self.screen = screen
            self.font = font

        def draw(self):
            pygame.draw.rect(self.screen, 'light gray', self.button, 0, 5)
            pygame.draw.rect(self.screen, 'dark gray', [self.pos[0], self.pos[1], 230, 40], 5, 5)
            text2 = self.font.render(self.text, True, 'black')
            self.screen.blit(text2, (self.pos[0] + 100 - len(self.text)*10, self.pos[1] + 7))

        def check_clicked(self):
            if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                return True
            else:
                return False

    class Conf_Game:
        def __init__(self, map, car):
            self.map = map
            self.car = car

    def draw_menu(self):
        self.screen.blit(self.bg, (0, 0))
        command = -1
        pygame.draw.rect(self.screen, 'black', [50, 100, 300, 300])
        #screen.blit(bg, (100, 100))
        pygame.draw.rect(self.screen, 'green', [50, 100, 300, 300], 5)
        pygame.draw.rect(self.screen, 'white', [70, 120, 260, 40], 0, 5)
        pygame.draw.rect(self.screen, 'gray', [70, 120, 260, 40], 5, 5)
        txt = self.font.render('Menus!', True, 'black')
        self.screen.blit(txt, (135, 127))
        # menu exit button
        menu = self.Button('Exit Menu', (85, 350), self.screen, self.font)
        menu.draw()
        play_button = self.Button('Play', (85, 180), self.screen, self.font)
        play_button.draw()
        options_button = self.Button('Options', (85, 240), self.screen, self.font)
        options_button.draw()
        random_button = self.Button('Randomize', (85, 300), self.screen, self.font)
        random_button.draw()
        if menu.check_clicked():
            command = 0
        if play_button.check_clicked():
            command = 1
        if options_button.check_clicked():
            command = 2
        if random_button.check_clicked():
            command = 3
        return command


    def draw_game(self):
        menu_btn = self.Button('Main Menu', (self.WIDTH/2 - 75, self.HEIGHT - 100), self.screen, self.font)
        menu_btn.draw()
        menu = menu_btn.check_clicked()
        self.screen.blit(self.ball, (200, 670))
        return menu


    def draw_game_conf(self):

        pass

    def switch_pages(x):
        #match x:
         #   case 1:


          #  pass
        pass


    def menus(self):
        #main_menu = self.main_menu
        run = True
        while run:
            #screen.fill('light blue')
            #print("ruuuuuun   " + str(self.main_menu))
            self.screen.blit(self.background, (0, 0))
            self.timer.tick(self.fps)
            if self.main_menu:
                #print("secooooooond   " + str(self.main_menu))
                self.menu_command = self.draw_menu()
                if self.menu_command != -1:
                    self.main_menu = False
            else:
                #print("alkjsdhslakhdjklahjsd   " + str(self.main_menu))
                self.main_menu = self.draw_game()
                if self.menu_command > 0:
                    #print("alk-----------------------jsdhslakhdjklahjsd   " + str(self.main_menu))
                    self.text = self.font.render(f'Button {self.menu_command} pressed!', True, 'black')
                    #print(self.menu_command)
                    self.screen.blit(self.text, (150, 100))
                    if self.menu_command == 1:
                        pygame.display.flip()
                        #pygame.quit()
                        game = gmf.Game()
                        game.play()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.flip()
        pygame.quit()
