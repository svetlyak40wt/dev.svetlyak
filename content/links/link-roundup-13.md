Title: Link Roundup #13
Slug: link-roundup-13
Date: 2012-09-10 09:40
Category: links
Tags: roundup
Lang: ru

Разработка
----------

* [Syntastic](https://github.com/scrooloose/syntastic) — Vim плагин для проверки синтаксиса в Python и многих других языках. Заменил на него старый pyflake-vim. #develop #vim
* [Django-cacheback](https://github.com/codeinthehole/django-cacheback) — библиотека, упрощающая асинхронное наполнение кэша. Для асинхронного выполнения использует Celery. #python #django
* Оказывается есть на Github [travisbot](https://github.com/travisbot), который ходит и добавляет к pull реквестам комменты, проходят эти изменения тесты, или нет. #develop #github
* [GitStats](http://gitstats.sourceforge.net/) — скрипт, для подствета интересной статистики про гитовый репозиторий. Рисует HTML с табличками и графиками — кто когда и сколько накоммитил, как развивался проект и т.д.. #git
* Статья [про реализацию различных структур данных](http://kmike.ru/python-data-structures/) с биндингами для Python. Отложил в копилку, вдруг когда-нибудь пригодится. #python #math
* [Django-rq](https://github.com/ui/django-rq) — модуль для Django, облегчающий работу c [Redis Queue](http://pypi.python.org/pypi/rq/) Винсента Дриессена. #django
* [Ijson](https://github.com/isagalaev/ijson) — обёртка над потоковым парсером JSON yajl. Ваня Сагалаев на днях ее значительно [улучшил](http://softwaremaniacs.org/blog/2012/09/07/pypy-ijson-3/). #python
* [The Redis Cookbook](http://rediscookbook.org/index.html) — рецепты использования Redis. Я тут решил заюзать его для временного хранения счетчиков со статистикой http://gitorama.com. #nosql #redis

Фронтэнд
--------

* Старая статья с "A List Apart" про то, как правильно верстать, [соблюдая вертикальный ритм](http://www.alistapart.com/articles/settingtypeontheweb/). #css
* [Rickshaw](http://code.shutterstock.com/rickshaw/) — бесплатная JS библиотечка для рисования симпатичных графиков. #js
* [3Djs](http://d3js.org/) еще одна JS библиотечка для красивой визуализации данных. А тут — [кучка демок](https://github.com/mbostock/d3/wiki/Gallery), сделанных на ней. Особенно [вот эта](http://mbostock.github.com/d3/talk/20111018/collision.html) мне нравится. #js
* [What The Key Code](http://whatthekeycode.com/) — веб-апп, показывающий код любой нажатой клавиши. Наверное полезно для описания хоткеев в JS. #js #webapp

Разное
------

* Разгребая вимовый конфиг, выделил небольшую, но весьма полезную его часть в отдельный плагин — vim-local-settings: http://bit.ly/PY3gaV #vim
* http://resume.github.com/ — использует API GitHub, чтобы показывать актуальное резюме. Вот, [к примеру, моё](http://resume.github.com/?svetlyak40wt). #services #github
* [Bucky](https://github.com/cloudant/bucky) — прокси между collectd или statsd и graphite. #admin
* [Collectd-carbon](https://github.com/indygreg/collectd-carbon) — плагинчик для collectd, который умеет писать данные в Graphite. Сам плагин написан на Python. Есть аналоги [на C](https://github.com/jssjr/collectd-write_graphite) и [Perl](https://github.com/joemiller/collectd-graphite) и [Node.js](https://github.com/loggly/collectd-to-graphite), но Python как-то родней. #python #monitoring #admin


