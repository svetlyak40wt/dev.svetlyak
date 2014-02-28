* Еще один инструмент для конфигурирования серверов — [Ansible](https://github.com/ansible/ansible/). Тот же Salt, вид сбоку. Но поскольку я уже все скрипты на Salt переписал, то Ansible даже и пробовать не стану. #deploy #misc
* Отличная статья Андрея Светлова [про то, как работает сборщик мусора в Python](http://asvetlov.blogspot.ru/2013/05/gc.html). #develop #python
* Заметка Джейсона Фрайда, [про то, как важно уметь быстро клепать на коленке](http://www.inc.com/magazine/201305/jason-fried/the-importance-of-quick-and-dirty.html). Джейсон – один из сооснователей [37 Signals](http://37signals.com/), расстраивается, что они растеряли этот замечательный навык, позволяющий побыстрому собрать черновой вариант сервиса за пару-тройку дней. Он считает, что это крайне важное умение для любой IT компании, и тут я с ним полностью согласен. #misc
* Интересное [расширение возможностей](https://github.com/TylerBrock/mongo-hacker) консольного MongoDB клиента. Там и подстветка json, и разный синтаксический сахар для построения запросов и апдейтов (почти как в Django ORM). Ставится элементарно. #mongodb #develop
* Винсент Дриессен рассказывает про [будущие улучшения в pip-tools](http://nvie.com/posts/better-package-management/). Думаю, они идут в правильном направлении, судя по описанию, pip-sync — просто песня. Попробовать можно уже сейчас. #python #develop
* [Пара скриптов](http://stackoverflow.com/questions/3462955/putting-git-hooks-into-repository) для установки и запуска git хуков. #git #misc
* Потрясающий [сайт Брета Виктора](http://worrydream.com/). Про дизайн и всякое такое. Смотреть обязательно! #design
* Вот не любят 1С, из-за русских операторов. Но что-то в этом есть. Встречайте: Йоба – язык для чотких пацанов: http://sorokdva.net/ #misc #fun
* Global Game Jam — эдакий хакатон для разработчиков игр. #misc
* [Ready For Zero](https://www.readyforzero.com/) — интересный стартап для тех кто берет кредиты. Жаль, что пока работает только в US. #misc
* Сводка из синтетических [тестов кучи веб-фреймворков](http://www.techempower.com/benchmarks/). По ним хорошо видно, как быстро начинают сравниваться в производительности динамические и компилируемые языки, когда дело доходит до более реальных задач. #develop
* На канале lisp, меня навели на две библиотечки, которые решают задачу, сходную с Plumber от Prismatic. Первая библиотечка — [Cells](http://common-lisp.net/project/cells/), вторая — [computed-class](http://common-lisp.net/project/computed-class/index-old.shtml). #lisp
* Всё больше проектов начинают использовать Go.

Так, ребята из Discus недавно заявили, что переписали часть своей backend логики с Python на Go, и добились увеличения производительности на несколько порядков — собщения теперь обрабатываются не несколько минут, а 10 миллисекунд.

Кроме этого, разработчики MongoDB объявили, что они переписали свою тулзу для бэкапа с Java на Go, и очень счастливы.

Пруфлинки:

* http://blog.disqus.com/post/51155103801/trying-out-this-go-thing

* http://blog.mongodb.org/post/51643994762/go-agent-go

#develop #go
* Про [использование format](http://lisper.ru/pcl/a-few-format-recipes) в lisp. Разные примеры и описание возможностей. На русском. #lisp
* Допилил скрипт, устанавливающий Graphite: https://github.com/svetlyak40wt/graphite-node на Ubuntu Precise заводится без всяких усилий! #develop #monitoring
* Reading: [Quickstart — dataset 0.3 documentation](http://dataset.readthedocs.org/en/latest/quickstart.html) -  Отличная обертка над SQLAlchemy, делающая работу с sql базами простой и даже в каком-то смысле приятной. Замечательно подходит для простых случаев использования и не требует жестко задавать схему, делая необходимые ALTER налету! #sql #python #develop

* Reading: [Python on Wheels | Armin Ronacher's Thoughts and Writings](http://lucumr.pocoo.org/2014/1/27/python-on-wheels/) -  Свежий пост Армина Роначера про то, как использовать новый формат python пакетов wheel для деплоймента. #python #develop

* Reading: [Ahrefs Site Explorer & Backlink Checker](https://ahrefs.com/) -  Зарегался на сайте ahrefs.com — аналитика для сеошников. Нашел его в access логах make-me-pizza.ru #misc #seo

* Reading: [ZSH-LOVERS(1)](http://grml.org/zsh/zsh-lovers.html) -  Туториал по zsh, фактически состоящий из одних примеров. #zsh #dotfiles

* Reading: [ThriftDB - Flexible datastore with search built-in](http://www.thriftdb.com/) -  ThriftDB — документоориентированная база данных со встроенным полнотекстовым поиском. Пока что это облачное решение, локально установить нельзя, но разработчики уверяют, что они работают над этим. #nosql #thriftdb #develop

* Reading: [Hacker News Data Analysis: 2014 Edition - Ecommerce Blog](http://blog.rjmetrics.com/2014/01/23/hacker-news-data-analysis-2014-edition/) -  Очень подробный анализ пользовательской активности на Hacker News. #misc #startups

* Reading: [The Best Time to Post on Hacker News | Rant / Code / Rant](http://nathanael.hevenet.com/the-best-time-to-post-on-hacker-news-a-comprehensive-answer/) -  Только хотел написать скрипт, который бы рассчитал наиболее правильное время для постинга на Hacker News, как наткнулся на эту статью, в которой чувак уже сделал подобный анализ. Единственное, чего там нет, так это учета дня недели. #misc

* Reading: [Hacker News API - Unofficial Hacker News JSON API](http://hndroidapi.appspot.com/) -  Еще одно API для доступа к данным с Hacker News. #misc

* Reading: [Arc Forum | I just use system to call sendmail (postfix). Here's how it looks in readwarp. ...](http://arclanguage.org/item?id=14622) -  Пример того, как отправлять почту через sendmail из Arc. #arc #lisp

* Установил в emacs geiser — модуль типа Slime, но для Scheme/Racket. #develop

* Reading: [A Startup's Guide to Hiring](http://blog.sourcing.io/startups-hiring-guide) -  Правильная статья про то, как нанимать айтишников. Особенно мне понравилось Воскресное Правило, надо бы тоже взять на вооружение. #misc

* Гитхабовцы здорово улучшили возможности по настройке и отладке вебхуков! https://github.com/blog/1778-webhooks-level-up #misc #github

* (https://circleci.com/) — платный continuous integration сервер в облаке. Для закрытых проектов, которым не годится Travis, самое оно, наверное. #misc #startups

* Длинный пост Яна Байкинга (Ian Bicking) о том, как он перестал писать на Python и ушел в Mozilla работать над Together.js: http://www.ianbicking.org/blog/2014/02/saying-goodbye-to-python.html #python #misc

* Вышел мажорный релиз ElasticSearch — [1.0.0](http://www.elasticsearch.org/blog/1-0-0-released/). Есть пара полезных фич, например API для бэкапа и восстановления. #develop #search

* Hemingwayapp.com — сервис (и приложение), [для полуавтоматической коррекции текстов](http://www.hemingwayapp.com/). Помогает упростить обороты речи и улучшить читаемость. Эдакий lint для человеческих текстов. С русским работает лишь чуть — может подсказывать когда предложения становятся слишком длинны. #misc #startups

* Узнал тут про существование такой опасной вещи, как bitsquating. Это когда регистрируют домен, [похожий на популярный, но отличающийся](http://dinaburg.org/bitsquatting.html) одним битом. Полагаются тут не на опечатки пользователей, а на ошибки железа. Оказывается такое бывает вполне себе часто. #security #misc

* Армин Роначер (Armin Ronacher) написал о том, [как ему жаль, что Postgres не поддерживает upsert](http://lucumr.pocoo.org/2014/2/16/a-case-for-upserts/) и выразил недоумение по поводу того, почему это мало кого волнует. #postgres #develop

* (https://github.com/SnabbCo/snabbswitch/wiki) — тулза которая позволяет с бешенной скоростью обрабатывать сетевые пакеты. Кастомизируется на lua. #misc #networking #lua

* На кикстартере собирают деньги [на расширенную поддержку PostgreSQL в Django](https://www.kickstarter.com/projects/mjtamlyn/improved-postgresql-support-in-django). Так сложилось, что сам я постгреса касался лишь единожды, и тогда увидев его проблемы с репликацией, решил держаться от этого чуда подальше. Но теперь там вроде всё хорошо с этим, может стоит попробовать снова? #develop #postgres

* (http://www.groovehq.com/blog/the-software-stack), позволяющая потестить некоторые SaaS сервисы в течении 3 месяцев бесплатно. #misc

* Блог Конана Далтона про язык Arc. В основном, он там пишет [про то, как синтезировать музыку на Lisp](http://www.fnargs.com/). #lisp #arc #develop

* Три года назад один чувак написал [тулзу, которая снифает MySQL трафик](http://yoshinorimatsunobu.blogspot.ru/2011/04/tracking-long-running-transactions-in.html) и показывает долгие транзакции. Пока не пробовал, но возможно пригодится. Утилитку можно [скачать с GitHub](https://github.com/yoshinorim/MySlowTranCapture). #develop #mysql

* Аддон к vagrant, который автоматически обновляет Guest Additions: https://github.com/dotless-de/vagrant-vbguest #misc

* (https://www.flowdock.com/) сервис для командного взаимодействия — чатик и обмен документами. #startups #misc

* (https://github.com/trustedsec/artillery) — средство обнаружения проникновений (HIDS), написанное на Python. Пока фукционал весьма прост. #misc #python

