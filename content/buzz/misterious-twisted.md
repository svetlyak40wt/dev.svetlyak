Title: Загадочные глюки Python+Twisted
Slug: misterious-twisted
Date: 2010-09-02 18:52
Category: texts
Tags: twisted, python
Lang: ru

Таких глюков, какие я сейчас ловлю, программируя на Python+Twisted, я не видал
с тех пор, как перестал работать с ребятами, пишущими на смеси С и С++ с
маллоками и прочей дребеденью. Сплошная мистика.

Например.

Запускаю джаббер-бота в фореграунде — все работает. Запускаю как демона — нет.
Добавляю в одном месте такую строчку: `log.msg('blah: %r' % (command,))` снова
работает, даже как демон. Меняю на `log.msg('blah: ')` — опять не работает.

Просто какой-то ад!

Более того, даже если просто вывести в лог более длинную строчку, то тоже все
работает: `log.msg('blah: minor')`.

Вот сижу и охуеваю.

Кстати, на виртуалке под Python2.6 все работает и без этого шаманства.

