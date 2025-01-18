# bd-2
Projekt z baz danych

## Kroki instalacji i uruchamiania projektu

### 1. Tworzenie wirtualnego środowiska
```bash
python3 -m venv venv
```

---

### 2. Aktywowanie wirtualnego środowiska
```bash
source venv/bin/activate
```

#### Alternatywne aktywacje dla różnych powłok:
- **csh (C Shell):**
  ```bash
  source venv/bin/activate.csh
  ```
- **fish (Fish Shell):**
  ```bash
  source venv/bin/activate.fish
  ```

---

### 3. Instalacja zależności projektu
```bash
python -m pip install flask python-dotenv psycopg2-binary bcrypt
```
- Instaluje wymagane biblioteki:
  - `flask`: Framework do budowy aplikacji webowych.
  - `python-dotenv`: Narzędzie do pracy z plikami `.env`, które przechowują zmienne środowiskowe.
  - `psycopg2-binary`: Biblioteka do komunikacji z bazą danych PostgreSQL.
  - `bcrypt`: Biblioteka do haszowania (szyfrowania) haseł.

---

### 4. Tworzenie pliku `.env`
```bash
cp .env.example .env
```
- Utworzenie pliku z konfiguracją środowiskową. Użytkownik może edytować ten plik, aby dostosować ustawienia, takie jak dane do bazy danych.

---

### 5. Tworzenie użytkownika bazy danych PostgreSQL
```bash
sudo -u postgres psql -a -c "CREATE USER ubiblioteka WITH PASSWORD '123454321';"
```

---

### 6. Tworzenie bazy danych PostgreSQL
```bash
sudo -u postgres psql -a -c "CREATE DATABASE biblioteka WITH OWNER ubiblioteka;"
```

---

### 7. Generowanie struktury bazy danych
```bash
python db_generator.py
```
- Automatyczne przygotowanie struktury bazy danych, aby aplikacja mogła z niej korzystać.
