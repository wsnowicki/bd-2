# bd-2
Projekt z baz danych


## Uruchamianie
1. Zainstaluj wymagane pakiety Pythonowe:
    - flask
    - python-dotenv
    - psycopg2-binary (postgresql)
lub ich alternatywy

2. Utwórz bazę danych oraz użytkownika w postgresie:

Na systemie Linux:
```bash
python3 db_generator.py
```
lub na systemie Windows:
```bat
py db_generator.py
```

3. Utwórz plik .env i wypełnij go odpowiednimi ustawieniami dla twoich potrzeb.
```bash
cp .env.example .env
vim .env
```

