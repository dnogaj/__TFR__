![TFRoo](https://github.com/jd-kowal/__TFR__/assets/94318576/723ebdd8-38d8-4861-aa36-b27ad81c5377)

*** 

# ZADANIA  
* [Zadanie 1](#Zadanie-1)
* [Zadanie 2](#Zadanie-2)
* [Zadanie 3](#Zadanie-3)
* [Zadanie 4](#Zadanie-4)

<br /> 

Do prezentacji może przydać się [dokumentacja pygame-a][pg].

[pg]: https://www.pygame.org/docs/

<br /> 
Korzystaj z sekcji ```PROTIPY```.
<br /> 
<br /> 

## Zadanie 1 
1.	Korzystaj z biblioteki pygame. 
2.	Narysuj dowolny obrazek w Paint. 
3.	Stwórz okno gry o wymiarach 800x600 z tytułem <Twój numer indeksu>. 
4.	Wczytaj Twój obrazek i wyświetl go. 
5.	Przy naciśnięciu przycisku zamknięcia okna gry, zakończ program. 

#### PROTIPY 
-	Skorzystaj z prezentacji #spoiler. 
-	Użyj ```pygame.image.load()``` do wczytania obrazu. 
-	Położenie obrazka definiujemy poprzez przekazanie w pikselach punktu, w którym znajduje się jego lewy górny róg. 
-	Funkcja ```pygame.display.set_mode()``` tworzy i zwraca okno gry o zadanym rozmiarze. 
-	Wykorzystaj ```screen.blit()``` do wyświetlenia obrazu na ekranie. 
-	Używając ```screen.fill()``` możesz zmienić kolor tła. 
-	Używając ```pygame.display.set_caption()``` ustawiasz tytuł okna gry. 
-	Funkcja ```pygame.display.flip()``` odświeża ekran. 
-	Uwaga: 'screen' jest przykładową nazwą obiektu okna gry, które stworzyłeś. Możesz ten obiekt nazwać inaczej jednakże należy wtedy uwzględnić tą zmianę w powyższych funkcjach. 

<br /> 
<br /> 

## Zadanie 2 
1.	Stwórz prostokąt o dowolnym kolorze.  
2.	Wewnątrz tego prostokąta, wyświetl dowolny tekst, również o dowolnym kolorze i czcionce. 
3.	Następnie napisz funkcję, która sprawdzi, czy przycisk został wciśnięty. Kiedy przycisk zostanie wciśnięty, poinformuj użytkownika o tym fakcie, na przykład wypisując tekst w konsoli (zobacz PROTIPY).  

#### PROTIPY
-	Sprawdzaj pozycję myszy (czy pokrywa się z prostokątem) oraz czy lewy jej przycisk został wciśnięty.  
-	Wykorzystaj ```pygame.Rect``` do stworzenia przycisku: Prostokątne przyciski są najłatwiejsze do stworzenia w Pygame, ponieważ moduł ten zawiera klasę Rect służącą do reprezentowania prostokątów. Możesz utworzyć prostokąt o określonym rozmiarze i pozycji, a następnie użyć go jako przycisku. 
-	Wykorzystaj ```pygame.draw.rect()``` do rysowania przycisku: Ta funkcja pozwala narysować prostokąt o określonym kolorze na powierzchni Pygame. Możesz użyć tej funkcji do narysowania ciała przycisku. 
-	Użyj ```pygame.font.Font.render()``` do generowania tekstu: Ta metoda pozwala na generowanie obiektów tekstu, które mogą być następnie wyświetlane na ekranie za pomocą metody blit powierzchni Pygame. 
-	Wykorzystaj ```pygame.event.get()``` do obsługi zdarzeń: Pygame generuje zdarzenia na podstawie akcji użytkownika, takich jak kliknięcia myszą. Możesz użyć tej metody, aby uzyskać listę wszystkich oczekujących zdarzeń i zareagować na nie w odpowiedni sposób. 
-	Sprawdź, czy przycisk został wciśnięty za pomocą metody collidepoint klasy Rect: Ta metoda sprawdza, czy dany punkt (tutaj pozycja myszy) jest w obrębie prostokąta. Możesz go użyć, aby sprawdzić, czy przycisk został wciśnięty.  
-	Pamiętaj o odświeżaniu ekranu za pomocą ```pygame.display.flip()```: Ta funkcja aktualizuje cały ekran, więc musisz ją wywoływać po każdej zmianie stanu ekranu (np. po narysowaniu przycisku). 
-	Pamiętaj o obsłudze zdarzenia QUIT: To zdarzenie jest generowane, gdy użytkownik próbuje zamknąć okno gry. Musisz obsłużyć to zdarzenie, zamykając Pygame i kończąc program, w przeciwnym razie gra będzie działać w nieskończoność.   

<br /> 
<br /> 

<br /> 
<br /> 

## Zadanie 3 
1. Pobierz nasz projekt.
2. Wyszukaj komentarze ```ZADANIE``` w module Tre w paczce algorythm.
3.  ```self.strength_path``` to zmienna pomocnicza, aby nie mnożyć kodu. Odpowiada ona za wzmacnianie ścieżki. Jej dokładne zastosowanie zależy od waszej implementacji.
4. W liniach z komentarzami trzeba uzupełnić kod odpowiadający za wzmacnianie i osłabianie się ścieżki.
5. Spróbuj doprowadzić algorytm do momentu, w którym będziesz widział, że kolejne samochodziki pokonują więcej zakrętów niż poprzednie.
6. Zescreenuj wynik w postaci samochodzików, które dojechały do drugiego zakrętu o 180 stopni. Możesz dodać również screena funkcji ```function()``` oraz ```purge_path()```.

#### PROTIPY
-	Wartość zmiennej ```self.strength_path``` ma wbrew pozorom spore znaczenie. Jeśli Ci nie działa, to niekoniecznie błąd musi znajdować się funkcjach.
-	Nie martw się, zadanie nie jest takie trudne, na jakie wygląda :))

<br /> 
<br /> 

## Zadanie 4
1. Korzystając również z naszego projektu, wyszukaj komentarze ```ZADANIE``` w module Ancestors w paczce algorythm.
2. ```self.max_sets``` to zmienna, która zachowuje maksymalną ilość ścieżek, za którą będzie podążać następna generacja.
3. ```self.base_unfollow_probability``` - jest to szansa na zejście ze ścieżki w ostatnim zapisanym kroku.
4. W funkcji ```who_to_follow()``` ustaw ```car.jump``` pożądaną szansę zejścia ze ścieżki w pierwszym kroku samochodzika (kod ten wykonuje się tylko raz na początku istnienia kolejnego pokolenia). 
5. W funkcji ```next_step()``` zmieniaj ```car.jump``` w kolejnych krokach programu.

#### PROTIPY
- ```car.jump``` jest to szansa na zeskoczenie ze ścieżki.
-	Prawdopodobieństwo zejścia ze ścieżki powinno rosnąć.
-	```self.base_unfollow_probability``` może być użyte w inny niż opisany sposób.

