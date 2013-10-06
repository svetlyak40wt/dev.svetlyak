Title: Link Roundup #21
Slug: link-roundup-21
Date: 2012-11-08 16:45
Category: links
Tags: roundup
Lang: ru

Разработка
----------
* [django-polymorphic-tree](https://github.com/edoburu/django-polymorphic-tree) — эта библиотека позволяет хранить в базе деревья, элементами которых могут быть объекты с разными моделями. Не смотрел внутрь, но подозреваю что оно тормозить будет адски. #django
* [django-fixture-magic](https://github.com/davedash/django-fixture-magic) — команды для сохранения фикстур в Django и работы с ними. #django
* [mmstats](https://github.com/schmichael/mmstats) — библиотека для сбора статистики. Фактически, она держит счетчики в memory-mapped файле, который можно читать другой программой и отправлять в системы мониторинга. У меня тоже есть подобная поделка, но она держит данные в памяти, а принимает их по UDP. #python #monitoring
* Ну и пара докладов с PyCon2012 один, под заголовком "[Перестаньте уже наконец использовать классы!](http://www.youtube.com/watch?v=o9pEzgHorH0)" и второй на тему "[Искусство наследования](http://www.youtube.com/watch?v=miGolgp9xq8)". Оба будут весьма полезны всем, кто хочет писать как можно более питонячий код. #python

Фронтэнд
--------
* [Grands](http://grawl.github.com/Grands/) —  шрифт с иконками значков разных популярных веб-сервисов. #design
* [PonyDebugger](https://github.com/square/PonyDebugger) — попытка сделать удаленный отладчик для мобильных платформ. Пока есть связка только с iOS, но как я понял, архитектура расширяема. #mobile #clientside

Разное
------
* [fabric-completion](https://github.com/underself/fabric-completion) — скрипт для реализации автокомплита для Fabric. Будет полезен всем, кто использует этот инструмент и bash. #develop
* Занятная [рекламная статья](http://highscalability.com/blog/2012/11/1/cost-analysis-tripadvisor-and-pinterest-costs-on-the-aws-clo.html) про сервис оценки стоимости развертывания сервиса в Облаке. Для примера, эти ребята рассчитывают возможную стоимость хостинга на Амазоне для TripAdvisor и прогнозируют рост стоимости хранения данных в S3, для Pinterest. Интересно, Pinterest окупается, или они надеются его быстренько продать, пока не пришлось платить баснословные баксы Амазону? #cloud #amazon #s3 #ec2
