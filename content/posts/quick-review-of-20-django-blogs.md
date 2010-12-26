Title: Quick review of 20 Django blogs.
Slug: quick-review-of-20-django-blogs
Date: 2008-09-27 04:04
Tags: blog,django,reusable,python,review
Category: texts
Lang: en
Description: 

I wrote my own blog engine in Django. How about you? There are many opensource django application which implement different features. For example, my own blog engine "[firefly][1]" (which is used at [http://svetlyak.ru][2]) has support for text post and also it has builtin photo blog with separate feed, urls and tagging. Also, it includes meny other features, but I don't think, that all these features will be useful even for 10% of readers. 

Today, I decide to look at existing opensource django blogs with hope to find a universal solution, simple but flexible enough to build a blog with any kind of the media. I need a reusable django application to build a blog with support for posts with links, text, images, whatever. 

So, lets look, what you can find at [http://code.google.com/hosting/][3] and [http://github.com][4] using keywords "django blog": 

  * [banjo][5] -- very complex "all-in-one" solution, with many models and custom plugins. This is absolutelly not "Django Way". 
  * [becca][6] -- minimalistic blog application. There is only two models -- for post and for tags. Pretty code, but to be updated to work with django 1.0. 
  * [blogango][7] -- relatively simple design, but with custom tags and comments. 
  * [blogmaker][8] -- has more or less complex design with built-in trackback and tags support. 
  * [coltrane-blog][9] -- simple blog by James Bennett with two separate models for posts and links. Uses custom categorization and django-tagging. 
  * [django-basic-blog][10] -- really simple blog application, some where similar to coltrane -- basic-blog also uses separate categories and django-tagging. 
  * [django_blog][11] -- very, very, very minimalistic blog application. 
  * [django-blog-entries][12] -- interesting models design. This blog uses `comment_utils` for moderation. 
  * [django-diario][13] -- also has very interesting models.py. I've learn some new things about usage of django's fields. This blogging application has relatively simple and has _optional_ support for django-tagging. Also, django-diario has _multi-site support_ and one post can be published on different sites. I don't like it complexity in multi-site part, but other ideas are look good. 
  * [django-ink][14] -- very simple and clean models. Nothing exeptional, just easy to use blog application. 
  * [django-yab][15] -- yab is nothing but yet another django blog. However, it has support for multiple blogs, which may be interesting to somebody, not for me, certanly. 
  * [flother][16] -- besides a simple and straigt blog application, "flother" includes a photo gallery application. In that way, "flother" very similar to my "firefly" engine, which also includes a blog for text and a separate photoblog. 
  * [lifeflow][17] -- another "all-in-one" solution. Complex, with custom comments, categories, tags, translation support, uploads and other strange post's grouping tools. LifeFlow is huge and ugly for my taste. 
  * [n00bish-django-blog][18] -- really noobish app, very simple and useless :-) 
  * [oebfare][19] -- simple blog, which includes few application to publish posts and links. Nothing interesting. 
  * [shiftingbits][20] -- based on the "oebfare", straightforward blog, with additional support for import from Wordpress, `metaWeblog API`, `Akismet`, `django.contrib.comments` and `comment_utils.moderation`. 
  * [zangetsu][21] -- pretty simple blog application with custom tags and example of TinyMCE, embedded into a django admin. Also, it has import from the wordpress and from a plain rss feed. 
  * [zsite][22] -- the most minimalistic blog. It has just a settings.py, manage.py and urls.py. Zsite includes basic.blog and basic.inlines from a [django-basic-apps][23]. 
  * [byteflow][24] -- is a very complex, full-fleged blog engine, based on separate applications. I don't need all this stuff, but sometimes it is very interesting to look "under the hood" of the byteflow and discover something interesting. 
  * [firefly][1] -- my own blog. Complex and with tight coupling between application. I want to separate them from each other, but sometimes it is to difficult. Has support for multiple languages, pingbacks, tagging (with modified multilingual django-tagging application), akismet moderation, photo blogging, pinging of blog search engines and etc.. 

As you can see, there are many solutions, but I am not found any application which comply with my requirements. So, I need to continue my investigations of the Django world… 

   [1]: http://svetlyak.ru/blog/about-design-and-move-to-git/
   [2]: http://svetlyak.ru
   [3]: http://code.google.com/hosting/
   [4]: http://github.com
   [5]: http://coderseye.com/2007/banjo-blog-nearing-01-release.html
   [6]: http://github.com/douglasjarquin/becca/tree
   [7]: http://code.google.com/p/blogango/
   [8]: http://code.google.com/p/blogmaker/
   [9]: http://code.google.com/p/coltrane-blog/
   [10]: http://code.google.com/p/django-basic-blog/
   [11]: http://github.com/vbabiy/django_blog/tree
   [12]: http://github.com/nshah/django-blog-entries/tree
   [13]: http://code.google.com/p/django-diario/
   [14]: http://www.bitbucket.org/jparise/django-ink/wiki/Home
   [15]: http://github.com/gregnewman/django-yab/tree
   [16]: http://code.google.com/p/flother/
   [17]: http://github.com/lethain/lifeflow/tree
   [18]: http://github.com/malini/n00bish-django-blog/tree
   [19]: http://github.com/brosner/oebfare/tree
   [20]: http://github.com/paltman/shiftingbits/tree
   [21]: http://svn.pardus.org.tr/projeler/zangetsu/
   [22]: http://github.com/buckyball/zsite/tree
   [23]: http://code.google.com/p/django-basic-apps/
   [24]: http://trac.piranha.org.ua/