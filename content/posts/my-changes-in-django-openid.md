Title: My changes in the django-openid
Slug: my-changes-in-django-openid
Date: 2008-11-05 07:43
Tags: django, openid
Category: texts
Lang: en
Description: Little post about my changes in the Simon Willisons's django-openid. My URLConf generators enables normal usage of a 'reverse' and {% url %}, also, unittest were refactored.

I am going to move from the blogspot to [my own blog engine][1], written in django. The main blocker right now is an OpenID authentication. I am decided to use a Simon Willison's django-openid, but it is still under the heavy development.

Here is [my fork of the django-openid][2] with few bugfixes and changes.

The most sugnificant change, on my taste, is a normal URLConf generator which I wrote for consumers. It allows you do not hardcode urls for openid login, registration and so on, but use reverse matching using "reverse" function or template tag {% url %}.

Also, I rewrote all unittest, and now they use a "reverse" function and a normal django.test.Client to talk to the clients. I think, that it is better solution, than to generate a mock WSCGI request and then pass it directly to the consumer's method.

By the way, my URLConf generator can be used to generate URL patterns for any object, which exposes "do_something" methods. For each of these methods, generator creates an URL pattern "^something/" and binds it to the object's method. "do_index" is binded to the "^$" pattern, however.

Second useful change, which I made in the django-openid is a AutoRegistration consumer, which automatically creates auth.User on login by open id. It trying to figure out some information about user requesting optional SREG data from the OpenID provider.

And finally, the dessert! I add an advanced login form, which uses newforms' MultiWidget and allow user do not guess, what does the "OpenID" mean, but just choose one of the popular services, where he has an account, from the select box and input his name on this service. I belive, that this is the most right way from the usability's view point.

I am hope, that Simon Willison will accept these changes to the django-openid's trunk somewhere, but now I am going to synchronize our repositories by hand. Stay tuned and look on [my branch][3] on the github.

   [1]: http://github.com/svetlyak40wt/django-dzenlog/
   [2]: http://github.com/svetlyak40wt/django-openid/tree/svetlyak40wt
   [3]: http://github.com/svetlyak40wt/django-openid/tree/svetlyak40wt/