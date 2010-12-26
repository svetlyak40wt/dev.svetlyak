Title: Переезжаю на российский Django хостинг.
Slug: russian-django-hosting
Date: 2010-03-02 08:40
Category: texts
Tags: life, hosting
Lang: ru

Подумываю переехать на российский Django хостинг. Но только не могу пока
выбрать, брать ли VPS или все-таки попробовать ужиться в общежитии shared
хостинга.

Вчера я зарегистрировал тестовый shared аккаунт на [locum.ru][1] (надо отдать
должное, ребята сделали все отлично, весь процесс занимает мунуту) и
попробовал перевезти маленький сайтик любимой. Сайт-заглушка, использующий
Django, у них создается за минуту. А вот для переноса моего хозяйства пришлось
чуть чуть повозиться.

Во-первых, логирование у ребят включается по запросу в службу техподдержки. А
без логирования сложно понять почему не взлетает WSGI приложение.

Во-вторых, потребовались некоторые манипуляции с django.wsgi, чтобы запускать
именно мою Django, из virtualenv а не расшареную, которую могут проапгрейдить
в любой момент. Дописал в django.wsgi такие строчки, и все заработало:

    :::python
    activation_script = \
        os.path.expanduser('~/env/martemenko/bin/activate_this.py')

    execfile(activation_script, dict(__file__= activation_script ))

Итог теста с помощью ab -c 10 -n 1000 показал, что с российского хостинга
странички отдаются примерно в 2.5 раза быстрее, чем с VPS тектоника. Буду
потихоньку переезжать если получится запустить [svetlyak.ru][2] на shared
хостинге.

[1]: http://locum.ru
[2]: http://svetlyak.ru