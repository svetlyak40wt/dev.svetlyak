Title: Link Roundup #6
Slug: link-roundup-6
Date: 2012-06-18 17:00
Category: links
Tags: roundup
Lang: ru

Сегодня целый ворох линков, потому что никак не собирал пост почти три недели. Решил их побить на более мелкие разделы.

Разработка
----------

### Python

* [Faye](http://faye.jcoglan.com/node.html), [Socket.io](http://socket.io/) и [Juggernaut](https://github.com/maccman/juggernaut). Всё это — библиотеки для реализации асинхронного обмена данными между клиентом и севером. Почему же они используют Node.js на серверной стороне? Только для Socket.io есть сторонняя разработка на Python — [gevent-socketio](https://github.com/abourget/gevent-socketio). Juggernaut и Socket.io весьма похожи друг на друга, и могут использовать разные транспорты, начиная от WebSocket и заканчивая лонг-поллингом. А вот Faye использует какой-то странный протокол Bayeux. Я особо не вчитывался, в [RFC Bayeux](http://svn.cometd.com/trunk/bayeux/bayeux.html), но похоже это что-то типа WebSocket на стероидах.
* Слайды [про то, как сделать чатик](http://www.slideshare.net/rick446/realtime-web-gevent-and-socketio) на Python + GEvent + ZeroMQ + Socket.io.
* Статья про то, [как собрать веб-комбайн на Circus и Mongrel2](http://blog.ziade.org/2012/05/31/mongrel2-amp-circus-full-control-of-your-web-stack/). Человек пытался заменить gunicorn на Mongrel2, но пока по результатам тесов выходит на 20% медленнее.
* [Slumber](http://slumber.in/) — библиотечка, упрощающая работу с HTTP API из Python.
* [HTTPie](http://pypi.python.org/pypi/httpie/) — интересная замена curl, построенная на базе Python библиотеки requests.

### JavaScript

* [Статья про Backbone.js](http://lincolnloop.com/blog/2012/jun/5/backbonejs-django-developers/) для Django разработчиков, интересующихся Javascript server-side разработкой.
* [Dygraphs](http://dygraphs.com/) — Прикольная JS билиотечка для отображения графиков.

### Databases

* Про новый [Aggregation Framework](blog.pythonisito.com/2012/06/using-mongodbs-new-aggregation.html), который появился в MongoDB с версии 2.1.
* [Ming](http://blog.pythonisito.com/2012/06/schema-maintenance-with-ming-and.html) — object-mappert для MongoDB, написанный в Sourceforge. Довольно занятная штука, надо попробовать.
* [Туториал](http://merciless.sourceforge.net/odm.html) по более высокоуровнему интерфейсу Ming для маппинга python объектов на MongoDB документы.
* Про новую [гугловую базу F1](http://static.googleusercontent.com/external_content/untrusted_dlcp/research.google.com/en//pubs/archive/38125.pdf). По сути, это NOSQL хранилище c автоматическим шардингом, над которым накручена SQL прокся.
* [Jetpants](http://engineering.tumblr.com/post/24612921290/jetpants-a-toolkit-for-huge-mysql-topologies) — инструмент для управления большим количеством MySQL шардов, недавно отданый в opensource Tumbler.

### Общее

* Старая, но до сих пор актуальная статья [про ошибки, допускаемые при разработке](http://jacobian.org/writing/rest-worst-practices/) REST API.
* [Плагин к Sphinx](http://packages.python.org/sphinxcontrib-httpdomain/) для документирования HTTP API. Начал приводить в порядок документацию на части своих проектов.
* Посмотрел на [доку по Zipper](https://github.com/twitter/zipkin) от Twitter, про трассировку запросов в гетерогенной среде. Оказывается, похожая штука есть и у Гугла — [Dapper](http://research.google.com/pubs/pub36356.html) называется.
* [HubFlow](http://datasift.github.com/gitflow/GitFlowForGitHub.html) —  попытка приспособить GitFlow для работы через GitHub. Увы, не годится для opensource проектов в которые могут  контрибьютить люди со стороны.
* Исследование про то, [до скольки параллельных коннектов](https://github.com/ericmoritz/wsdemo/blob/master/results.md) держат реализации WebSocket на разных языках.

Дизайн
------

### Графика

* Полезный сайтик с которого можно брать картинки заглушки. Например так: http://lorempixel.com/300/200/people/2/ размеры картинки можно менять прямо в URL.
* Еще один [сервис с картинками-заглушками](http://placekitten.com/). Но там только котята.
* [Шрифтовые иконки](http://fortawesome.github.com/Font-Awesome/) для Bootstrap и не только.

### CSS

* На пальцах, [про разницу между absolute и relative position в CSS](http://designshack.net/articles/css/the-lowdown-on-absolute-vs-relative-positioning/). Выучил новый трюк.
* Опять же, на пальцах объясняют, [как центровать блоки](http://designshack.net/articles/css/how-to-center-anything-with-css/) с помощью CSS.
* И еще немного [про сокращенный синтаксис в CSS](http://designshack.net/articles/css/6-css-shorthand-tricks-every-developer-should-know).

Сервисы
-------

* [GitTip](gittip.com) — это что-то вроде Flattr, но только для GitHub, если вы понимаете, о чем я ;-)
* [Cacoo](https://cacoo.com) — сервис для прототипирования и рисования диаграмм. Есть бесплатный "план".
* [Статейка](http://mashable.com/2012/06/07/mockup-tools/) со списком других сервизов для прототипирования.
* [Crate.io](https://crate.io/) — более современная замена PyPi. Умее показывать графики со статистикой, посасывает информацию о репозитории и доках на ReadTheDocs.

Разное
------

* Про [управление распределенным офисом](http://ryancarson.com/post/24884883426/how-i-manage-40-people-remotely). Украдено из [линкблога](http://addmeto.cc) Бобука.
* [Geekli.st объявил](http://gklst.tumblr.com/post/25111024798/from-the-engineering-team-facebook-integration) об интеграции с Facebook посредством Open Graph.  Вот описание самого протокола [Open Graph](http://ogp.me/) придуманного в Facebook в 2010 году. Так же, в их доках есть краткое описание того, [как использовать Open Graph](https://developers.facebook.com/docs/opengraph/) для интеграции с фейсбуком. Там же есть и туториал про то, [как интегрировать](https://developers.facebook.com/docs/opengraph/tutorial/) свой сайт с фейсбучиком.

