Title: Simple untar function for your shell
Slug: simple-untar-function-for-your-shell
Date: 2008-12-01 12:15
Tags: shell, utils
Category: texts
Lang: en
Description: Few days ago I wrote this simple shell function to untar gzipped and bzipped archives.

This simple function will save you a few keystrokes each time, when you need to unpack some tar archive.

Here we are! It's easy and should work in bash and zsh.

    :::bash
    function untar()
    {
        [ `basename $1 .gz`  != $1 ] && tar -zxvf $1 && return 0
        [ `basename $1 .bz2` != $1 ] && tar -jxvf $1 && return 0
    }