Title: Link Roundup #9
Slug: link-roundup-9
Date: 2012-07-23 10:45
Category: links
Tags: roundup
Lang: ru

Разработка
----------

* Поставил на попробовать SourceTree, с поддержкой git-flow. Хорошо работает только с локальными файлами, с подключенными по sshfs — вообще никак. Откатился на консольный вариант.
* Стал применять [Tmuxinator](https://github.com/aziz/tmuxinator). Хотя я не использую сплиты внутри tmux, все равно этот конфигуратор кажется мне полезным. Оказалось, что его лучше ставить из исходников, с  Github. Тогда он будет уметь подхватывать конфиги из текущей директории, а не только их HOME.
* [Пример](https://github.com/lukaszkorecki/DotFiles/blob/master/tmuxinator/work-ui.yml) достаточно сложного конфига для Тмуксинатора.
* [StGit](http://www.procode.org/stgit/doc/tutorial.html) скрипты для хранения патчей в Git репозитории. Мне такое пока не нужно, но может кому пригодится.

Разное
------

* Про [разные версии объектно-ориентированного CSS](http://cwebbdesign.tumblr.com/post/23666803241/scalable-and-maintainable-css-approaches). Описываются преимущества и недостатки OOCSS, DRYCSS и SMACSS.
* Про то, [как работается в GitHub](http://opensoul.org/blog/archives/2012/06/05/whats-it-like-to-work-at-github/). Со слов Брэндона Кипера, это немного похоже на анархию, в хорошем смысле этого слова — каждый несет ответственность за то, что он делает.
* Статья с HighScalability про то, как ["масштабировали" сервис iDoneThis](http://highscalability.com/blog/2012/6/20/idonethis-scaling-an-email-based-app-from-scratch.html). Почему в кавычках, да потому что ребята в конце делают вывод: "Лучше мы будем держать всё на одном сервере, а почту рассылать через [SendGrid](http://sendgrid.com/).". Смешно.
