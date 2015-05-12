Postup instalace
==============

Vytvoření databáze a superuživatele proběhne následujícím způsobem:

    python3 manage.py migrate
    python3 manage.py createsuperuser

Spuštění aplikace
===============

Pro spuštění vestavěného web serveru lze použít příkaz:

    python3 manage.py runserver <ip>:<port>

IP může být 0.0.0.0 pro bind na všechno.
