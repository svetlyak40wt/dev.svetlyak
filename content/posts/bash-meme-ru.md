Title: Bash meme
Slug: bash-meme
Date: 2008-11-25 11:36
Tags: bash, fun
Category: texts
Lang: ru

Сегодня, Эрик Флорензано начал [забавный конкурс][list]. По сути, это блоггинговая игра.

Правила очень просты:

1. Напишите программу, которая запрашивает имя пользователя и его возраст, а затем печатает "Привет {имя пользователя}" столько раз, сколько он прожил лет.
2. Выкложите эти правила и исходный код вашего решения и следующий листинг (включающий ваш) на вашем блоге.
3. Получите дополнительные очки, если программы на этом языке еще нет [в списке][list]!

Вот моя программа, написанная в [bash][]:

    :::bash
    #!/bin/bash
    echo -n 'Please enter your name: '
    read NAME
    echo -n 'Please enter your age: '
    read AGE

    for i in `seq $AGE`; do echo "$i) Hello, $NAME"; done

Он работает так же, как питоновский скрипт Эрика, просто запрашивает имя и возраст, а затем печатает приветствия.

Надеюсь, вместе мы сможем создать более длинный список, чем коллекции [Hello World][hello]. Наслаждайтесь!

[list]: http://www.eflorenzano.com/blog/post/trying-start-programming-meme/
[hello]: http://www.roesler-ac.de/wolfram/hello.htm
[bash]: http://tldp.org/LDP/Bash-Beginners-Guide/html/
