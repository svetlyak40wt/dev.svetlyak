Title: Don't be lazy when writing 'if' statements in the Python
Slug: dont-be-lazy-when-writing-if-statements
Date: 2008-07-30 08:47
Tags: tips,python
Category: texts
Lang: en
Description: Example of stupid mistake in the python's 'if' statement.

If you want to check some object is None, don't be lazy, write full statement like this:

    :::python
    res = someFunction()
    if res is None:
        print 'blah-minor'

If you write:

    :::python
    if res:
        do_something_useful()

then you can get strange behavior, because not all objects evaluate to True.

For example, try this code:

    :::python
    import xml.etree.ElementTree as ET e = ET.Element('blah') if e: print 'Hello from elementtree'

You'll be surprised.