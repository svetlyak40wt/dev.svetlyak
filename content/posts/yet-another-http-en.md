Title: Yet Another HTTP Lib
Slug: yet-another-http
Date: 2011-02-16 11:11
Category: reviews
Tags: python
Lang: en

Sometimes I see interesting links in the Twitter. For example, Yury Yurevich retwitted few PyPi updates yesterday. One of them is a new [HTTP library][requests]. This is just a wrapper around urllib and urllib2, to make the life easier. But this bicycle design could be improved.

For example, to use HTTP basic auth, author suggest to create an Auth object and then use it in every call:

    :::python
    conv_auth = requests.AuthObject('requeststest', 'requeststest')
    r = requests.get('https://convore.com/api/account/verify.json', auth=conv_auth)

Why? This object just stores a username and a password, why not to use a tuple instead? If you strive for simplicity, why not to go to the end?

And there are some comments, related to the code. It is incompatible with python2.5 because author forgot about `from __future__ import absolute_import` and uses new style try except blocks. The main method, sending request, is overcomplicated and contains few huge ifelse blocks. Also, he is trying to do some monkeypatching if there are 'eventlet' or 'gevent' modules. But which side-effects I should be aware of if one of these libraries is installed in the system, but I don't mind to use it?

[requests]: http://pypi.python.org/pypi/requests/
