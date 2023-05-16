docs: https://www.pygame.org/docs/

ZADANIA  <br />
*** 
<br />
Zadanie 1 <br />
•	Korzystaj z biblioteki pygame. <br />
•	Narysuj dowolny obrazek w Paint. <br />
•	Stwórz okno gry o wymiarach 800x600 z tytułem <Twój numer indeksu>. <br />
•	Wczytaj Twój obrazek i wyświetl go. <br />
•	Przy naciśnięciu przycisku zamknięcia okna gry, zakończ program. <br />

> [!TIP]
PROTIPY <br />
•	Skorzystaj z prezentacji #spoiler. <br />
•	Użyj pygame.image.load() do wczytania obrazu. <br />
•	Położenie obrazka definiujemy poprzez przekazanie w pikselach punktu, w którym znajduje się jego lewy górny róg. <br />
•	Funkcja pygame.display.set_mode() tworzy i zwraca okno gry o zadanym rozmiarze. <br />
•	Wykorzystaj screen.blit() do wyświetlenia obrazu na ekranie. <br />
•	Używając screen.fill() możesz zmienić kolor tła. <br />
•	Używając pygame.display.set_caption() ustawiasz tytuł okna gry. <br />
•	Funkcja pygame.display.flip() odświeża ekran. <br />
•	Uwaga: 'screen' jest przykładową nazwą obiektu okna gry, które stworzyłeś. Możesz ten obiekt nazwać inaczej jednakże należy wtedy uwzględnić tą zmianę w powyższych funkcjach. <br />
>
*** 
<br /> 
PROTIPY <br />
•	Sprawdzaj pozycję myszy (czy pokrywa się z prostokątem) oraz czy lewy jej przycisk został wciśnięty. <br />
•	Wykorzystaj pygame.Rect do stworzenia przycisku: Prostokątne przyciski są najłatwiejsze do stworzenia w Pygame, ponieważ moduł ten zawiera klasę Rect służącą do reprezentowania prostokątów. Możesz utworzyć prostokąt o określonym rozmiarze i pozycji, a następnie użyć go jako przycisku. <br />
•	Wykorzystaj pygame.draw.rect do rysowania przycisku: Ta funkcja pozwala narysować prostokąt o określonym kolorze na powierzchni Pygame. Możesz użyć tej funkcji do narysowania ciała przycisku. <br />
•	Użyj pygame.font.Font.render do generowania tekstu: Ta metoda pozwala na generowanie obiektów tekstu, które mogą być następnie wyświetlane na ekranie za pomocą metody blit powierzchni Pygame. <br />
•	Wykorzystaj pygame.event.get do obsługi zdarzeń: Pygame generuje zdarzenia na podstawie akcji użytkownika, takich jak kliknięcia myszą. Możesz użyć tej metody, aby uzyskać listę wszystkich oczekujących zdarzeń i zareagować na nie w odpowiedni sposób. <br />
•	Sprawdź, czy przycisk został wciśnięty za pomocą metody collidepoint klasy Rect: Ta metoda sprawdza, czy dany punkt (tutaj pozycja myszy) jest w obrębie prostokąta. Możesz go użyć, aby sprawdzić, czy przycisk został wciśnięty. <br />
•	Pamiętaj o odświeżaniu ekranu za pomocą pygame.display.flip: Ta funkcja aktualizuje cały ekran, więc musisz ją wywoływać po każdej zmianie stanu ekranu (np. po narysowaniu przycisku). <br />
•	Pamiętaj o obsłudze zdarzenia QUIT: To zdarzenie jest generowane, gdy użytkownik próbuje zamknąć okno gry. Musisz obsłużyć to zdarzenie, zamykając Pygame i kończąc program, w przeciwnym razie gra będzie działać w nieskończoność. <br />
*** 
<br />
Zadanie 3 <br />





QUIZ
1)	Genetyczny – algorytm blokowy
•	
2)	Jakie funkcje w module PyGame pozwalają wyświetlać obiekty na ekranie?
•	Sd
3)	



Wyświetl dowolny napis na tle prostokąta o kolorze <>. Ustaw kolor tekstu <> oraz jego czcionkę <>. Następnie sprawdzaj kolizję (PROTIP: sprawdzaj pozycję myszy oraz czy lewy jej przycisk został wciśnięty). Dowolnie poinformuj użytkownika o wciśnięciu przycisku (może być to wypisanie w konsoli dowolnego tekstu).

