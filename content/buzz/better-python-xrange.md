Title: Aналог python xrange, но лучше
Slug: better-python-xrange
Date: 2010-12-10 11:47
Category: texts
Tags: python, snippets
Lang: ru

Написал тут по необходимости вот такой аналог python xrange, но лучше:

    :::python
    def real_range(from_, to_, delta = 1):
        x = from_
        while x < to_:
            yield x
            x += delta

Он позволяет, например, итерироваться по датам с заданным timedelta:

    :::python
    from datetime import date, timedelta
    for x in real_range(
            date.today() - timedelta(356),
            date.today(),
            timedelta(1)):
        print x

Не понимаю, почему стандартный xrange так не умеет.
