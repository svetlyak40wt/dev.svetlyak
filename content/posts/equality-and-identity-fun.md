Title: Equality and identity fun with python
Slug: equality-and-identity-fun
Date: 2009-02-18 18:11
Tags: python, tips
Category: texts
Lang: en
Description: A few asserts to check integer types. Be careful!

    :::python
    >>> assert( int(0) is not long(0) )
    >>> assert( int(0) == long(0) )

So, never write like this:

    :::python
    if var is 0:
        print 'Cool!'

Because if `type(var) == 'long'` it does not work.