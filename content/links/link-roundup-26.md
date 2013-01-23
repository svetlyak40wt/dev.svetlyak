Title: Link Roundup #26
Slug: link-roundup-26
Date: 2013-01-23 15:32
Category: links
Tags: roundup
Lang: ru

Разработка
----------

* В MongoDB 2.4 появится [полнотекстовый поиск](http://emptysquare.net/blog/mongodb-full-text-search/), но попробовать можно уже сейчас. #mongodb #develop
* В MongoDB появились так называемые [fail points](http://www.kchodorow.com/blog/2013/01/15/intro-to-fail-points/) — конфигурируемые точки отказа. Они могуть быть полезны, когда нужно смоделировать определенные ошибки базы данных, или ее медленную работу. Как я понял, пока что для этого требуется лезть в исходники Mongo, по крайне мере, в коде монги, на данный момент, есть только три таких программируемых точки отказа. #mongodb #develop
* [Скрипты для запуска на Heroku](https://github.com/mtravers/heroku-buildpack-cl) проектов, использующих Common Lisp. А вот [пример того, как это использовать](http://kuomarc.wordpress.com/2012/05/13/12-steps-to-build-and-deploy-common-lisp-in-the-cloud-and-comparing-rails/). #lisp #heroku #develop
* Charles Leifer пишет [про то, как он полностью переписал](http://charlesleifer.com/blog/shortcomings-in-the-django-orm-and-a-look-at-peewee-a-lightweight-alternative/) API своего ORM Peewee. И он предлагает сделать то же самое команде Django. На мой взгляд, у него получилось все консистентно, но очень уж громоздко выглядят конструкции — проще тогда на чистом SQL писать. #python #django #orm #peewee #develop
* Пара инструментов для Рубистов: [Gemnasium](https://gemnasium.com/) — сервис, который проверяет, не устарели ли зависимости вашего проекта, и [CodeClimate](https://codeclimate.com/) — считает по разным метрикам качество кода, и сигналит, если все стало слишком плохо. Хочу такое же, но для Python! #ruby #develop
* [Pypackage](https://github.com/jamescasbon/pypackage) — скрипт для заворачивания питоновских виртуальных окружений в deb или rpm пакеты. #python #debian #redhat #develop
* [Описание способа взлома](http://phenoelit.org/blog/archives/2012/12/21/let_me_github_that_for_you/index.html) опенсорсных проектов на Ruby On Rails. #ruby #security #develop
* [Матрица компетентности](http://www.indiangeek.net/wp-content/uploads/Programmer%20competency%20matrix.htm) разработчика. #develop
* [django-import-export](https://github.com/bmihelac/django-import-export) — модуль для django, позволяющий экспортировать и импортировать данные. Работает с разными форматими, табличными и не только. #django #develop
* Простая Python [библиотечка для простых краулеров](https://github.com/bbrodriges/pholcidae) на питоне. Зато совсем без зависимостей. #python #develop
* [Mongo WAT](http://www.kchodorow.com/blog/2012/12/27/mongodb-puzzlers-1/) — пример неожиданного поведения монги на, казалось бы, простом запросе. #mongodb #develop
* [Hyperpolyglot](http://hyperpolyglot.org/scripting) — интересный сайт со сравнительными табличками для разных языков. Наглядно показывает, разницу между конструкциями в разных языках программирования. #python #ruby #perl #php #develop
* [django-deployer](https://github.com/natea/django-deployer) — скрипт для раскатывания django сервисов на такие платформы, как Heroku, Dotcloud, Stackato, OpenShift, и Gondor. #django #develop
* [GitHubSurvivor](https://github.com/99designs/githubsurvivor) — дашборд для вывода количества багов и так же топа коммиттеров, закрывающих баги. #github #develop #flask
* [Pick Your Battles](http://zef.me/4235/pick-your-battles) — автор статьи пытается отсоветовать вам использовать клёвые технологии для нового-кленового стартапа. В качестве аргументов приводит ряд проблем, с которыми они столкнулись в Cloud9, выбрав Node.js и Redis, хотя могли бы обойтись старым добрым PHP+MySql. #nodejs #startup #redis #cloud9 #develop

Фронтэнд
--------

* Интересное описание процесса создания [нового дизайна для auto.yandex.ru](http://www.artlebedev.ru/everything/yandex/auto/process/). #frontend
* [Normalize.css](https://github.com/necolas/normalize.css) — альтернатива всяческим CSS ресетам. Этот стиль пытается сгладить неровности между представлением HTML в разных браузерах. #css #frontend
* [Пара](http://www.alistapart.com/articles/howtosizetextincss/) старых текстов о том, [почему надо использовать em](http://clagnut.com/blog/348/) для задания размеров в CSS верстке. #css #frontend
* [Wirify](http://www.wirify.com/) — букмарклет, превращающий любую HTML страницу в прототип, годный для дальнейшего редактирования в Visio, OmniGraffle или Balsamiq. #frontend
* Перебрал несколько инструментов для прототипирования страниц. Пробовал и [Pencil](http://pencil.evolus.vn/), и [Balsamiq Mocups](http://www.balsamiq.com/), но остановился пока на бесплатной версии [Cacoo](https://cacoo.com/). #design #frontend
* [8 сервисов для генерации](http://net.tutsplus.com/articles/web-roundups/the-top-8-placeholders-for-web-designers/) картинок-заглушек. #frontend

Разное
------

* GitHub подвел [итоги конкурса на лучшую игру](https://github.com/blog/1337-github-game-off-winners). Посмотрел несколько игрушек. Весьма клевые! #misc #github
* [Paysio.com](https://paysio.com/) — русская система приема платежей. Поддерживает много платежных систем. С виду, очень приятная документация, REST API. #misc #startups
* [Статья про то, почему от Скрама кони дохнут](http://habrahabr.ru/post/163413/). К счастью, содержит конструктивные советы, как этого избежать. Рецепт достаточно простой — Continuous Integration со встроенными средствами мониторинга качества кода. #misc
* В GitHub сделали страницу профиля еще более клёвой! Теперь на ней показан календарик на котором отображается <a href="https://github.com/blog/1360-introducing-contributions">частота коммитов в тот или иной день</a>. Сразу видно, кто активно использует сервис, а кто — лишь время от времени. #misc
* [Repowatcher](http://www.repowatcher.com/) — попытка сделать удобный интерфейс для классификации и поиска репозиториев, которые вы когда-то зазвездили или завотчили на Github и Bitbucket. #github #startup
