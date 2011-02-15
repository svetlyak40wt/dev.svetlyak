Title: Эволюция проектов на GitHub
Slug: forkfeed
Date: 2011-02-09 12:11
Category: texts
Tags: python
Lang: ru

Сегодня зарелизил небольшую но очень полезную тулзу для пользователей GitHub. Проект называется [Forkfeed][]. Он предназначен для слежения за развитием форков ваших проектов на гитхабе.

![](http://img-fotki.yandex.ru/get/5602/alexander-artemenko.e/0_73de3_97d804f1_L)  
by [GraemePow@flickr](http://www.flickr.com/photos/graeme_pow/4534266872/in/photostream/)

Часто бывает такое, что кто-то форкает ваш проект, начинает его развивать, а pull реквестов не присылает. А за всем ведь не уследишь. Поэтому я написал скрипт, который обходит все форки всех моих проектов, смотрит какие их коммиты новее моих, и создает Atom фид. [Фид][feed] обновляется по крону, на моем VPS. Теперь я всегда буду в курсе новых форков каждого из моих проектов.

[Forkfeed]: https://github.com/svetlyak40wt/forkfeed
[feed]: http://forkfeed.svetlyak.ru/svetlyak40wt.xml

