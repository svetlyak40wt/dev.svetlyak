Title: Порядок сортировки стандартных моделей Django
Slug: django-user-ordering
Date: 2010-12-10 14:14
Category: texts
Tags: django, snippet
Lang: ru

Искал, как бы изменить порядок сортировки стандартных моделей Django. В
моем случае, нужно чтобы пользователи сортировались по имени, а не по id, как
это происходит по умолчанию.

И вот, нашел блог где описан [такой хак][1]:

    :::python
    from django.contrib.auth.models import User
    User._meta.ordering = ['username']

Странно, но больше ничего внятного про эту проблему я не нашукал и не
нагуглил.

[1]: http://www.djangofoo.com/269/change-django-auth-group-ordering
