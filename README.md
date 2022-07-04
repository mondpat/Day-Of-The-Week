# Day-Of-The-Week
Konzolový program pro výpočet dne v týdnu, dle zadaného data.
Projekt sestává z několika funkcí:
- JsouDataStejná - Vrátí true, pokud jsou v parametrech při volání vloženy stejné dny a měsíce.
- PočetDní - Vrátí počet dní od počátku roku až do zadaného dne a měsíce.
- JeRokPřestupný - Zkontroluje zda je rok zadaný jako parametr při volání přestupný. Pokud ano, vrátí true.
- PočetDníZaRoky - Vypočítá počet dní od roku 1 do zadaného roku (přestupné roky se počítají souběžně s nepřestupnými).

Potom, co program vypočítal počet dní od roku 1 až do zadaného data, určí den v týdnu podle zbytku po dělení 7.
