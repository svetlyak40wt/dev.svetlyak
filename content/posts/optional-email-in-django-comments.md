Title: How to make email field optional in django.contrib.comments
Slug: optional-email-in-django-comments
Date: 2009-06-02 02:57
Tags: django, tips, snippet, python
Category: texts
Lang: en
Description: Short code snippet which show simple way to make email field optional.

Today I solved a little problem on my personal blog http://svetlyak.ru. I'm using the django.contrib.comments there, and some my readers encounter a problem. They are registered using OpenID, but don't have a email in their accounts, because OpenID provider does not share that information.

So, when such users tried to post a comment on my blog, they are shown a page with error, because email is required field.

I found a simple way to make an email field optional. All what you need is to add additional app in the INSTALLED_APPS, and COMMENTS_APP variable. In my case it's looks like that:

    :::python
    INSTALLED_APPS = (
        'django.contrib.sessions',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sites',
        'django.contrib.admin',
        'django.contrib.markup',
        'django.contrib.sitemaps',
        'django.contrib.humanize',
        'django.contrib.comments',
        'django_faces',
        'django_openid',
        'blog',
        'gallery',
        'tagging',
        'firefly.utils',
        'firefly.my_comments',
    )
    COMMENTS_APP = 'firefly.my_comments'

Next, in file my_comments.py:

    :::python
    from django import forms
    from django.utils.translation import ugettext_lazy as _
    from django.contrib.comments.forms import CommentDetailsForm

    class CommentForm(CommentDetailsForm):
        email = forms.EmailField(label=_("Email address"), required=False)

    def get_form():
        return CommentForm

That's it! By the way, you can change other behaviour too. Just look at the sources of `django/contrib/comments/__init__.py` file.