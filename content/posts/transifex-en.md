Title: OpenSource Translations
Slug: transifex
Date: 2011-01-27 14:55
Category: reviews
Tags: web, tools
Lang: en

About a week ago, I saw an announce at the [django-developers][group] mail list. It was about the Django translation process, which is moved to online translation service [Transifex][].

Transifex provides an interface to work on translations. Here is the process:

* You have to sign in.
* Then to add a project.
* Upload existing translations. Usually it is a gettext "po" files.

Then you need to gather some translators around the project. They must be organized into the language teams.

When translation is ready, you are able to download the "po" files.

For experiment, I added one of my tiny projects [django-faces][] to the service. If you know language other than Russian or English, try to translate it. There is a little amount of text.

By the way, I found the there are about 600 projects at the Transifex, but only half have some translation resources. It means that these developers start to play with the interface, but something prevents them from finishing the process. And interface is really obscure. For example, I do not understand how to search some project to translate it into Russian.

[group]: http://groups.google.com/group/django-developers
[Transifex]: http://www.transifex.net
[django-faces]: http://www.transifex.net/projects/p/django-faces/

