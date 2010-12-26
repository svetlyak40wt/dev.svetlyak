Title: Pdb decorator
Slug: pdb-decorator
Date: 2010-12-16 14:43
Category: texts
Tags: python, snippet
Lang: ru

Нарисовал тут pdb decorator. Он полезен, когда отлаживаешь функцию, обернутую
большим кол-вом декораторов, например какую-нибудь Django вьюху.

    :::python
    from functools import wraps

    def pdb_deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            import pdb;pdb.set_trace()
            return func(*args, **kwargs)
        return wrapper

