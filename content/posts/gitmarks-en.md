Title: Social bookmarks at the GitHub
Slug: gitmarks
Date: 2011-01-13 11:17
Category: review
Tags: python, git
Lang: en

Today I want to tell you about quite interesting project from the GitHub. It
is developed by Hilary Mason and called [gitmarks][].

This project allows to save URLs and share them with other GitHub users. For
each bookmark, script downloads page's content. Also, you could specify the
tags and description of the link. All data are saved to the git repository and
commited, and of cause you is able to use `git grep` to search over all saved
bookmarks. URLs could be added from the command line or using a bookmarklet,
but in the latter case your have to start a local web server.

![][image]  
Image by [Ei! Kumpel](http://www.flickr.com/photos/eikumpel/2201268993/).


However, this project have a few shortcomings.

First, the code looks ugly because Hilary ignores [naming conventions][pep-8], accepted
by Python community.

Secondly, existing documentation says nothing were to store bookmarks. Because of that,
many people start to fork the repository and to save bookmarks in it. Look at
the [network graph][graph], it is quite cluttered with bookmark commits and it
is very hard to find code changes in this heap.

It worse to enforce code and content separation, to make script development
easier.

And finally, there are batch of small things which are inconvenient. For
example, people could comment bookmarks of each other, using the GitHub's
commit comments. However, right now commit page looks very scary because
it include a full HTML downloaded from the bookmarked URL. To avoid this
HTML have to be converted into the readable text.

I hope, this project will evolve to the usable distributed bookmarks service.

[gitmarks]: https://github.com/hmason/gitmarks/
[graph]: https://github.com/hmason/gitmarks/network
[pep-8]: http://www.python.org/dev/peps/pep-0008/
[image]: http://farm3.static.flickr.com/2262/2201268993_a560441f47.jpg
[image-url]: http://www.flickr.com/photos/eikumpel/2201268993/
