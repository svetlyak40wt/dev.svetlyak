* Еще один инструмент для конфигурирования серверов — [Ansible](https://github.com/ansible/ansible/). Тот же Salt, вид сбоку. Но поскольку я уже все скрипты на Salt переписал, то Ansible даже и пробовать не стану. #deploy #misc
* Отличная статья Андрея Светлова [про то, как работает сборщик мусора в Python](http://asvetlov.blogspot.ru/2013/05/gc.html). #develop #python
* Заметка Джейсона Фрайда, [про то, как важно уметь быстро клепать на коленке](http://www.inc.com/magazine/201305/jason-fried/the-importance-of-quick-and-dirty.html). Джейсон – один из сооснователей [37 Signals](http://37signals.com/), расстраивается, что они растеряли этот замечательный навык, позволяющий побыстрому собрать черновой вариант сервиса за пару-тройку дней. Он считает, что это крайне важное умение для любой IT компании, и тут я с ним полностью согласен. #misc
* Интересное [расширение возможностей](https://github.com/TylerBrock/mongo-hacker) консольного MongoDB клиента. Там и подстветка json, и разный синтаксический сахар для построения запросов и апдейтов (почти как в Django ORM). Ставится элементарно. #mongodb #develop
* Винсент Дриессен рассказывает про [будущие улучшения в pip-tools](http://nvie.com/posts/better-package-management/). Думаю, они идут в правильном направлении, судя по описанию, pip-sync — просто песня. Попробовать можно уже сейчас. #python #develop
* [Пара скриптов](http://stackoverflow.com/questions/3462955/putting-git-hooks-into-repository) для установки и запуска git хуков. #git #misc
* Потрясающий [сайт Брета Виктора](http://worrydream.com/). Про дизайн и всякое такое. Смотреть обязательно! #design
* Вот не любят 1С, из-за русских операторов. Но что-то в этом есть. Встречайте: Йоба – язык для чотких пацанов: http://sorokdva.net/ #misc #fun
* Global Game Jam — эдакий хакатон для разработчиков игр. #misc
* [Ready For Zero](https://www.readyforzero.com/) — интересный стартап для тех кто берет кредиты. Жаль, что пока работает только в US. #misc
* Сводка из синтетических [тестов кучи веб-фреймворков](http://www.techempower.com/benchmarks/). По ним хорошо видно, как быстро начинают сравниваться в производительности динамические и компилируемые языки, когда дело доходит до более реальных задач. #develop
* На канале lisp, меня навели на две библиотечки, которые решают задачу, сходную с Plumber от Prismatic. Первая библиотечка — [Cells](http://common-lisp.net/project/cells/), вторая — [computed-class](http://common-lisp.net/project/computed-class/index-old.shtml). #lisp
* Всё больше проектов начинают использовать Go.

Так, ребята из Discus недавно заявили, что переписали часть своей backend логики с Python на Go, и добились увеличения производительности на несколько порядков — собщения теперь обрабатываются не несколько минут, а 10 миллисекунд.

Кроме этого, разработчики MongoDB объявили, что они переписали свою тулзу для бэкапа с Java на Go, и очень счастливы.

Пруфлинки:

* http://blog.disqus.com/post/51155103801/trying-out-this-go-thing

* http://blog.mongodb.org/post/51643994762/go-agent-go

#develop #go
* Про [использование format](http://lisper.ru/pcl/a-few-format-recipes) в lisp. Разные примеры и описание возможностей. На русском. #lisp
* Допилил скрипт, устанавливающий Graphite: https://github.com/svetlyak40wt/graphite-node на Ubuntu Precise заводится без всяких усилий! #develop #monitoring
