Title: Link Roundup #15
Slug: link-roundup-15
Date: 2012-09-24 09:30
Category: links
Tags: roundup
Lang: ru

Разработка
----------

* Guido van Rossum капитанит, давая очевидные советы про то, [как сделать ваши Python программы быстрыми](https://plus.google.com/u/0/115212051037621986145/posts/HajXHPGN752). Впрочем, извлек из этого тредика одну полезную вещь, а именно — ссылку на gui для просмотра дампов из cProfile. Называется [RunSnakeRun](http://www.vrplumber.com/programming/runsnakerun/). #python #profiling
* RunSnakeRun мне так и не удалось запустить на OSX. Зато узнал про утилитку lipo, с помощью которой можно обстрипать бинарник и убрать из него поддержку лишних архитектур. Зато на OSX отлично работает qcachegrind (устанавливаемый через homebrew). Но только для него надо конвертировать дампы cProfile с помощью [pyprof2calltree](http://pypi.python.org/pypi/pyprof2calltree/). #python #profiling
* [Sh](http://amoffat.github.com/sh/index.html) —  интересный интерфейс к питоновому subprocess. Более навороченный, чем [envoy](http://pypi.python.org/pypi/envoy/). #python #admin
* [Anemometer](https://github.com/box/Anemometer) — вебинтерфейс для просмотра MySQL slow query лога. #php #mysql
* Длинный предлинный туториал [Redis с нуля](http://blog.mjrusso.com/2010/10/17/redis-from-the-ground-up.html). Я пока не осилил. Отложил в копилку. #redis #tutorial #nosql
* Любят емаксеры комбайны, я смотрю. Для разработки на Django вон что написали — [Pony Mode](https://github.com/davidmiller/pony-mode). Вы только посмотрите на список фич! #django #emacs #ide

Фронтэнд
--------

* Яндекс зарелизил свой [JS шаблонизатор Yate](http://habrahabr.ru/company/yandex/blog/151700/). Я хоть и не люблю XSL, на который идеологически похож Yate, но всё же стоит на него посмотреть. #js #yandex #frontend
* Длинная статья про то, почему весь тот синтаксический сахар, которым напичкан Coffee Script, [приводит к плохочитаемому коду](http://ceronman.com/2012/09/17/coffeescript-less-typing-bad-readability/). #javascript #coffee

Разное
------
* Строка поиска в GitHub стала выполнять функции омнибокса, позволяя [запускать разные команды](https://github.com/blog/1264-introducing-the-command-bar). #github
* И еще, GitHub сделал [поддержку oAuth токенов](https://github.com/blog/1270-easier-builds-and-deployments-using-git-over-https-and-oauth) в HTTPS транспорте. Теперь можно указывать токен вместо username:password. Кто-нибудь HTTPS использует? Я привык все по SSH клонировать. #github
* Для любителей Sublime2 — плагин реализующий [TODO листы](https://github.com/aziz/PlainTasks). Жаль, что я саблим не использую, выглядит симпатичненько. #develop
* Отличная статья Винсента Дриессена [про то как проектировать ПО](http://nvie.com/posts/open-sourcing-is-the-ultimate-isolation/), разбивая его на отдельные модули. Идея в том, чтобы разрабатывать каждый модуль изолированным, и так, будто ты завтра готовишься выложить его в OpenSource. Даже зафлэттерил ее, настолько понравилось! #develop
* Программисты во всем стараются упростить себе жизнь. Один вот, к примеру, написал [расширение к Photoshop](https://github.com/sapegin/PEW), позволяющее писать простые скрипты для экспорта изображений с нужными настройками в один клик. Подозреваю, что там и так можно было это делать с помощью макросов, но JS ведь прикольнее! #js #design
* AOL заопенсорсил свой инструмент для администрирования кластеров — [Trigger](https://github.com/aol/trigger). Как я понял из описания, эта такая запускалка команд на кластерах. К слову, у нас в Яндексе тоже есть нечто подобное, только называется Executer. #yandex #aol #networking #python
* <http://foauth.org> — некий Marty Alchin решил сделать HTTP прокси к сервисам, предоставляющим авторизацию по oAuth. Выглядит клево и избавляет от необходимости морочиться с получением токенов, когда пишешь какой-нибудь простенький скрипт. Параноики могут поднять такой прокси на своем сервачке, [проект в opensource](https://github.com/gulopine/foauth.org). #services #develop #python
