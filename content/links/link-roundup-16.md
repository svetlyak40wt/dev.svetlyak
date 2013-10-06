Title: Link Roundup #16
Slug: link-roundup-16
Date: 2012-10-01 15:36
Category: links
Tags: roundup
Lang: ru

Разработка
----------

* Оказывается, Spotify выложил в opensource свою системы для распределенного выполенения задач — [Luigi](https://github.com/spotify/luigi). По описанию, она более фичастая чем Celery, но завязана на Hadoop :( #python #develop
* Искал python альтернативу ruby библиотечке [Chronic](https://github.com/mojombo/chronic) и нашел пример того, [как парсить даты на естественном языке, с помощью PyParsing](http://pyparsing.wikispaces.com/UnderDevelopment#toc0). #python #ruby
* Ruby [скрипт](http://brettterpstra.com/logging-with-day-one-geek-style/) для добавления записей в OneDay. #misc
* [Интересный способ](http://linsong.github.com/2010/07/24/debugger-with-source-view-using-tmux.html) отлаживаться в консоли с помощью Tmux и Vim. Оказывается, Tmux позволяет передавать вывод одного из окон в другую программу, и основываясь на этом, Vincent Wang сделал прокси, которая позволяет открыть rdb и vim в сплите Tmux и видеть иходник, который дебажишь в данный момент. #ruby #tmux
* [Pyquery](http://pypi.python.org/pypi/pyquery/) — python библиотечка для доступа к элементам html страниц с помощью селекторов, по типу того, как это сделано в jQuery. #python
* [Cram](https://bitheap.org/cram/) — утилита для функционального тестирования программ командной строки. Если у вас есть конскольные утилитки, то для них можно написать тесты, а cram позаботится об их выполнении. #develop #testing #console
* Винсент Дриессен сделал штуку, которую я давно хотел — [утилиту, проверяющую актуальность python модулей](http://nvie.com/posts/pin-your-packages/), поставленных через pip. Я всегда прописываю версии пакетов в requirements.txt, и понятное дело, они устаревают. Теперь с помощью [pip-review](https://github.com/nvie/pip-tools), можно узнать, какие появились новые версии! #python #pip
* [Sub](https://github.com/37signals/sub/) — мини фреймворк от "37 Сигналов", позволяющий писать утилиты командной строки с подкомандами. #shell #unix
* [Python-instagram](https://github.com/Instagram/python-instagram) — библиотека для взаимодействия с Instagram из python. Быстренько написал с ее помощью [модуль для TheBot](https://github.com/svetlyak40wt/thebot-instagram), который каждый 15 минут постит в канал новую фоточку. #python #instagram #thebot

Фронтэнд
--------

* [Recess](https://github.com/twitter/recess) — CSS валидатор от разработчиков Twitter. Прогнал им CSS-ку от <http://dev.svetlyak.ru>, боже ж мой, сколько там ошибок!!! :) #css #frontend
* [Hummer.js](https://github.com/EightMedia/hammer.js) — библиотека для обработки жестов на мобильных устройствах с сенсорным экраном. #frontend #js
* [Lovely.io](https://github.com/MadRabbit/lovely.io) — фреймворк для разработки клиент-сайда. Немного напомнил мне Яндексовый БЭМ, и нашу библиотеку блоков LEGO. #js #css #frontend #framework

Разное
------

* Некий Mark O'Connor [делится своим опытом разработки на iPad](http://yieldthought.com/post/31857050698/ipad-linode-1-year-later). Если коротко, то для него iPad это "тонкий" клиент, а вся разработка идет на сервере, под скрином и в Vim. #develop
* GitHub снова пишет о стратегии "release early". На этот раз, про то, [как они научились автоматически](https://github.com/blog/1271-how-we-ship-github-for-windows) раскатывать Windows клиент. Очень красивые графики обращений к API из разных версий клиента, рекомендую взглянуть. #github
* Noah Kagan пишет про свой [опыт увольнения из Facebook](http://okdork.com/2012/09/29/why-i-got-fired-from-facebook-a-100-million-dollar-lesson/) и рассказывает, какие полезные уроки он извлек из этого. #misc #management
* Весьма занятное [описание процесса найма в GitHub](https://github.com/blog/1269-the-github-hiring-experience). #misc
* [Spectacle](http://spectacleapp.com/) — попытка сделать оконный менеджер OSX более похожим на tiled собратьев. Spectacle позволяет посредством шоткатов управлять размером и положением окон, при чем более гибко, чем сама OS. #osx #misc
