Title: Fuzzy testing в Python
Slug: fuzzy-testing-in-python
Date: 2010-11-18 14:33
Category: texts
Tags: snippets, python, testing
Lang: ru

Отлаживая скрипт, который должен быть надежен и безопасен, написал вот такой
небольшой хелпер:

    :::python
    def random_error(
        probability = 0.05,
        exceptions = (IOError, RuntimeError, DatabaseError, IntegrityError),
    ):
        if getattr(settings, 'RANDOM_ERRORS', False) and random.random() < probability:
            raise random.choice(exceptions)('blah')

И расставил вызовы этой функции по коду в местах, где наиболее вероятно
появление исключений: обращение к базе, диску или парсинг чего-нибудь.

Теперь, одной лишь опцией в `settings.py`, я могу включить эти ацкие глюки и
прогнать стресс-тест в таких непростых условиях.
