Title: Command Line for the Internet
Slug: facebook-bunny1
Date: 2011-01-20 11:11
Category: reviews
Tags: python
Lang: en

Do you use search shortcuts, allowing to enter a query directly into the browser's address bar? If yes, then you will certainly be interested to know that you can not only to connect existing search engines to your browser, but also to write a more sophisticated query processor directly in Python.

Yesterday, I found an interesting project on the GitHub. It was developed in the Facebook. The project's name is [Bunny1][].

![][Resized]  
by [serenionion@flickr](http://www.flickr.com/photos/opid/256250194/)

Bunny1, is a web server, which receives a command and a query, and then either redirects somewhere else, or shows a HTML page with the result. If you'll plug the URL of the server as the default search engine, you'll get the powerful command line directly in the browser. And the most useful here is that:

* it will work in all modern browsers;
* commands can be added by yourself and written in the Python.

For example, you can write a handler that by the request `tw Good morning, Moscow!` will tweet from your name and redirect to the tweet's page.

Sake of justice, it should be noted that the idea is not new. There is, a service [YubNub][], which implements similar functionality and a Firefox plug-in [Ubiquity][]. But the former contains a lot of unnecessary commands and can't be extended, and the latter is suitable only for Firefox users.

[YubNub]: http://yubnub.org/
[Bunny1]: https://github.com/facebook/bunny1/
[Ubiquity]: https://mozillalabs.com/ubiquity/
[Image]: http://farm1.static.flickr.com/120/256250194_ac05247901_o.jpg
[Resized]: http://resizer.co/?image=http%3A%2F%2Ffarm1.static.flickr.com%2F120%2F256250194_ac05247901_o.jpg&w=600

