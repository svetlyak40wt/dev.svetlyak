Title: Python functional "Hello" meme
Slug: python-functional-hello-meme
Date: 2008-11-26 12:49
Tags: python, fun, functional
Category: texts
Lang: en
Description: This is another interpretation of Eric's task. This time in functional way, python incarnation.

This is another interpretation of [Eric's task][contest]. This time in functional way, python incarnation.

    :::python
    import itertools, sys 
    [sys.stdout.write('%s) Hello, %s\n' % tuple(reversed(item))) \
        for item in itertools.izip(
            itertools.repeat(raw_input('Please enter your name: ')),
            xrange(int(raw_input('Please enter your age: '))))]

[contest]: http://www.eflorenzano.com/blog/post/trying-start-programming-meme/