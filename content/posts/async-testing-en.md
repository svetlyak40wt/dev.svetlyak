Title: Asynchronous testing with Twisted
Slug: async-testing
Date: 2011-03-01 10:53
Category: texts
Tags: python, twisted
Lang: en

Some time ago, [I tweeted][twitter] that I like to write unittests for programs, using a [Twisted][] framework. Tweets are short and there are not enough space for more comprehensive description, that is why I decided to write a separate post on this theme.

I am developing a distribute, fault-tolerant lock service. It is asynchronous and uses Twisted. Nodes talk to each other using TCP and custom text protocol, but provide a REST HTTP API for clients. It is very important to be consistent and durable, that is the reason I wrote tests before any actual lock implementation. They are functional, rather than unit-tests.

Well, my tests check an interaction among different nodes. Nodes exchange messages via network. How to run such tests? Should I start few separate processes? And if I should, then how to debug them?

Debugging threaded networking code is a complex task. But (drum roll), not with Twisted!

![](http://img-fotki.yandex.ru/get/5005/alexander-artemenko.e/0_755a1_e15d9963_L)  
by [dirkjanranzijn](http://www.flickr.com/photos/dirkscircusimages/2785357852/)

First, twisted allowed to run all five nodes in one process on one reactor, and now I am able to set `pdb.set_trace()` where I want.

Second, I replaced a networking layer with a mock objects, which deliver messages with some random delay. But I can drive the python's random generator which gives me ability to reproduce stochastic errors and debug them. It works as following:

* before the test `TestCase` class calls `random.seed(some_value)` and remembers the `some_value`;
* it test raises `AssertionError` besides a normal error message, `TestCase` prints `RANDOM SEED: some_value`;
* to run test, with random generator initialized explicitly, it should be decorated:

        :::python
        @seed(some_value)
        def test_my_broken_code(self):
          ...

Here are the class `TestCase` and the decorator `seed`:

    :::python
    import random
    import time

    from twisted.trial import unittest


    def seed(value):
        def decorator(func):
            func._random_seed = value
            return func
        return decorator


    class TestCase(unittest.TestCase):
        def _run(self, method_name, result):
            method = getattr(self, method_name)
            seed = getattr(method, '_random_seed', int(time.time()))
            random.seed(seed)

            def seed_info_adder(failure):
                failure.value.args = (failure.value.args[0] + ' (random seed: %s)' % seed,) + failure.value.args[1:]
                return failure

            d = super(TestCase, self)._run(method_name, result)
            d.addErrback(seed_info_adder)
            return d

Feel free to write your thoughts about this testing method, or send any suggestions.

[twitter]: http://twitter.com/svetlyak40wt/status/38659219838337024
[twisted]: http://twistedmatrix.com
