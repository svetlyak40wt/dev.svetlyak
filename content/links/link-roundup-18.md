Title: Link Roundup #18
Slug: link-roundup-18
Date: 2012-10-15 15:15
Category: links
Tags: roundup
Lang: ru

Разработка
----------

* Отличный доклад Неда Батчелдера, — [Pragmatic Unicode](http://nedbatchelder.com/text/unipain.html), где он подробно разжевывает, что это такое, и как быть со всеми этими encode/decode. #python #video #slides
* [Django-api-playground](https://github.com/Hipo/Django-API-Playground) — специальное Django приложение, позволяющее прямо из браузера потыкать в рестовое API. Должно быть весьма удобно для документирования API. Жаль только, что структуру ручек и параметры нужно описывать вручную. #django #api
* Bitly заопенсорсил свой новый-кленовый [message queue](http://news.ycombinator.com/item?id=4631994) — NSQ. Весь из себя быстрый, распределенный и отказоустойчивый. Написан на Go, есть биндинги к Python. Репа хостится [на GitHub](https://github.com/bitly/nsq). #go #python #highload
* [Redis-faina](https://github.com/Instagram/redis-faina) — инструмент, разработанный в Instagram для аггрегации логов redis и анализа его производительности. #redis #highload #utils
* [Pykka](http://pykka.readthedocs.org/en/latest/) — библиотечка для программирования на Python, [на акторах](http://en.wikipedia.org/wiki/Actor_model) — когда абстрактные кусочки кода обмениваются сообщениями через некую шину. Считается, что программы, написанные таким образом, могут легко параллелиться. Судя по примечанию к документации, Pykka сделана по мотивам Java библиотеки Akka. #python #libs
* Кристина Чодоров пишет про то, [как работает журналирование в MongoDB](http://www.kchodorow.com/blog/2012/10/04/how-mongodbs-journaling-works/) и почему, при включенном журналировании, монга хавает в два раза больше памяти. #nosql #mongodb
* А ребята из TripAdvisor провели эксперимент, и посчитали, [во сколько им обойдется поднять кластер](http://highscalability.com/blog/2012/10/2/an-epic-tripadvisor-update-why-not-run-on-the-cloud-the-gran.html), способный держать продакшн нагрузку, на Amazon EC2. Оказалось, что за те же деньги, что они тратят сейчас, они смогут получить почти в полтора раза больше машин (хотя ядер на них будет в два раза меньше). Зато в замен они получили большую гибкость в масштабировании. #highload
* А тем временем, Рик Копелэнд, написал [скрипт для простенькой master-master репликации](http://blog.pythonisito.com/2012/07/multi-master-replication-in-mongodb.html) в MongoDB. Точнее, он его называет Mongo Multi Master, потому что скрипт можно гибко конфигурировать, указывая ему, какие коллекции на какую машинку реплицировать. #mongodb

Фронтэнд
--------
* [Descript](https://github.com/pasaran/descript) — Javascript аналог Яндексового сервера XScript. Позволяет собирать JSON документ из нескольких источников и, возможно (я код и доки не смотрел), как-то  его обрабатывать. Примечательно, что descript написан одним из разработчиков Яндекса, интересно, используется ли этот сервер где-нибудь внутри? #javascript  #backend
* [Opalang](http://opalang.org/) — еще один язык, компилирующийся в Javascript. На этот раз синтаксис не так чудовищен, как у Coffescript, opalang это скорее надмножество js, нежели чем совсем другой язык. Думаю, он стоит того, чтобы на взглянуть на него повнимательней. #javascript #frontend #backend

Разное
------

* [Coderwall.com](http://coderwall.com/svetlyak40wt) — еще одна платформа для разработчиков, позволяющая завести себе профиль, основываясь на данных с GitHub. У них там есть весьма забавные ачивки. Нечто подобное я как раз хотел сделать на http://gitorama.com. #services #startup
* [Humans.lol](http://humanslol.org/) — интересная инициатива. Чувак предлагает выкладывать на http://ваш-домен.рф/humans.lol какую-нибудь ржаку, а на прочих страницах проставлять специальный тег, чтобы тем самым обеспечить автоматическую ржако-дисковери. Надо будет на своем бложике что-нибудь подобное выложить. #misc
