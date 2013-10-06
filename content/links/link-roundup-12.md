Title: Link Roundup #12
Slug: link-roundup-12
Date: 2012-09-03 08:24
Category: links
Tags: roundup
Lang: ru

Сегодня много ссылок, и большинство из них, на разные GitHub проекты. А всё благодаря моему новому-кленовому [агрегатору персональной ленты событий с GitHub](http://gitorama.com/?utm_source=dev.svetlyak.ru&utm_campaign=roundup&utm_medium=blog-post).

Разработка
----------

* [Python-patterns](https://github.com/faif/python-patterns) — реализация разных паттернов на питоне. Но это только для тех, кто жизни не мыслит без того, чтобы писать все сверх-объектно-ориентированно. Кроче, большинство этих вещей в реальных программах на питоне, я ни разу не видел :) #python
* [Django Report Tools](https://github.com/evanbrumley/django-report-tools) — позволяет удобно вставлять в страницы графики. Генерируются они через google chart api. #django
* Еще, Гитхабом навеяло — простейший [асинхронный SMTP сервер](https://github.com/kennethreitz/inbox.py) для Python. By Kenneth Reitz. #python
* [Dagny](https://github.com/zacharyvoase/dagny) — Rails-like ресурсо-ориентированные вьюхи для Django. #django #python
* [Scaffold](https://github.com/Aaronontheweb/scaffold-py) — полезная питоновская утилитка, создающая первоначальную структуру нового Python проекта. #python #tools
* Большая статья про то, [как происходят выкладки](https://github.com/blog/1241-deploying-at-github) в GitHub. Если коротко, то они тестят код автоматом, потом выкатывают бранч в продакшн, если и там все хорошо, то бранч мерджится в master. Если все плохо, то либо чинят на месте пока не починят, либо откатываются обратно на мастер. Жаль не написали, как они БД туда-сюда откатывают. #github #develop

Фронтэнд
--------
* Есть такой плагин для многих текстовых редакторов — ZenCoding. По сути, это генератор HTML, который по строке, похожей на css селекторы, генерит html структуру. Так вот, [Sparkup](https://github.com/rstacruz/sparkup/), это реализация ZenCoding для vim.  #css #vim
* [Иконки браузеров](http://paulirish.deviantart.com/favourites/51528712) с пони из мультика My Little Pony. #art
* Ни много, ни мало, [30 советов](http://slodive.com/web-development/css-typography-tricks/) по веб-типографике. #css

Разное
------
* Описание устройства операционной системы [Plan 9](http://plan9.bell-labs.com/sys/doc/9.html). Читал как роман, настолько там всё красиво и продумано было. Интересно, ее где-нибудь все еще используют? #system #unix
* Еще один проект, использующий API GitHub — [Pelican мигратор](http://djangodash12.trilandev.com/). Сделан в рамках DjangoDash. Помогает перенести блог с нескольких популярных платформ на GitHub Pages. #django #python #github
* [Gitviz](https://github.com/kevinw/gitviz) — интересная, но на мой взгляд бесполезная, поделка, визуализирующая git репозиторий в виде дерева коммитов налету. Ты туда коммитишь, и картинка обновляется. #git
* @kennethreitz начал писать интересный документ: [Conduct of Code](https://github.com/kennethreitz/conductofcode/wiki). Пока там только наброски тем и оглавлений. #development
* Так же, Kenneth Reitz задумал создать сайт [pythonforhumans.org](https://github.com/kennethreitz/pythonforhumans.org), для пропаганды правильного образа жизни с Python :) #python
* А еще, на прошлой неделе я решил преписать Vim конфиги и попробовать использовать VAM — [Vim Addon Manager](https://github.com/MarcWeber/vim-addon-manager). А то у меня в vim файлах бардак порядочный! #vim
