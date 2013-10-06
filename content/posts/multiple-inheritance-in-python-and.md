Title: Multiple inheritance in the Python and «diamond problem»
Slug: multiple-inheritance-in-python-and
Date: 2008-08-27 04:53
Tags: python
Category: texts
Lang: en
Description: 

Hello, all!

Today I've write small and simple test for multiple inheritance in the python:

    :::python
    #!/usr/bin/env python
    class Base(object):
        def say(self, indent = 0):
            print '%s%s' % ('\t'*indent, 'Base')
    class ChildA(Base):
        def say(self, indent = 0):
            print '%s%s' % ('\t'*indent, 'ChildA')
            super(ChildA, self).say(indent+1)
    class ChildB(Base):
        def say(self, indent = 0):
            print '%s%s' % ('\t'*indent, 'ChildB')
            super(ChildB, self).say(indent+1)
    class ChildC(ChildA, ChildB):
        def say(self, indent = 0):
            print '%s%s' % ('\t'*indent, 'ChildC')
            super(ChildC, self).say(indent+1)
    obj = ChildC()
    obj.say()


Here is the output of the program:

    ChildC
        ChildA
            ChildB
                Base

As you can see, methods are evaluated in right order!

See more information about multiple inheritance in the [official Python Tutorial][1].

   [1]: http://docs.python.org/tut/node11.html#SECTION0011510000000000000000