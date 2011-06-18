Title: Bash meme
Slug: bash-meme
Date: 2008-11-25 11:36
Tags: bash, fun
Category: texts
Lang: en
Description: A fun contest — to implement a basic program in any language.

Today, Eric Florenzano started [a funny contest][list]. He suggested the idea for new blogging game.

Rules are quite simple:

1. Implement a program that takes in a user's name and their age, and prints hello to them once for every year that they have been alive.
2. Post these rules, the source code for your solution, and the following list (with you included) on your blog.
3. Bonus points if you implement it in a language not yet seen [on the following list][list]!

Here is my program, written in [bash][]:

    :::bash
    #!/bin/bash
    echo -n 'Please enter your name: '
    read NAME
    echo -n 'Please enter your age: '
    read AGE

    for i in `seq $AGE`; do echo "$i) Hello, $NAME"; done

It's behaviour the same as Eric's python script. It just retrives you name and age, and then print some greetings.

I hope, together we can create a more long list, than a [Hello World][hello] collection. Have a fun!

[list]: http://www.eflorenzano.com/blog/post/trying-start-programming-meme/
[hello]: http://www.roesler-ac.de/wolfram/hello.htm
[bash]: http://tldp.org/LDP/Bash-Beginners-Guide/html/
