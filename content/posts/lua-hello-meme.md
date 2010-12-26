Title: Lua "Hello" meme
Slug: lua-hello-meme
Date: 2008-11-26 12:30
Tags: lua, fun
Category: texts
Lang: en
Description: Another hello world meme, written in lua.

Thanks to Eric for his [funny programming contest][contest].

In my [previos post][back], I show, how to write this meme in [bash][]. Today I had written it in [lua][]:

    :::lua
    print('Please enter your name: ')
    name = io.stdin:read()
    print('Please enter your age: ')
    age = tonumber(io.stdin:read())

    for i = 1, age do
        print(string.format("%2d) Hello, %s", i, name))
    end

[lua]: http://www.lua.org/manual/5.1/manual.html
[back]: http://aartemenko.com/texts/bash-meme/
[contest]: http://www.eflorenzano.com/blog/post/trying-start-programming-meme/
[bash]: http://tldp.org/LDP/Bash-Beginners-Guide/html/