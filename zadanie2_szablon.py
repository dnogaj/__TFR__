import pygame
import sys

# Inicjowanie Pygame
pygame.init()

# TODO: Ustawienie rozmiarów okna
screen = pygame.display.set_mode((..., ...))

# TODO: Ustaw kolor przycisku

# TODO: Ustaw kolor tekstu

# TODO: Ustaw czcionkę

# TODO: Utwórz prostokąt reprezentujący przycisk


def check_button_pressed(mouse_pos):
    pass
    # TODO: Sprawdź, czy przycisk został wciśnięty, jeśli tak wyświetl wiadomość


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # TODO: Obsłuż zdarzenie kliknięcia myszą
        # TODO: Wypełnij tło kolorem
        # TODO: Narysuj przycisk
        # TODO: Wygeneruj tekst do wyświetlenia
        # TODO: Wyświetl tekst na przycisku
        # TODO: Odśwież ekran


if __name__ == "__main__":
    main()
