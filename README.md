Postup instalace
==============

Vytvoření databáze a superuživatele proběhne následujícím způsobem:

    $ python manage.py migrate
    $ python manage.py createsuperuser

Spuštění aplikace
===============

Pro spuštění vestavěného web serveru lze použít příkaz:

    $ python manage.py runserver <ip>:<port>

IP může být 0.0.0.0 pro bind na všechno.

Django
=====

Pokud na cílovém stroji není nainstalován framework Django a není možné
jej nainstalovat běžným způsobem (balíčkovací systém, pip), tak je
možné jej získat například následujícím způsobem:

    $ wget -O django.tar.gz https://www.djangoproject.com/download/1.8.1/tarball/
    $ tar xzf django.tar.gz
    $ cd Django-*
    $ python setup.py install --user
