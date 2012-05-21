Title: Link Roundup #2
Slug: link-roundup-2
Date: 2012-04-23 13:15
Category: links
Tags: python, roundup
Lang: ru

Python
------
* Статья о том, [как пушить стэктрейсы через PubSub Redis'a в IRC канал](http://charlesleifer.com/blog/using-redis-pub-sub-and-irc-for-error-logging-with-python/).
* Мой [клон Homebrew, но для Linux и на Python](https://github.com/svetlyak40wt/osbench/), пока очень очень alpha, но уже умеет устанавливать пакетики, и скоро научится удалять :))).
* Один из коллег опубликовал на GitHub [python скриптик, чтобы считать IO по файлам в Linux](https://gist.github.com/2397652). Сначала статистика собирается через TAP, а потом этим скриптиком аггрегируется: `stap filestat.stp bsc-srch-base-8 | python -u aggregate_filestat.py`.
* А вот [Chaco](http://github.enthought.com/chaco/) — python библиотечка для рендеринга интерактивных графиков.
* Кеннет Рейнц написал [статью](http://www.kennethreitz.com/repository-structure-and-python.html) про "правильную" структуру репозитория для Python проекта. Всё очевидно и разжевано. Можно рекомендовать новичкам.
* Доклад [Python Metaprogramming for Mad Scientists and Evil Geniuses](http://www.youtube.com/watch?v=Adr_QuDZxuM), с PyCon2012. Много интересного про манкипатчинг.
* Так же, я потестил PyPy на маленьком Bottle+Gunicorn проектике, и получил прирост производительности всего на 30%. Не впечатлен. Настмотревшись [их графиков](http://speed.pypy.org/), ожидал большего.
* Кстати, вы знали, что в gunicorn можно передавать не только путь до application, но и фунцию, которая этот app генерит? Как-то так: `gunicorn 'mysite:app_generator()'`.

Разное
------
* Огромная подборка статей [про Responsive Design](http://www.smashingmagazine.com/2011/07/22/responsive-web-design-techniques-tools-and-design-strategies/). Отложил в закладки, когда-нибудь пригодится, хоть я и не верстальщик и не дизайнер.
* Интересная статья про то, [как правильно писать асинхронный код](http://jeditoolkit.com/2012/04/26/code-logic-not-mechanics.html) на Javascript. Предлагаемая концепция немного напоминает Deferred в Twisted Python, и обертку inlineCallbacks.
* Старая статья Guy Kawasaki о том, что [презентация должна быть](http://blog.guykawasaki.com/2005/12/the_102030_rule.html) на 10 страницах, за 20 минут и крупным 30pt шрифтом.
* Описание формата [oEmbed](http://oembed.com/), позволяющего посредством GET запросов получать информацию о ресурсах сайта по урлу. Например для встраивания их в другие сайты. Оказывается, этот oEmbed много кто поддерживает.
* Твиттер принес ссылку на еще один GUI клиент к MongoDB — [MonjaDB](http://www.jumperz.net/index.php?i=2&a=0&b=9). Пока не смотрел. Судя по скриншотам, довольно развесистый, и на Java и под Eclipse.

Полезные сервисы
----------------
* [ChartBeat](http://chartbeat.com/) — онлайн аналитика посещений. По словам разработчиков, их сервис отличается от Google Analytics или Яндекс Метрики тем, что позволяет отслеживать то, чем занимаются пользователи вышего сервиса прямо сейчас, в "реальном" времени. Хотел попробовать, но они хотят даже для триала, получить данные моей кредитки. Отказался.
* [Hide-My-Ass](http://hidemyass.com) — прокси, который не нужно настраивать.
* 19 апреля, Python хостинг <http://ep.io> объявил о скором закрытии. Не выдержали конкуренции. Вовремя я перевел один свой маленький сайтик с него, на хостинг яндекса.
