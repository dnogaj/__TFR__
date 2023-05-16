![TFRoo](https://github.com/jd-kowal/__TFR__/assets/94318576/723ebdd8-38d8-4861-aa36-b27ad81c5377)

*** 

# ZADANIA  
* [Zadanie 1](#Zadanie-1)
* [Zadanie 2](#Zadanie-2)
* [Zadanie 3](#Zadanie-3)
* [Zadanie 4](#Zadanie-4)

Do prezentacji może przydać się [dokumentacja pygame-a][pg].

[pg]: https://www.pygame.org/docs/

## Zadanie 1 
1.	Korzystaj z biblioteki pygame. 
2.	Narysuj dowolny obrazek w Paint. 
3.	Stwórz okno gry o wymiarach 800x600 z tytułem <Twój numer indeksu>. 
4.	Wczytaj Twój obrazek i wyświetl go. 
5.	Przy naciśnięciu przycisku zamknięcia okna gry, zakończ program. 

### PROTIPY 
-	Skorzystaj z prezentacji #spoiler. 
-	Użyj pygame.image.load() do wczytania obrazu. 
-	Położenie obrazka definiujemy poprzez przekazanie w pikselach punktu, w którym znajduje się jego lewy górny róg. 
-	Funkcja pygame.display.set_mode() tworzy i zwraca okno gry o zadanym rozmiarze. 
-	Wykorzystaj screen.blit() do wyświetlenia obrazu na ekranie. 
-	Używając screen.fill() możesz zmienić kolor tła. 
-	Używając pygame.display.set_caption() ustawiasz tytuł okna gry. 
-	Funkcja pygame.display.flip() odświeża ekran. 
-	Uwaga: 'screen' jest przykładową nazwą obiektu okna gry, które stworzyłeś. Możesz ten obiekt nazwać inaczej jednakże należy wtedy uwzględnić tą zmianę w powyższych funkcjach. 

<br /> 
<br /> 

## Zadanie 2 
1.	Stwórz prostokąt o kolorze <>.  
2.	Wyświetl w tym prostokącie dowolny tekst o kolorze <> oraz czcionce <>. 
3.	Wewnątrz tego prostokąta, wyświetl dowolny tekst, również w dowolnym kolorze i czcionce. 
4.	Następnie napisz funkcję, która sprawdzi, czy przycisk został wciśnięty. Kiedy przycisk zostanie wciśnięty, poinformuj użytkownika o tym fakcie, na przykład wypisując tekst w konsoli (zobacz PROTIPY).  

### PROTIPY
-	Sprawdzaj pozycję myszy (czy pokrywa się z prostokątem) oraz czy lewy jej przycisk został wciśnięty.  
-	Wykorzystaj pygame.Rect do stworzenia przycisku: Prostokątne przyciski są najłatwiejsze do stworzenia w Pygame, ponieważ moduł ten zawiera klasę Rect służącą do reprezentowania prostokątów. Możesz utworzyć prostokąt o określonym rozmiarze i pozycji, a następnie użyć go jako przycisku. 
-	Wykorzystaj pygame.draw.rect do rysowania przycisku: Ta funkcja pozwala narysować prostokąt o określonym kolorze na powierzchni Pygame. Możesz użyć tej funkcji do narysowania ciała przycisku. 
-	Użyj pygame.font.Font.render do generowania tekstu: Ta metoda pozwala na generowanie obiektów tekstu, które mogą być następnie wyświetlane na ekranie za pomocą metody blit powierzchni Pygame. 
-	Wykorzystaj pygame.event.get do obsługi zdarzeń: Pygame generuje zdarzenia na podstawie akcji użytkownika, takich jak kliknięcia myszą. Możesz użyć tej metody, aby uzyskać listę wszystkich oczekujących zdarzeń i zareagować na nie w odpowiedni sposób. 
-	Sprawdź, czy przycisk został wciśnięty za pomocą metody collidepoint klasy Rect: Ta metoda sprawdza, czy dany punkt (tutaj pozycja myszy) jest w obrębie prostokąta. Możesz go użyć, aby sprawdzić, czy przycisk został wciśnięty.  
-	Pamiętaj o odświeżaniu ekranu za pomocą pygame.display.flip: Ta funkcja aktualizuje cały ekran, więc musisz ją wywoływać po każdej zmianie stanu ekranu (np. po narysowaniu przycisku). 
-	Pamiętaj o obsłudze zdarzenia QUIT: To zdarzenie jest generowane, gdy użytkownik próbuje zamknąć okno gry. Musisz obsłużyć to zdarzenie, zamykając Pygame i kończąc program, w przeciwnym razie gra będzie działać w nieskończoność.   

<br /> 
<br /> 

## Zadanie 3 
 



<br /> 
<br /> 
***


QUIZ
1)	Genetyczny – algorytm blokowy
•	
2)	Jakie funkcje w module PyGame pozwalają wyświetlać obiekty na ekranie?
•	Sd
3)	Podaj wszystkie zdania prawdziwe na temat algorytmu heurystycznego



Wyświetl dowolny napis na tle prostokąta o kolorze <>. Ustaw kolor tekstu <> oraz jego czcionkę <>. Następnie sprawdzaj kolizję (PROTIP: sprawdzaj pozycję myszy oraz czy lewy jej przycisk został wciśnięty). Dowolnie poinformuj użytkownika o wciśnięciu przycisku (może być to wypisanie w konsoli dowolnego tekstu).

