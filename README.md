# Zadanie
Napisz skrypt za pomocą framework'a Flask pobierający dane pogodowe z serwisu
*metaweather.com* dla zadanego *WOEID* (where on earth identifier).

Użyj Pythona w wersji 3.x.

Aplikacja powinna udostępniać jeden widok pod URI */update-forecast/:woe_id*,
gdzie *:woe_id* to parametr zadany przez użytkownika.

Po wykonaniu zapytania typu *POST* na ww. widok aplikacja powinna wykonać
zapytanie o dane pogodowe i następnie zapisać je w formacie *CSV* na dysku.

Dane powinny zostać pobrane za pomocą zapytania *GET* na adres
*https://www.metaweather.com/api/location/(woeid)/*.

Przykładowe *WOEID*:
- Berlin 638242
- Warszawa 523920
- San Francisco 2487956

[Dokumentacja](https://www.metaweather.com/api/)

Dane te powinny zostać zapisane w następującej strukturze katalogów:
```
katalog, na który wskazuje zmienna *FORECASTS_DIR*
└── katalog o nazwie *WOEID*, w nim będą przechowywane rezultaty wszystkich
    zapytań pod to *WOEID*.
    └── katalog, który w nazwie ma datę wykonania zapytań, np. 03-11-2017.
        └── pliki .csv, które w nazwie mają czas wykoania zapytania,
            np. 12-35-44.csv
```
Przykładowa struktura:
```
forecasts
└── 523920
    ├── 06-11-2017
    │   ├── 17-03-09.csv
    │   └── 17-03-11.csv
    └── 07-11-2017
        ├── 09-29-08.csv
        ├── 09-29-09.csv
        └── 09-29-17.csv
```

Szablon aplikacji został już przygotowany. Zadanie polega na wypełnieniu kodem
odpowiednich metod/funkcji. Wraz z szablonem dostarczono odpowiednie testy.
Zadanie zostanie uznane za rozwiązane jeżeli przechodzi w wszystkie testy. Aby
uruchomić testy należy wykonać polecenie `pytest -vv`.

Ważne! Nie zmieniaj nazw funkcji/method, gdyż to będzie miało wpływ na wykonanie
testów. Możesz oczywiście dopisać swoje dodatkowe funkcje/metody, z których
będziesz korzystał.

Skorzystaj ze zmiennych w pliku *settings.py*.
