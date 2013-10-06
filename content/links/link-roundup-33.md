Title: Link Roundup #33
Slug: link-roundup-33
Date: 2013-06-10 13:46
Category: links
Tags: roundup
Lang: ru

Разработка
----------
* Оказывается, существует специальный [образ для VirtualBox, чтобы тестировать Django](https://github.com/jphalip/djangocore-box) на разных версиях Python и СУБД! #develop #django
* Вот так можно посмотреть версии и зависимости всех модулей в virtualenv: `pip list --local | awk '{print $1}' | xargs pip show | grep -v -e '^Location' -e '^Requires: $'`. #python #develop
* Хорошая статья, сравнивающая [Puppet и SaltStack](http://www.opencredo.com/blog/a-dive-into-salt-stack). Краткий вывод — Salt годная вещь. #misc #deploy
* Наткнулся тут на интересный сервис — [xip.io](http://xip.io/). Этот такой DNS, который берет IP из имени хоста, и ресолвится в него же. Например dev.192.168.1.1.xip.io отресолвится в 192.168.1.1. Это может быть полезно, когда у вас во внутренней сети сервер, который обрабатывает несколько виртаульных хостов. Так вот, чтобы к ним доступаться с разных устройств и не прописывать всё в DNS или /etc/hosts, можно ходить туда через xip.io. По-моему, клево! #develop
* Восторженный отзыв одного из разработчиков 37 Signals о программе для вывода статистики на iPad. Тоже что-ли попробовать этот [Status Board](http://37signals.com/svn/posts/3514-current-status)? Или может сначала побаловаться бесплатным [Status Dashboard](https://github.com/obazoud/statusdashboard), который работает в браузере, или же [Hubble](https://github.com/jaymedavis/hubble), который исключительно для консоли? #develop #dashboard
* Заметка Jesse Jiryu Davis, [про то, как он отлавливал баг в PyMongo](http://emptysquare.net/blog/another-thing-about-pythons-threadlocals/) и оказалось что баг в версиях Python <= 2.7.0. Речь о thread locals и weak ref. #python #develop
* [MongoQP](http://blog.mongodb.org/post/37261742378/mongoqp-mongodb-slow-query-profiler) и [Professor](https://github.com/dcrosta/professor) — два инструмента для просмотра статистики профайлера в MongoDB. Professor я попроовал, потому что его проще всего установить, ибо он на Python. Работает клево. Запросы аггрегирует, статистику считает, индексы на коллекциях показывает. #mongodb #python #highload

Фронтэнд
--------
*  Статья [про плоский дизайн](http://talala.ru/blog/2013/05/03/1/). Автор выражает свое мнение, что большинство дизайнеров не понимают сути дизайна в стиле "метро", и лишь копируют внешние проявления. При этом, он не раскрывает этой самой сути, или это я чего-то не понял и надо было читать между строк? #frontend
* Прекрасная статья Романа Комарова про то, что [все активные элементы на странице](http://kizu.ru/issues/cursor-pointer/) должны изменять курсор, и делать это консистентно и ожидаемо. #frontend
* [Mobify.js](http://www.mobify.com/mobifyjs/) — библиотечка, позволяющая модифцировать DOM дерево до загрузки всяких ресурсов. С ее помощью можно, например, изменять layout сайта для отображения на мобильных устройствах. #frontend
* Наконец на BEM технологии сделали библиотеку элементов по типу бутстрапа — [Topcoat](http://topcoat.io/). Попробовал, оказалось что блоков реализовано совсем мало, сделано всё странно, блоки пытаются эмулировать контролы, встречающиеся в десктопных программах (что не удивительно, учитывая происхождение библиотеки из недр Adobe). В общем, посмотрим что из этого разовьется. #frontend #bem #css

Разное
------
* Прекрасное описание того, [как работает process substitution в bash и zsh](http://tldp.org/LDP/abs/html/process-sub.html). Я даже и не знал про такое. Век живи, век учись. #misc  #shell
* Интересный движок для MySQL — TokuDB, [вышел в openssource](http://www.opennet.ru/opennews/art.shtml?num=36779). Судя по описанию, он обладает множеством прекрасных свойств, но многие из них мне кажутся противоречивыми. #mysql #misc
* Очень интересный [текст, презентации Кевина Вербаха, про Геймификацию](http://digitaloctober.ru/player/content/83). #misc #gamification
* Не знал, что у GitHub есть специальное [API, позволяющее помечать цветом pull-реквесты и ветки](https://github.com/blog/1227-commit-status-api)! А теперь вот они [ещё улучшили взаимодействие с разными системами CI](https://github.com/blog/1484-check-the-status-of-your-branches), добавив отображение статусов на странице веток. #github #misc
