Title: Link Roundup #10
Slug: link-roundup-10
Date: 2012-07-30 10:11
Category: links
Tags: roundup
Lang: ru

Сегодня ссылок немного, и все про разработку:

* [Введение в gevent](http://blog.pythonisito.com/2012/07/introduction-to-gevent.html) простенькая статья, объясняющая, зачем нужны гринлеты.
* И следующая статья [про gevent](http://blog.pythonisito.com/2012/07/gevent-threads-and-benchmarks.html), того же автора, с немного поправилеными тестами и разъяснениями.
* Заметка гитхабовцев про недавнюю проблему с ssh авторизацией. Оказывается, они [ходили в  MySQL напрямую из sshd](https://github.com/blog/1212-surviving-the-sshpocolypse) и создавали много коннектов к базе. Теперь схема такая: sshd --HTTP--> Rails --> MySQL.
* Офигенная статья про то, как чувак собрал [централизованный логгинг на open source компонентах](http://divisionbyzero.net/article/2012/06/17/central-logging-with-open-source-software.html). Rsyslog для сбора + Logstash с ElasticSearch бэкендом — для анализа + Graphite для рисования графиков.
* Весьма полезная заметка про то, [почему ваши range запросы могут тормозить](http://blog.mongolab.com/2012/06/cardinal-ins/) даже несмотря на индексы. Статья о MongoDB, но кажется что и в других БД может быть подобная проблема.
* А вот эта статья для особых извращенцев, желающих [отлаживать Python код в gdb](https://stripe.com/blog/exploring-python-using-gdb). Так и не понял, зачем это кому-то может понадобиться. Разве только вы не C расширение пишете.
* [Про плюсы и минусы](http://faassen.n--tree.net/blog/view/weblog/2011/11/18/0) client-side шаблонов, а так же про то, что в основном они — push-only, то есть, не позволяют делать вызовы методов, так как в контексте лежат простейшие структуры данных.
