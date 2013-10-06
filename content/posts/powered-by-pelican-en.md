Title: Powered by Pelican
Slug: powered-by-pelican
Date: 2010-12-25 23:06
Lang: en
Category: texts
Tags: life, python

After a few days of work, I rewrote my blog to static blog generator [Pelican][]. Moreover, I transfered not only one blog but two: my english blog <http://aartemenko.com> and my Google Buzz where I tried to write about software development in russian.

I decided to drop <http://aartemenko.com> and move this blog to static to reduce a memory usage on my VPS. Google Buzz turned out useless for short programmer's notes, because it even not support a simple HTML tags nor syntax highlight for code snippets.

As the result, I took a new static blog generator [Pelican][], forked it on the GitHub and patched. Some bugs were fixed and some functionality was added. For example, now it could handle article translation into different languages and separate Atom feeds are available for all translations. About two days I spent, developing my own scheme for the Pelican.

Now I able to edit blog posts in my favorite editor Vim, grep them and do other things, you want usually do with texts. For now, Pelican supports only Markdown and ReST markups, but that is enough for most cases. The other features which I need to implement, are Vim helper to deploy articles to the server and ping the FeedBurner.

By the way, I published [the sources, of this blog][blog] at the GitHub as an example of the modified Pelican usage.

[Pelican]: https://github.com/svetlyak40wt/pelican
[blog]: https://github.com/svetlyak40wt/dev.svetlyak
