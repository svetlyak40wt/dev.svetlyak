Title: Unittesting With Tdaemon And Tmux
Slug: unittesting-with-tdaemon-and-tmux
Date: 2012-04-06 16:39
Category: texts
Tags: python
Lang: ru

Некоторое время назад я нашел интересный watchdog для запуска юнит-тестов — [tdaemon][]. Инетересн он был прежде всего тем, что
работал без использования inotify, что позволяло мне запускать его в диреткториях, подмонтированных внутрь VirtualBox.

Впрочем, [tdaemon][] оказался написан из рук вон плохо. Он тормозил, и поддерживал лишь ограниченный список систем для запуска юнит-тестов.
Зато это проект на Python. В итоге, я переписал там основной функционал. Теперь он работает шустро, не грузит зря проц бесконечным поллингом файловой системы.

На днях я, решив попробовать новый севис для записи скринкастов, [сделал ролик][ascii], в котором демонструрую работу с [tdaemon][], [tmux][] и специальным плагином [nose-notify-tmux][], который умеет показывать прогресс юниттестов прямо в табике [tmux][].

Вот уже производная этого ролика, переснятая и с саундтреком:

<iframe src="http://player.vimeo.com/video/39888128" width="500" height="281" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>

Кто хочет нормального качества, тем в [ascii плеер][ascii].


[tdaemon]: https://github.com/svetlyak40wt/tdaemon/tree/develop
[nose-notify-tmux]: https://github.com/svetlyak40wt/nose-notify-tmux
[tmux]: http://tmux.sourceforge.net/
[nose]: http://pypi.python.org/pypi/nose
[ascii]: http://ascii.io/a/228
