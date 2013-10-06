Title: Асинхронное тестирование с Twisted
Slug: async-testing
Date: 2011-03-01 10:53
Category: texts
Tags: python, twisted
Lang: ru

Недавно [я писал][twitter] в твиттере, что мне нравится писать юниттесты для программ, использующих Python фреймворк [Twisted][]. В твиттере всего не уместишь, поэтому я решил оформить пояснение отдельным постом.

Дело в том, что я сейчас разрабатываю распределенный, отказоустойчивый сервис локов. Внутри он асинхронный, использует Twisted. Ноды общаются между собой по TCP, используя собственный текстовый протокол, а наружу предоставляют HTTP интерфейс в духе REST. Мне очень важно обеспечить стабильность и консистентность моего сервиса, потому что от него будет зависеть синхронизация других задач. Поэтому первое что я сделал, это написал тесты. Эти тесты даже и unit-тестами назвать нельзя, они скорее, функциональные.

Итак, мои тесты тестируют взаимодействие нескольких нод. Ноды обмениваются данными по сети. Но как такой тест запускать? Стартовать ли несколько процессов? И если да, то как их отлаживать?

Отладка сетевого взаимодействия сложная штука. Но тут (барабанная дробь), на сцену выходит Twisted!

![](http://img-fotki.yandex.ru/get/5005/alexander-artemenko.e/0_755a1_e15d9963_L)  
by [dirkjanranzijn](http://www.flickr.com/photos/dirkscircusimages/2785357852/)

Во-первых, твистед позволил мне запустить все мои пять нод в одном процессе, на одном реакторе. Это позволило ставить `pdb.set_trace()` в любом месте, где мне нужен отладчик.

Во-вторых, я заменил сетевой слой, который они используют для общения, на его упрощенную модель, где сообщения доставляются с некоторой случайной задержкой. Так как генератором случайных чисел можно управлять, то я получил возможность воспроизводить разные "псевдо-случайные" глюки, происходящие в моей системе.  Вот как выглядит процесс тестирования (все происходит автоматически):

* перед запуском теста, `TestCase` класс вызывает `random.seed(some_value)` и запоминает значение `some_value`;
* если тест сломался, то помимо обычного сообщения об ошибке, `TestCase` выводит `RANDOM SEED: some_value`;
* чтобы запустить тест, явно инициализировав генератор случайных чисел, я его декорирую:

        :::python
        @seed(some_value)
        def test_my_broken_code(self):
          ...

Вот класс `TestCase` и декоратор `seed`, реализующие данную функциональность:

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

Что думаете по поводу такого метода отладки? <span style="color: white;">13558447.88548999.1298975203.fe8d17be47add1425588f6f16d9ae6e9 и 1120000000000244.1354.1298974870.96d80d1dda087b5185ebddd707442782</span>

[twitter]: http://twitter.com/svetlyak40wt/status/38659219838337024
[twisted]: http://twistedmatrix.com
