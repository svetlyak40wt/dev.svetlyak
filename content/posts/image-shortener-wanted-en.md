Title: Image Shortener Wanted!
Slug: image-shortener-wanted
Date: 2010-12-28 01:05
Tags: ideas
Category: texts
Lang: en

I have an idea of a new service. I call it "The Image Shortener".

Sometimes, I found an image on the internet, licensed under the Creative Commons and just insert
it into the blog post. But to get nice result, image have to be resized according to a blog
column width.

I'm wondering if there is already such service exists which is acts like a resizing proxy server and
url shortener simultaneously?

For example, if I found this image <http://farm5.static.flickr.com/4005/4203341399_c1c99027e5_o.jpg> and
want to insert in into my blog post, but it should be resized to have no more 600 pixels width:

1. I go to the shortener and enter the URL (ideally, I even don't have to enter the image's URL
   (it is should work with flickr's pages too).
2. Shortener remember the URL and give me the shortened `http://blah.img/3bfg`, which, by default,
   redirects to the original image.
3. Then I insert this URL into the blog post but supply additional parameter: `http://blah.img/3bfg?width=600`.
4. When this image will be requested, shortener will have to fetch the original, resize it, save somewhere
   in the cloud and redirect to this new image.
5. And finally, I get the profit from this automatization.

What do you think about this idea? Is it a bicycle and already implemented somewhere?
