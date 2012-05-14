Title: Link Roundup #3
Slug: link-roundup-3
Date: 2012-05-14 16:06
Category: texts
Tags: roundup
Lang: ru

Разработка
----------

* Что-то пошла мода на "легковесные" очереди задач. Недавно Vincent Driessen [опубликовал свой RQ](http://python-rq.org/), а теперь вот и [David Cramer пишет](http://justcramer.com/2012/05/04/distributing-work-without-celery/), что они в DISCUS пришли к чему-то подобному.
* На Highscalability появилась [ссылка на новую статью про Paxos](http://highscalability.com/blog/2012/5/10/paper-paxos-made-moderately-complex.html). Говорят, там всё хорошо расписано, и обсуждаются детали реализации.
* Про то, что [масштабируемые сервисы](http://highscalability.com/blog/2012/5/9/cell-architectures.html) нужно разделять переборками, чтобы повысить их плавучесть.
* [MailCatcher](http://mailcatcher.me/) — простой SMTP сервер, для отладки отправки писем. Перехватывает все проходящие через него сообщения, и показывает из в веб-интерфейсе.
Попробовал [swiftypy.com](http://swiftype.com/) — поисковый движок для сайтов. Морфологию русскую, увы, не поддерживает. Но выглядит круто. И пока бесплатен.
* Небольшая заметка [о том, как ребята из Pinterest продвигают формат oEmbed](http://www.quora.com/Pinterest/How-does-Pinterest-know-the-title-and-creator-when-I-pin-a-deep-linked-Flickr-image-1), и с его помощью по непонятному урлу картинки с flickr, получают реальный адрес страницы, с этим изображением.
* Статья про то, как [применять GitFlow и работать с GitHub](http://qq.is/article/git-flow-on-github). Правда ничего не говорится о том, как майнтейнер апстрима будет мерджить твою feature ветку, ведь если он сделает это через интерфейс гитхаба, то git-flow будет нарушен. Жаль, gitflow мне приглянулся.
* Статья про то, почему команда GitHub [не использует git-flow](http://scottchacon.com/2011/08/31/github-flow.html) в своей работе.
* Статья [о том, как устроен Ginger](http://lincolnloop.com/blog/2012/apr/23/ginger-tech-stack/) — сервис общения для команд. Схема асинхронного IO такая: Django -> Redis PubSub -> Node.js -> Socket.io -> Браузер.
* Обширное, хоть и старое (2008) года, [сравнение JSON библиотек](http://deron.meranda.us/python/comparing_json_modules/) для Python.
* [Антипаттерны деплоя Python](http://hynek.me/articles/python-deployment-anti-patterns/) кода. Согласен со всеми пунктами.
* Статья про то, [как кластеризуют документы](http://blog.getprismatic.com/blog/2012/4/17/clustering-related-stories.html) ребята из стартапа Prismatic. Присутствует пара практических советов, как бороться с нехваткой памяти и ресурсов CPU при больших объемах подобных вычислений. Суть проста — не хранить и не делать лишнего.
* Пост про то, [почему плохо заводить организации](http://www.mikealrogers.com/posts/face-of-the-faceless.html) для проектов на GitHub.
* Про [динамическую подгрузку](http://blog.arongriffis.com/post/dynamic-virtualenvwrapper) функций virtualenvwrapper и [скринкастик про сам враппер](http://mathematism.com/2009/07/30/presentation-pip-and-virtualenv/). Посмотрел всё это и и понял, что мне это не нужно, потому что я крайне редко переключаюсь между окружениями в одной консоли, у меня для этого tmux есть.

Полезные сервисы
----------------

* [GitHire](http://githire.com/) — сервис для найма активных гиттеров.
* [git.io](https://github.com/blog/985-git-io-github-url-shortener) — сокращала урлов для GitHub. Оказывается уже почти полгода существует, а я и не знал.

