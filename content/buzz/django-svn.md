Title: Скрипт для сборки Django из SVN
Slug: django-svn
Date: 2010-12-04 17:13
Category: texts
Tags: tools, django
Lang: ru

Скрипт для сборки Django из SVN.

Есть у меня [небольшой скриптик][1], который я использую чтобы собирать пакетик с
джангой. Свои пару сайтиков я деплою с помощью рецепта djangorecipe и
zc.buildout.

Но djangorecipe каждый раз лазит в SVN проверяя, не изменилось ли чего, даже в
том случае, если задана конкретная ревизия. А вот пакет он ставит быстро, к
тому же, в качестве бонуса, каждая инсталляция испольует один и тот же код из
кэша buildout, если версии Django на сайтах совпадают.

[1]: https://gist.github.com/728329
