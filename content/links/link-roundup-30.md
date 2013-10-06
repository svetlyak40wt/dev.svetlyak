Title: Link Roundup #30
Slug: link-roundup-30
Date: 2013-03-21 16:24
Category: links
Tags: roundup
Lang: ru

Разработка
----------

* Способ, [как зафиксировать QuickLisp на конкретную дату](http://article.gmane.org/gmane.lisp.lispworks.general/12135). Но это конечно совсем не то, что дают нам virtualenv и pip в Python :( #lisp #develop
* Про то, как можно [обрабатывать do-not-track](http://blog.mathieu-leplatre.info/django-do-not-forget-do-not-track.html) HTTP заголовок в Django. #standarts #django #develop
* [django-braces](http://django-braces.readthedocs.org/en/latest/index.html) — полтора десятка миксинов для использования с объектными вьюхами Django. #develop #django
* Одна из этих двух библиотек вам точно пригодится, если понадобится иметь дело с табличными данными в Python: [TableFu](http://eyeseast.github.com/python-tablefu/) и [tablib](http://docs.python-tablib.org/en/latest/). #python #develop
* Ben Darnell зарелизил [новый профайлер для Python](http://emptysquare.net/blog/plop-python-profiler-with-call-graphs/) — Plop. Основные особенности — он может профилировать не каждый вызов а лишь определеную долю времени, а так же включает в себя фронтенд на Tornado и d3.js, позволяющий визуализировать накопленные данные. #python #performance #develop
* [Django Migratron](http://chase-seibert.github.com/blog/2013/03/01/introducing-django-migratron.html) — еще один способ накатывать миграции схемы и данных. У данного решения куча недостатков и несколько странных, на мой взгляд, фич. Например, нет зависимостей между миграциями, нет автогенерации миграций, как у South, но зато их можно зачем-то группировать и накатывать не все, а только часть. В общем, странное решение.

Разное
------

* Kristina Chodorow, чьи посты про MongoDB я читал с огромным удовольствием, [объявила о своем переходе в Google](http://www.kchodorow.com/blog/2013/02/26/goodbye-10gen-hello-google/). Чем она там будет заниматься, пока не известно. #misc
* Круть — в интерфейсе GitHub теперь можно [перемещать и переименовывать файлы](https://github.com/blog/1436-moving-and-renaming-files-on-github)! #github #misc
* Недавно у GitHub появился конкурент [Kiln Harmony](http://www.fogcreek.com/kiln/). Главная особенность Kiln заключается в том, что он позволяет работать с репозиторием как через Mercurial, так и через Git протокол. При этом внутри у них конечно два репозитория, которые синкаются между собой. И разработчики даже написали статью [о том, какой это адов-ад — синхронизировать Hg с Git](http://blog.fogcreek.com/kiln-harmony-internals-the-basics/).