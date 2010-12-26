Title: Disassembler of Python byte code
Slug: disassembler-python-byte-code
Date: 2009-03-20 12:16
Tags: python, optimization
Category: texts
Lang: en
Description: A short overview of `dis` python mudule.

Thanks to [StackOverflow][stack-post], I have discovered an interesting module in python's library — `dis`.

It is a disassembler of python byte code into mnemonics.

For example, for can view into a functions which create dicts:

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

Here, dis shows you, that `dict` is a function call, whereas `{}` is a pure python syntax construction. I think, that this module can be useful when you in doubt, why some constructions are more expensive than others.

[stack-post]: http://stackoverflow.com/questions/664118/whats-the-difference-between-dict-and