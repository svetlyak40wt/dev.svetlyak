Title: GitHub user's stats
Slug: github-users-stats
Date: 2009-04-17 17:43
Tags: git, python
Category: texts
Lang: en
Description: A short overview of my python script to retrive GitHup user's stats.

Today I wrote a simple python script, which uses [GitHub's API][github-api], to retrive information about user's projects and their watchers/forkers count.

The script is pretty simple and uses lxml to get and parse XML page:

    :::python
    #!/usr/bin/env python
    import sys
    from lxml import etree as ET

    username = 'svetlyak40wt'

    if len(sys.argv) == 2:
        username = sys.argv[1]

    url = 'http://github.com/api/v1/xml/%s' % username
    data = ET.parse(url)
    reps = data.findall('repositories/repository')

    if reps:
        tmpl = '%25s, %8s, %5s'
        print tmpl % ('NAME', 'WATCHERS', 'FORKS')
        for rep in reps:
            print tmpl % (
                rep.find('name').text,
                rep.find('watchers').text,
                rep.find('forks').text,
            )
    else:
        print 'User %s has no repositories.' % username

Feel free to fork [this Gist][gist-reps] and modify it.

By the way, after work was done, I've found that Gabriel Horner already done same task few weeks ago, but he implemented it as [a bookmarklet][bookmarklet].

Using these tools, I found, the top 5 of my most popular apps:

* [django-tagging-ng](http://github.com/svetlyak40wt/django-tagging-ng/) — 30 watchers and 1 fork
* [django-perfect404](http://github.com/svetlyak40wt/django-perfect404/) — 12 watchers
* [django-faces](http://github.com/svetlyak40wt/django-faces/) — 9 watchers
* [django-pingback](http://github.com/svetlyak40wt/django-pingback/) — 9 watchers and 1 fork
* [gtdzen](http://github.com/svetlyak40wt/gtdzen/) — 7 watchers and 1 fork

Not bad! :-)

[github-api]: http://github.com/guides/the-github-api
[gist-reps]: http://gist.github.com/96909
[bookmarklet]: http://tagaholic.me/2009/04/06/github-bookmarklet-for-user-pages.html