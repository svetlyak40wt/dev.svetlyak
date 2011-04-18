Title: For-Else in Python
Slug: for-else
Date: 2011-04-18 11:18
Category: texts
Tags: python
Lang: ru

Пользовались ли вы когда-нибудь ключевым словом [`else`][else], совместно с `for`? Нет? Мне тоже не приходилось.
А оказывается, это чрезвычайно удобно в тех случаях, когда в теле цикла используется ключевое слово `break`.

Как работает `else`? Очень просто. Код этой секции выполняется в том случае, если основной цикл завершился
естественным образом, без эксепшена или вызова `break`.

То есть, это ключевое слово будет полезно тогда, когда вам нужно выполнить какой-то код только в том случае,
если в цикле были перебраны все элементы. Я на этом сделал аналог `switch` с поддержкой регекспов и значением
по-умолчанию:

    :::python
    import re
    REGEXES = (
        (r'some ([^ ]+)', lambda m, line: do_some(m, line)),
        (r'another ([^ ]+)', lambda m, line: do_another(m, line)),
    )
    REGEXES = tuple((re.compile(line), func) for line, func in REGEXES)

    def switch(text_to_check, regexes, default):
        for line, func in re:
            match = line.match(blah)
            if match is not None:
                func(match, line)
                break
        else:
            default(line)

    switch('blah minor', REGEXES, do_default_action)

[else]: http://docs.python.org/reference/compound_stmts.html#the-for-statement
