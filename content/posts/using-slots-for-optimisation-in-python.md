Title: Using __slots__ for optimisation in python
Slug: using-slots-for-optimisation-in-python
Date: 2008-09-09 06:26
Tags: tools,optimisation,python,memory
Category: texts
Lang: en
Description: 

Do you know anything about python's __slots__ construction? I did't before this day.

But __slots__ in the python exists from version 2.2. It's main purpose is memory optimisation because it allow to get rid of __dict__ object, which created by interpreter for each instance of class.

If you create many small objects, with predefined structure, and meet a memory limit, than __slots__ can help you to overcome that limitation.

But remember, that early optimisation is the root of all evil. Furthermore, __slots__ has many [limitations that you need to be aware][2]. For example, you can't use multiple inheritance and must be very careful if usual inheritance too.

As I am very interested in the different optimisation technics, I desided to make a small test.

I have found an interesting python library, that helps to measure memory usage. It's name is [Guppy][3].

So, I write this simple test, which create tuples of one million instances of simple class. Every object hold two attibute 'a' and 'b'. First class is standart, second uses __slots__ to optimise memory footprint.

    :::python
    #!/usr/bin/env python
    import sys
    import guppy
    import time

    class Test1(object):
        def __init__(self):
            self.a = 1
            self.b = 2

    class Test2(object):
        __slots__ = ('a', 'b')
        def __init__(self):
            self.a = 1
            self.b = 2

    if __name__ == '__main__':
        num = 1000000
        cls = Test1

        if len(sys.argv) == 2:
            if sys.argv[1] == '2':
                cls = Test2

        l = tuple(cls() for i in xrange(num))

        h = guppy.hpy()
        print h.heap()

If you run this program without params, it would create a 1000000 usual instances and output something like that:


    Partition of a set of 2020446 objects. Total size = 169426216 bytes.
     Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
         0 1000000  49 136000000  80 136000000  80 dict of __main__.Test1
         1 1000000  49 28000000  17 164000000  97 __main__.Test1
         2   4901   0  4178264   2 168178264  99 tuple
         3   9527   0   611920   0 168790184 100 str
         4   1416   0    96288   0 168886472 100 types.CodeType
         5     61   0    89704   0 168976176 100 dict of module
         6    155   0    85784   0 169061960 100 dict of type
         7   1342   0    75152   0 169137112 100 function
         8    170   0    73360   0 169210472 100 type
         9    119   0    68408   0 169278880 100 dict of class


Now run program with one argument '2'. In this case, output will look like that:


    Partition of a set of 1020446 objects. Total size = 33426216 bytes.
     Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
         0 1000000  98 28000000  84  28000000  84 __main__.Test2
         1   4901   0  4178264  12  32178264  96 tuple
         2   9527   1   611920   2  32790184  98 str
         3   1416   0    96288   0  32886472  98 types.CodeType
         4     61   0    89704   0  32976176  99 dict of module
         5    155   0    85784   0  33061960  99 dict of type
         6   1342   0    75152   0  33137112  99 function
         7    170   0    73360   0  33210472  99 type
         8    119   0    68408   0  33278880 100 dict of class
         9     65   0    49928   0  33328808 100 dict (no owner)


Pay attention at the top line in the first stats. It states, that 136000000 was reserved to the "dict of __main__.Test1". Seconds stats does not countain such line because of __slots__ was used for optimisation.

Now we can calculate a profit of the __slots__ in that particular case. It is (136000000 + 28000000) / 28000000 or 5 times! Second run reqire a 5 times less memory than first! It's amazing! But remember about warning you was given to.

Also see these links:

  * Metaclass for [automated __slots__ creation][4].
  * Nicolás Miyasato's post [about __slots__ usage][5] in every day life.

   [2]: http://groups.google.com/group/comp.lang.python/msg/0f2e859b9c002b28
   [3]: http://guppy-pe.sourceforge.net/
   [4]: http://code.activestate.com/recipes/435880/
   [5]: http://mypythonnotes.wordpress.com/2008/09/04/__slots__/