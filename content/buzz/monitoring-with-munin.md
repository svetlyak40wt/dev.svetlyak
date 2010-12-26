Title: Мониторинг логов с помощью Munin
Slug: monitoring-with-munin
Date: 2010-03-20 16:51
Category: texts
Tags: admin
Lang: ru

Недавно я перевел свой сайт svetlyak.ru на новый хостинг. И решил заодно нестроить мониторинг всяческих параметров, чтобы было все, как у "больших".

В качестве системы мониторинга, я решил попробовать Munin. Так как она показалась мне очень легко настриваемой, и заработала в Debian, что называется, из коробки.

Итак, установка оказалась проста:

    :::bash
    sudo aptitude install munin munin-node munin-plugins-extra
    sudo /etc/init.d/munin-node start

После этого большое количество параметров буду мониториться автоматически.

К сожалению, я не нашел специального плагина для мониторинга access логов lighttpd. Но все оказалось просто. В состав munin-node входит скрипт под названием loggrep. С его помощью можно пониторить появление новых строк в любых лог файлах.

Итак, что же потребовалось, чтобы сконфигурировать loggrep?

Для начала, я сделал пару симлинков:

    :::bash
    sudo ln -s /usr/share/munin/plugins/loggrep /etc/munin/plugins/lighttpd_svetlyak
    sudo ln -s /usr/share/munin/plugins/loggrep /etc/munin/plugins/lighttpd_svetlyak_errors

по одному, на каждый график.


Далее, я написал вот такой конфиг, в котором указал что следует грепать и откуда брать логи:

    # /etc/munin/plugin-conf.d/svetlyak
    [lighttpd_svetlyak]
    user root
    env.logfile /home/art/log/lighttpd/svetlyak-access.log
    env.title Lighttpd svetlyak.ru
    env.label 20x
    env.regex HTTP/\d+.\d+" 20\d
    env.colour 00ff00
    env.label_40x 40x
    env.regex_40x HTTP/\d+.\d+" 40\d
    env.colour_40x ffcc00
    env.label_50x 50x
    env.regex_50x HTTP/\d+.\d+" 50\d
    env.colour_50x 990000


    [lighttpd_svetlyak_errors]
    user root
    env.logfile /home/art/log/lighttpd/svetlyak-access.log
    env.title Lighttpd svetlyak.ru 500
    env.label 50x
    env.regex HTTP/\d+.\d+" 50\d
    env.colour 990000

В итоге, получается вот такая красота:

![](http://stats.svetlyak.ru/svetlyak.ru/locum.svetlyak.ru-lighttpd_svetlyak-day.png)

Есть, правда, одно "но". Директива colour, не поддерживается стандартным loggrep, так что его пришлось немного доработать. Фича полезная, так как позволяет раскрашивать графики в любые цвета. [Патч][patch] уже в багтрекере разработчика. Качайте и пользуйтесь.

[patch]: http://munin-monitoring.org/attachment/ticket/897/0001-Colour-support-for-loggrep-munin-plugin.patch
