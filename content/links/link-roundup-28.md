Title: Link Roundup #28
Slug: link-roundup-28
Date: 2013-02-11 16:21
Category: links
Tags: roundup
Lang: ru

Разработка
----------

* Про то, как [сделать ваш HTTPS сервер более стойким](http://hynek.me/articles/hardening-your-web-servers-ssl-ciphers/). В конце статьи есть ссылки на другие источники, к которых так же обсуждаются как вопросы правильной настройки SSL на вебсервере, так и то, зачем это вообще может быть нужно. #backend #develop
* Нашел несколько инструментов для подсчета. CCCC работает только с C, C++. [Sloccount](http://www.dwheeler.com/sloccount/) считает только строки кода, но зато для кучи разных языков. Для питончика есть [PyMetrics](https://github.com/ipmb/PyMetrics). [Ohcount](https://github.com/blackducksw/ohcount) эта тулза используется для построения графиков роста кодобазы, на сервисе [Ohloh.net](http://www.ohloh.net/). #develop
* [django-mini](https://github.com/davidwtbuxton/django-mini) — хелпер для запуска отдельный django приложений без необходимости settings.py. Там этого явно не сказано, но мне кажется, что естественное применение этой тулзе — запуск unit-тестов. #django #develop
* [django-conch](https://github.com/zacharyvoase/django-conch) — тулза, дающая доступ к django shell по ssh. Сначала я думал, оно дает подключаться к непосредственно Django серверу, крутящемуся на продакшене, как это можно делать, к примеру, с Twisted приложениями. Однако, на практике оказалось что это просто shell — немногим лучше чем просто ssh mange.py shell, а в чем-то может даже и хуже. #django #develop
* Старая статья (2006 год) Стива Егги, ["Почему Lisp не Lisp"](http://steve-yegge.blogspot.ru/2006/04/lisp-is-not-acceptable-lisp.html), где он многословно описывает все проблемы, что есть у Common Lisp, и приходит к выводу, что должен найтись супергерой, который выкинет всё к чертям, и придумает целостный, язык вроде Lisp. Это было еще до рождения [Clojure](http://en.wikipedia.org/wiki/Clojure) и, как я понимаю, создатель кложуры как раз пытается решить проблемы, описанные Стивом. #develop
* Некий Ben Plesser написал [автоматический релоадер кода для джанговской утилиты shell_plus](http://benplesser.com/2013/01/10/beefing-up-the-python-shell-to-build-apps-faster-and-dryer/). При чем, релоадер умный, не просто перезапускает процесс, а перезагружает отдельные модули и даже подменяет классы моделей для уже созданных объектов. #django #develop
* [Functional Programming Is Hard, That's Why It's Good](http://dave.fayr.am/posts/2011-08-19-lets-go-shopping.html) — эссэ на тему того, почему полезно изучать функциональные языки программирования. #develop

Фронтэнд
--------

* Отличные слайды про то, [что же такое Дизайн на самом деле](http://www.slideshare.net/ts-lim/web-design-101-9144718). В слайдах присутствуют ссылки на множество полезных ресурсов. #frontend #design #ux
* Занимательная статья про то, [как с помощью SVG и CSS создать анимированную инфографику](http://tympanus.net/codrops/2013/02/06/interactive-infographic-with-svg-and-css-animations/) для сайта. Автор очень подробно расписывает процесс создания анимации с помощью CSS, так что это пригодится для оживления любых элементов страницы, а не только SVG. #frontend #svg #tutorial

Разное
------

* Забавный прикол, который можно [провернуть с любителями халявного Wi-Fi](http://www.ex-parrot.com/pete/upside-down-ternet.html). На самом деле, так можно не только позабавиться, но и устроить им более серьезные неприятности. #misc
* Занятная [утилита для рисования гистограмм в консоли](https://github.com/visionmedia/histo). У меня, однако, не заработала ни в OSX, ни на Ubuntu Precise. Компилируется, запускается, но графики не рисует. #misc
