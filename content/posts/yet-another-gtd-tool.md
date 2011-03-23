Title: Yet another GTD tool
Slug: yet-another-gtd-tool
Date: 2009-02-15 23:36
Tags: gtd, tools, python
Category: texts
Lang: en
Description: A description of my new Getting Things Done tool, based on "tagging workflow".

I was very busy last month because of a deadline of [my current project](http://42.yandex.ru). And [getting things done][gtd] method was especially useful for me these days.

During last two or three weeks, I tried almost all time management programs for Mac OS X, but have not found any convinient. All of them are overloaded with uneeded features, their interfaces are cluttered with tags, projects, areas and etc..

So, I decided to write [my own GTD tool][gtdzen], simple, flexible and convinient. I wrote it in one holiday using python and sqlalchemy. It's name is GTDZen.

GTDZen operates with two item types: Task and Tag. Any Task have title, priority and tags. You can get Tasks by tags, using simple AND-NOT logic. For example, you can show all tasks, related to "work" but not to "today".

Now GTDzen exists as a python module, which is the middleware between user interface and database. Also, it includes a command line interface. I think that this is enough, but you easily could write you own GUI interface for Windows or Mac OS X.

You can find a short tutorial in the README file, on the [project's page at GitHub][gtdzen].

Code is licensed under the New BSD License, so feel free [to fork][gtdzen] it and use it. But I would be very appreciated if you send me some patches.

[gtdzen]: https://github.com/svetlyak40wt/gtdzen/
[gtd]: http://en.wikipedia.org/wiki/Getting_Things_Done
