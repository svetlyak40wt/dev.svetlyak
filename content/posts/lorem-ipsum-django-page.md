Title: Lorem ipsum django page
Slug: lorem-ipsum-django-page
Date: 2008-12-05 09:37
Tags: webdev, django
Category: texts
Lang: en
Description: This post shows how to build a useful lorem ipsum page in few minutes!

If you are a web designer, then sometimes you need to fill a web page with some fake text. In graphics and web design, [lorem ipsum][wiki] became a standart placeholder. This mean, that you need to have a handy source of this meaningless information :-)

Surely, you can use [someone's][lorem] lorem ipsum page, but I want to show how you can build your own in few minutes with django's generic view and simple template.

First of all, add this line to your urlpatterns:

    :::python
    (r'^lorem/$', 'django.views.generic.simple.direct_to_template', {'template': 'lorem.html'}),

Next, create template like this:

    :::django
    {% extends 'base.html' %}
    {% load webdesign %}

    {% block title %}{% block heading %}Lorem ipsum{% endblock %} — {{ block.super }}{% endblock %}

    {% block content %}
        {% lorem 5 p %}
    {% endblock %}

As you can see, django doing all dirty work for us. We just load template [tags for webdesign][doc] and then use tag `lorem` as text generator.

It need to say, that if you have enabled [django-dbtemplates][] and [flatpages][], then you even don't need to modify the settings.py file or edit any local templates. In that case for can just add a flatpage with nondefault template.

Don't be slow, build your own lorem page right now! I already have [one][mine], and you?

[wiki]: http://en.wikipedia.org/wiki/Lorem_ipsum
[lorem]: http://www.lipsum.com/
[doc]: http://docs.djangoproject.com/en/dev/ref/contrib/webdesign/
[django-dbtemplates]: http://github.com/jezdez/django-dbtemplates/
[flatpages]: http://docs.djangoproject.com/en/dev/ref/contrib/flatpages/
[mine]: /lorem/