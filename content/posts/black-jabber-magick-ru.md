Title: Black Jabber Magick
Slug: black-jabber-magick
Date: 2009-01-21 16:14
Tags: jabber, admin, erlang
Category: texts
Lang: ru
Description: Короткая заметка о том, как изменить пароль пользователя в ejabberd.

Это очень короткая заметка о том, как изменить пароль пользователя в ejabberd, если у вас есть доступ к консоли Erlang.

Вот последовательность команд:

    :::bash
    [art@dhcp218-197:~]% ssh jabber-server.com
    [art@jabber-server.com:~]% sudo su - ejabberd
    [ejabberd@jabber-server.com:~]$ erl -sname username -remsh ejabberd@`hostname -s`
    (ejabberd@jabber-server.com)1> ejabberd_auth:set_password("username", "jabber-server.com", "test-password").


Вот и всё. Просто замените *jabber-server.com*, *username* и *test-password* на реальные данные.
