Title: Git helper for GitHub Users
Slug: hub
Date: 2011-04-14 12:26
Category: links
Tags: git
Lang: ru

Нашел тут [скриптик](http://defunkt.io/hub/), облегчающий работу с гитхабом из командной строки. Все что нужно, это иметь установленный ruby (в Mac OS X, он уже есть). Скрипт достаточно скачать куда-нибудь в `PATH`, и сделать на него алиас `alias git=hub`.

Для полноценной работы, нужно так же добавить в `~/.gitconfig` секцию с вашим именем и токеном:

    [github]
        user = svetlyak40wt
        token = а-тут-секретный-токен

После этого можно будет, к примеру, по-быстрому форкнуть мой проект [ForkFeed](http://github.com/svetlyak40wt/forkfeed), который, кстати, тоже полезен пользователям GitHub:

    git clone svetlyak40wt/forkfeed
    cd forkfeed
    git fork

Наслаждайтесь!
