Title: Link Roundup #7
Slug: link-roundup-7
Date: 2012-06-25 16:36
Category: links
Tags: roundup
Lang: ru

Разработка
----------

* Гитхаб [закрыл v1 и v2](https://github.com/blog/1160-github-api-v2-end-of-life) версии своего API и слава богу.
* В девелоперской версии MongoDB [появились TTL индексы](http://www.kchodorow.com/blog/2012/06/18/good-night-westley-time-to-live-collections/), позволяющие задавать время жизни документов в коллекции. Годно для кеша, сессий и может еще для чего.
* [Diesel](http://diesel.io/tutorial) — еще один асинхронный сетевой фреймворк для Python, основанный на библиотеке greenlets.
* Хозяйке на заметку. Поднять девелоперский SMTP сервер на 8085 проще всего так: `python -m smtpd -n -c DebuggingServer`. Но есть и вебсервисы для этого, например http://mailtrap.io
* Пара pull-реквестов к pip, которые я хотел бы видеть в upstream — команда [show](https://github.com/pypa/pip/pull/517) и команда [outdated](https://github.com/pypa/pip/pull/235).
* [Реализация шаблонизатора](http://pypi.python.org/pypi/pystache/) Mustache, на Python.
* Есть и [JS реализация](https://github.com/janl/mustache.js) Mustache.
* А вот обертка, которая упрощает использование таких шаблонов на клиентской стороне — назвается [ICanHaz.js](http://icanhazjs.com/).
* [FormEncode](http://www.formencode.org/en/latest/Validator.html) — валидатор данных формы для Python.
* Оказывается, в MySQL можно [реплизировать только избранные таблицы](http://dev.mysql.com/doc/refman/5.0/en/replication-options-slave.html#option_mysqld_replicate-do-table). Иногда может оказаться полезно.

Разное
------
* [Fractal](https://www.getfractal.com/) — платный сервис по созданию кросс-клиентских HTML писем.
* [Sendgrid](http://sendgrid.com/) — платный сервис для массовой рассылки писем. Как водится, с API, аналитикой, подтверждением доставки и друими плюшками.
* [IFixIt](http://www.ifixit.com/) — сайт с мануалами по починке разных дейвайсов. К программированию отношения не имеет, но может быть полезно с в случае, если вы вдруг решите разобрать свой MacBook.
