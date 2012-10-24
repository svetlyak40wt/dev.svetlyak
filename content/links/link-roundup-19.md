Title: Link Roundup #19
Slug: link-roundup-19
Date: 2012-10-24 19:04
Category: links
Tags: roundup
Lang: ru

Разработка
----------
* [Pattern](https://github.com/clips/pattern) — подборка средств для дата-майнинга, включает в себя веб-паука, разные парсеры и реализацию алгоритмов машинного обучения. Внятного туториала, как этим пользоваться, я у них не нашел, но кому надо — разберется :) #machine-learning #python
* [Скрипт для генерации](https://github.com/mwhite/resume) резюме в PDF и HTML из Markdown. #command-line #python
* [Syte](https://github.com/rigoneri/syte/) — Django приложение, позволяющее подтягивать ваши данные из разных соц-сетей. Полезно для собственных бложиков, чтобы показывать расширенный профиль автора. Поддерживает Twitter, GitHub, Dribbble, Instagram, Foursquare, Tumblr, Last.fm, SoundCloud и Bitbucket. #django
* [Docopt](https://github.com/docopt/docopt) — очень интересная библиотека для парсинга аргументов командной строки. Не надо кодить сам парсер — достаточно лишь написать help к вашей программе! Как я понял, есть [реализации](https://github.com/docopt) для разных языков: #ruby #coffee #lua #C #PHP #python
* [Tox](http://tox.testrun.org/latest/) — утилита для автоматического тестирования Python модулей под разными интерпретаторами. А вот слайды [про продвинутое использование tox](http://farmdev.com/talks/tox/). Я уже прикрутил его к [TheBot](http://bitly.com/40wt-thebot), работает замечательно! #python #tools #unittesting
* Модуль [more-itertools](http://packages.python.org/more-itertools/api.html) содержит функции для работы с итераторами, дополняющими itertools из стандартной библиотеки. #python #libs
* Часто ли вы создаете новые Python модули? Я нет. Но видимо, Винсент Дриессен очень часто. Он даже command-line хелперы сделал для удобства, и назвал их [python-fu](https://github.com/nvie/python-fu). #python
* [Метрики машинного обучения](https://github.com/benhamner/Metrics), для языков #python  #R #Haskell #matlab #octave
* [nanomsg](https://github.com/250bpm/nanomsg) — кому-то не сидится на месте, и он начал клепать клон ZeroMQ. И тоже на C. Проект совсем свеженький — первый коммит от 10 октября. На мой вопрос, чем же будет отличаться nanomsg от ZeroMQ, разработчик выдал длинную тираду на тему: "Ну, у меня все будет реализовано очень просто…" а далее, описание того, что его nanomsg будет поддерживать и подключаемые транспорты, и какие-то паттерны, и еще кучу всего. Как я понял, "просто" не будет :) #develop #c #messaging
* [Python-reloader](https://github.com/jparise/python-reloader) — умный перезагрузчик python модулей. #python
* Пост про то, [как выделить доминирующие цвета](http://charlesleifer.com/blog/using-python-and-k-means-to-find-the-dominant-colors-in-images/) в изображении с помощью алгоритма k-means. Реализация на #python

Фронтэнд
--------
* [cssConsole](https://github.com/michalkow/cssConsole) — прикольный, но на мой взгляд бесполезный jQuery плагин, реализующий поле ввода, мимикрирующее под консоль. #jquery #plugin
