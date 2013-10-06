Title: Black Jabber Magick
Slug: black-jabber-magick
Date: 2009-01-21 16:14
Tags: jabber, admin, erlang
Category: texts
Lang: en
Description: A short note, how to change user's password in ejabberd.

This is a very short note, how to change user's password in ejabberd if you have an access to the Erlang console.

Here is a sequence of the commands:


    :::bash
    [art@dhcp218-197:~]% ssh jabber-server.com
    [art@jabber-server.com:~]% sudo su - ejabberd
    [ejabberd@jabber-server.com:~]$ erl -sname username -remsh ejabberd@`hostname -s`
    (ejabberd@jabber-server.com)1> ejabberd_auth:set_password("username", "jabber-server.com", "test-password").


That's it. Just replace *jabber-server.com*, *username* and *test-password* with your real data.