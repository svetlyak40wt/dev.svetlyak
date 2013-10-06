Title: Disassembler of Python byte code
Slug: disassembler-python-byte-code
Date: 2009-03-20 12:16
Tags: python, optimization
Category: texts
Lang: ru
Description: Краткий обзор модуля `dis` в Python.

Благодаря [StackOverflow][stack-post], я обнаружил интересный модуль в библиотеке языка Python - `dis`.

Это дизассемблер Python байт-кода в мнемоники.

Например, мы можем заглянуть внутрь двух функций, создающих словари:

    :::python
    >>> import dis
    >>> def a():
    ...     return {'one': 1, 'two': 2}
    ...
    >>> def b():
    ...     return dict(one=1, two=2)
    ...
    >>> dis.dis(a)
      2           0 BUILD_MAP                0
                  3 DUP_TOP
                  4 LOAD_CONST               1 (1)
                  7 ROT_TWO
                  8 LOAD_CONST               2 ('one')
                 11 STORE_SUBSCR
                 12 DUP_TOP
                 13 LOAD_CONST               3 (2)
                 16 ROT_TWO
                 17 LOAD_CONST               4 ('two')
                 20 STORE_SUBSCR
                 21 RETURN_VALUE
    >>> dis.dis(b)
      2           0 LOAD_GLOBAL              0 (dict)
                  3 LOAD_CONST               1 ('one')
                  6 LOAD_CONST               2 (1)
                  9 LOAD_CONST               3 ('two')
                 12 LOAD_CONST               4 (2)
                 15 CALL_FUNCTION          512
                 18 RETURN_VALUE

Здесь, `dis` показывает, что `dict` является вызовом функции, тогда как `{}` является чисто синтаксической конструкции в Python. Думаю, этот модуль может быть полезен, когда вы сомневаетесь, какая из конструкций являются более дорогостоящей.

[stack-post]: http://stackoverflow.com/questions/664118/whats-the-difference-between-dict-and
