Title: Link Roundup #1
Slug: link-roundup-1
Date: 2012-04-16 12:54
Category: links
Tags: python, roundup
Lang: ru

Решил делать еженедельные подборки ссылок на разные темы. Это первый такой пост.

* Думаю переползать с Munin на Collectd, но попутно наткнулся на проектик [python-munin](https://github.com/samuel/python-munin), упрощающий написание плагинов для Munin на python. Мне уже вряд ли пригодится. Кстати, для collectd тоже можно на питончике писать плагины, но запускаются они более разумно.
* На прошлой неделе я написал [things-periodical-tasks](https://github.com/svetlyak40wt/things-periodical-tasks), но позже осознал его бесполезность. Во-первых, в things есть периодические задачи, хоть их и неудобно добавлять, если нужно указывать дни недели. Во-вторых, на постоянно выключаемом ноуте, cron пропускает задачи, запланированные на то время, которое он проспал.
* [Yaxy](https://github.com/Kolyaj/Yaxy) — прокси сервер для разработчика, позволяет на лету подменять урлы, заголовки, куки, и т.д..
* [MongoDB Architecture](http://horicky.blogspot.com/2012/04/mongodb-architecture.html) — заметка про особенности разработки под MongoDB. Наверное всё это можно найти в официальной документации, но там оно разбросано по разделам, а здесь на одной странице.
* Амазон запустил [Cloud Search](http://aws.typepad.com/aws/2012/04/amazon-cloudsearch-start-searching-in-one-hour.html) и об этом не написал только ленивый. Вообще, довольно очевидная идея и странно, что ни один поисковый гигант до сих пор не выпустил такого продукта.
* Статейка про [Two Phase Commit](http://cookbook.mongodb.org/patterns/perform-two-phase-commits/) в MongoDB и прочих noSQL — про то, как в отсутствии нормальных транзакций, организовать гарантированное изменение нескольких объектов в базе данных.
* Статейка про [S.M.A.R.T](http://www.ixbt.com/storage/hdd-smart-testing.shtml) и то, что означают те или иные пункты отчета. Кстати, для OSX в Homebrew есть консольная утилитка smartmontools.
* В догонку, я нашел страницу с [описанием разных форков Homebrew](https://github.com/mxcl/homebrew/wiki/Interesting-Branches). И целых три форка Homebrew под Linux:

    * <https://github.com/paxan/homebrew>
    * <https://github.com/rubiojr/homebrew>
    * <https://github.com/ndevenish/homebrew>

    Из них попробовал пока только последний, от ndevenish. Но там не всё так гладко. Тот же collectd — не собирается потому что не видит dev библиотек, установленных в Ubuntu. Пока отложил.
