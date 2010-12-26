Title: Как временно увеличить себе объем памяти на VPS?
Slug: swap-on-vps
Date: 2010-03-19 07:38
Tags: hosting
Category: texts
Lang: ru

Придумал, как временно увеличить себе объем памяти на новом VPS. Просто
добавил еще swap:

    :::bash
    dd if=/dev/zero of=/var/swap bs=1024 count=262144
    mkswap -f /var/swap
    swapon /var/swap

Оперативы пока всего 128 мегов, за 250 р/мес, по моему нормально.

Посмотрим, как заживут питоньи процессы после переноса [http://pthings.ru][1],
[http://aartemenko.com][2] и [http://martemenko.com][3].

[1]: http://pthings.ru
[2]: http://aartemenko.com
[3]: http://martemenko.com
