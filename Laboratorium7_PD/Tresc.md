# Zadanie 1
Stworzyć klasę <i>Polynomial</i> reprezentującą wielomian o współczynnikach całkowitych. Klasa ma posiadać następujące metody:
<ul>
<li>konstruktor z jednym parametrem będącym kolekcją par opisujących składniki wielomianu (wartość potęgi X i współczynnik), wartością domyślną dlatego parametru ma być kolekcja pusta (jako błąd -zgłaszany wyjątek ValueError -ma być traktowane: podanie współczynnika o wartości zero, podanie ujemnej lub powtórzonej wartości potęgi X,</li>
<li>_str_-zwracająca tekst opisujący wielomian (zgodnie z przykładami na końcu zadania),</li>
<li>degree-zwracająca stopień wielomianu,</li>
<li>coefficient-zwracająca współczynnik przy X w potędze podanej jako parametr metody,</li>
<li>value-zwracającą wartość wielomiany dla podanej wartości X,</li>
<li>add-dodającą dwa wielomiany,</li>
<li>subtract-odejmującą dwa wielomiany.</li>
</ul>
<p>
Wielomian może być bardzo wysokiego stopnia i może posiadaćbardzo mało współczynników. Wewnętrznie należy więc przechowywać tylko te współczynniki, które maja wartość różną od zera (przy wykonywaniu operacji dodawania lub odejmowania, w wynikowym wielomianie nie może być współczynników o wartościach równych 0).<br /><br />
Przykłady<br />
Parametry konstruktora i odpowiadające im wielomiany:
<p>
  [(0,-8)]-'-8'<p>
  [(0,4),(1,-2)]-'-2x+4'<p>
  [(1,5),(3,2),(5,-1)]-'-x^5+2x^3+5x'<p>
  [(4,2),(6,3),(2,3),(0,7)]-'3x^6+2x^4+3x^2+7'<p>
  [(1,5),(3,0),(5,-1)]-błąd<p>
  [(1,5),(-3,7),(5,-1)]-błąd<p><br /><br />
Przykładowe napisy opisujące wielomian<p>
  '-8'<p>
  '-2x+4'<p>
  '-x^5+2x^3+5x'<p>
  '3x^6+2x^4+3x^2+7'<p>
  '2x^7+3x^5+3x^3-3x+2'<p>
  'x^234+3x^5+3x^3-3x^2-3x+7'<p><br /><br />
Przykład dodawania dwóch wielomianów<p>
  2x^7+3x^3+3x^2-5`+3x^5-3x^3'='2x^7+3x^5+3x^2-5'<p>
  Podpowiedź: do obliczania wartości wielomianu można zastosować schemat Hornera
