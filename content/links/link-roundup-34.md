Title: Link Roundup #34
Slug: link-roundup-34
Date: 2014-01-21 14:09
Category: links
Tags: roundup
Lang: ru

Разработка
----------

* Студия Futurecolors выложила на гитхаб [скелет Django сайта](https://github.com/futurecolors/tinned-django/), который они используют начиная работу над новым проектом. #django #develop
* [Wheel](http://wheel.readthedocs.org/) – новый формат пакетов для Python, который позиционируется, как замена для egg. Попробовал на одном из своих проектов, результаты такие: сборка без wheels — 1:43, сборка с wheels — 0:28. Сами пакеты при этом собираются 2 минуты. Получается, что при редком изменении версий, сборки будут проходить в три раза быстрее. #python #develop
* Очень познавательная статья [про то, как на питоне решать многие проблемы](http://www.stephendiehl.com/posts/postmodern.html), не свойственные этому языку. #develop #python

Фронтэнд
--------

* В новом интерфейсе GitHub используется интересная либа для jQuery – [pjax](https://github.com/defunkt/jquery-pjax), которая позволяет очень просто вместо перехода по ссылке, перезагружать указанную часть страницы. #frontend #javascript
* Статья [про разницу между Backbone.js и Angular.js](http://victorsavkin.com/post/65519559752/contrasting-backbone-and-angular). Я, так понял, что backbone для меня слишком низкоуровневый, и начал ковырять angular. #javascript #frontend
* Говорят, есть такая крутая штука для форматирования css  и приведения его к единому виду — [csscomb.js](https://github.com/csscomb/csscomb.js). #css #frontend

Разное
------

* Несколько сервисов для интеграции других сервисов: http://cloudwork.com, http://ifttt.com и http://zapier.com/. Могут быть полезны, когда надо интегрировать несколько разных сервисов для совместной работы. Подобным образом у меня формируется RSS с новыми задачами, которые потом попадают в Emacs OrgMode. #misc
* Gigablast заопенсорсил свой [поисковый движок](https://github.com/gigablast/open-source-search-engine). Доселе я и не знал про такой поисковик. А теперь вот знаю. #misc
* [Librato](https://metrics.librato.com/) – еще один облачный сервис мониторинга и графиков. Вероятно, для тех, кто не осилил поднять Graphite. #misc
