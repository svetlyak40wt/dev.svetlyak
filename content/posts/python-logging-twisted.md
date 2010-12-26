Title: Python Logging in Twisted
Slug: python-logging-twisted
Date: 2010-11-28 03:27
Tags: python, twisted
Category: texts
Lang: en
Description: 

This is a way to turn on a standart pyton's logging support in the Twisted. But it is broken. Really. For example, this is my default log format: `"%(asctime)s %(process)s/%(thread)s %(levelname)s %(name)s %(filename)s:%(lineno)s %(message)s"`, and this is piece of log which I get using `twisted.python.log.PythonLoggingObserver`:

    2010-11-28 03:15:09,027 7571/-1220024640 INFO twisted log.py:508 Log opened.
    2010-11-28 03:15:09,028 7571/-1220024640 ERROR blah server.py:37 blah minor
    2010-11-28 03:15:09,031 7571/-1220024640 INFO twisted log.py:508 lock.LockFactory starting on 4001
    2010-11-28 03:15:09,032 7571/-1220024640 INFO twisted log.py:508 Starting factory <lock.LockFactory instance at 0x8755d2c>
    2010-11-28 03:15:09,033 7571/-1220024640 INFO twisted log.py:508 twisted.web.server.Site starting on 9001
    2010-11-28 03:15:09,034 7571/-1220024640 INFO twisted log.py:508 Starting factory <twisted.web.server.Site instance at 0x875a18c>

Did you see these `log.py:508` everywhere? This is wrong! Wrong! But there is the simple way to fix it:

    :::python
    import os
    import twisted
    import logging
    _srcfile = twisted.python.log.__file__
    if _srcfile[-4:].lower() in ['.pyc', '.pyo']:
        _srcfile = _srcfile[:-4] + '.py'
    _srcfile = os.path.normcase(_srcfile)
    logging._srcfile = _srcfile

After this fix, the log will have the right file and line numbers in it:

    2010-11-28 03:18:07,763 7710/-1220380992 INFO twisted server.py:35 Log opened.
    2010-11-28 03:18:07,764 7710/-1220380992 ERROR blah server.py:37 blah minor
    2010-11-28 03:18:07,766 7710/-1220380992 INFO twisted tcp.py:861 lock.LockFactory starting on 4001
    2010-11-28 03:18:07,767 7710/-1220380992 INFO twisted protocol.py:44 Starting factory <lock.LockFactory instance at 0x8755d2c>
    2010-11-28 03:18:07,769 7710/-1220380992 INFO twisted tcp.py:861 twisted.web.server.Site starting on 9001
    2010-11-28 03:18:07,770 7710/-1220380992 INFO twisted protocol.py:44 Starting factory <twisted.web.server.Site instance at 0x875a18c>

Have a fun, read sources!

**Update**: I created [a ticket](http://twistedmatrix.com/trac/ticket/4749) in Twisted's trac.