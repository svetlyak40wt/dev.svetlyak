Title: Link Roundup #31
Slug: link-roundup-31
Date: 2013-04-10 19:04
Category: links
Tags: roundup
Lang: ru

Разработка
----------
* Доклад разработчика New Relic, на тему того, [какие бывают виды профайлинга в Python](http://lanyrd.com/2013/pycon/scdywg/). #develop #python
* [Python data tools](http://strata.oreilly.com/2013/03/python-data-tools-just-keep-getting-better.html) #develop
* Подробная статья про то, [как использовать Chef для деплоя в облака](http://blog.fungibleclouds.com/blog/2012/12/09/using-chef-to-deploy-cloud-applications/), учитывая разные среды (разработка, престейбл, продакшн), а так же типы серверов. #develop
* А вы знали, что можно делать так: `echo '{"2": {"timestamp": 1364978341, "jams": {"13": {"from": 5}}}}' | python -mjson.tool` для того, чтобы вывести JSON в удобочитаемом виде? Работает начиная с 2.6. #python #develop
* [django-authority](http://pythonhosted.org/django-authority/index.html) — интересная реализция raw-level permissions для Django. Правда в отличии от того-же [django-guardian](http://pythonhosted.org/django-guardian/) я не нашел способа получить список объектов, которые я могу изменять. А это важно. #django #develop
* Пример того, [как запустить Django на Python 3.3](https://github.com/aaugustin/django-c10k-demo) в асинхронном режиме, чтобы обслуживать тысяч одновременных соединений через websocket. #django #highload #develop #async
* Прикольный [dashboard с разными метриками про разработку Django](https://dashboard.djangoproject.com/). #develop #django
* Интересный фреймворк для функционального тестирования — [RobotFramework](http://robotframework.org/). Можно тестировать все что угодно, от вебсервисов до низкоуровневых библиотек. #development #tests

Фронтэнд
--------
* Подробный туториал [про авто-тестирование веб-интерфейсов в Яндекс.Почте](http://habrahabr.ru/company/yandex/blog/173769/). Используются Selenium, Node.js, Mocha и Chai. #frontend
* Наконец понял, [как работает ключевое слово auto](http://www.vanseodesign.com/css/auto-positioning/) в CSS, при позиционировании элементов. #frontend #css

Разное
------

* Существует в вебе такая инициатива, как Do Not Track. Если кратко, то это соглашение между пользователями и владельцами сайтов о том, что если пользователь говорит: "Не надо накапливать данные обо мне и использовать их в любых целях", то сайты не накапливают и не используют подобные данные. Кажется, что это в первую очередь для параноиков, которых пугает таргетированная реклама. На сайте Мозиллы есть [подробное описание того, как работает Do Not Track](http://www.mozilla.org/en-US/dnt/), а вот тут можно почитать разъяснения на тему того, [как это может быть реализовано на стороне провайдера контента](http://donottrack.us/cookbook/). #misc
* [Новая версия python.org](http://preview.python.org/) весьма сэкси. #misc
* Небольшой пост про то, [почему программисты должны спариваться](http://mdswanson.com/blog/2013/03/19/cross-pollination.html) и какая в том польза. #misc
* [Expand-region](https://github.com/magnars/expand-region.el) — полезное расшрение для Emacs, позволяет расширять выделение по блокам кода. А вот [и демка](http://emacsrocks.com/e09.html). #emacs #misc