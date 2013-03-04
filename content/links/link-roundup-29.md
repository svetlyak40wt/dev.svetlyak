Title: Link Roundup #29
Slug: link-roundup-29
Date: 2013-03-04 12:36
Category: links
Tags: roundup
Lang: ru

Разработка
----------

* [Статейка про подписывание Python пакетов PGP подписью](http://www.davidfischer.name/2012/05/signing-and-verifying-python-packages-with-pgp/). Насквозь пронизана болью от того, что никто этого не делает. #python #develop
* [Squash.io](http://squash.io/) — система для аггрегации логов, типа Sentry, более фичастый, но менее раскрученный. #develop #backend
* [Сравнение PyPy с CPython](http://rz.scale-it.pl/2013/02/18/wikipedia_processing._PyPy_vs_CPython_benchmark.html) на более-меннее реальных задачах по работе с базами и парсинге данных. PyPy быстрее CPython в несколько раз, даже при том, что для последнего используются библиотеки с сишными расширениями. #develop #python #pypy
* Подробное [описание возможных уязвимостей в xml библиотеках](http://blog.python.org/2013/02/announcing-defusedxml-fixes-for-xml.html). #develop #security #python
* Для Django вышел [секурити апдейт](https://www.djangoproject.com/weblog/2013/feb/19/security/). Всем обновляться до 1.3.7, 1.4.5 или 1.5rc2. #develop #django #security
* А вот эта ссылка, [специально для тех извращенцев, которые не могут жить без функционального программирования](https://github.com/kachayev/fn.py), но вынуждены использовать Python :) #python #functional
* [django-db-tools](http://craigkerstiens.com/2013/02/08/django-read-only-mode/) — простой модуль для переключения вашего Django сайта в read-only режим. Но даже с ним требуется много ручной работы — изменить настройки, перестартовать инстансы, не забыть отключить кроны и всякие Celery, запустить миграции и повторить всё в обратном порядке. #django
* Про то, [как и зачем Prismatic мигрировал на Clojure](http://blog.getprismatic.com/blog/2013/1/14/bringing-functional-to-the-frontend-clojure-clojurescript-for-the-web) с Node.js. Если коротко, то они купились на возможность писать шаблоны в терминах основного языка, и иметь возможность его трансформировать перед рендерингом. Для шаблонов на сервере, они используют [Hiccup](https://github.com/weavejester/hiccup), а на клиенте — свою собственную разраотку [dommy](https://github.com/prismatic/dommy). #clojure

Фронтэнд
--------

* Несколько замен [console.log](http://patik.com/blog/complete-cross-browser-console-log/). #frontend
* Туториал по использованию [SVG для создания красивых заголовков](http://blogs.adobe.com/webplatform/2013/02/19/improving-css-text-decorations/) на вебе. #frontend #svg #css
* Интересного эффекта можно добиться [с помощью CSS транзишенов](http://pepsized.com/icon-fonts-in-use-with-a-fancy-hover-effect/), для иконок. Для нетерпеливых, [вот демка](http://pepsized.com/demo/?id=1202). #frontend #css

Разное
------

* Очень правильная статья (2006 года) [про разработку дизайна информационных систем](http://worrydream.com/MagicInk/)! Читал запоем, и до сих пор остаюсь в недоумении, почему у нас 2013 год на дворе, а интерфейсы большинства интернет проектов настолько убоги? #misc #design
* Свежее [описание стека технологий Twitter](http://engineering.twitter.com/2013/01/braindump.html). У них там кругом JVM. Инетесен способ, с помощью которого анализируются задержки в обработке запросов различными подсистемами, для этого используется собственная разработка — [Zipkin](https://github.com/twitter/zipkin/). #twitter #stack