Title: CouchDB bulk insert's performance
Slug: couchdb-bulk-inserts-performance
Date: 2008-11-19 03:24
Tags: couchdb, database, scalability
Category: texts
Lang: en
Description: Small test for CouchDB's performance on bulk inserts.

Few days ago, I found a two articles by [Damien Katz][katz] and [Jan Lehnardt][jan] about [CouchDB's][couchdb] scalability and I decided to write my own test.

My test is very similar to Jan's, but written in python. It uses almost the same datastructure,but the main purpose of my test — to check [CouchDB's][couchdb] scalability on large about of data.

I measure an RPS — records per second. Actually, I've made three test.

Threads
=====

First one — to check how performance depends on number of simultaneous connections. Here, I insert 100 records at once up to 100000. Thread count vary from 2 to 16. Here is a result from this test. This chart show, how depends RPS from database's size and thread count:

<inline type="media.photo" id="3" class="center" />

As you can see, values almost the same for all parameters. Obviously, something wriong with my test setup.

Bulk size
======

Next, I tried to see, how RPS depends on bulk size. On the next chart you can see how CouchDB operates on bulk sizes from 10 to 10000:

<inline type="media.photo" id="2" class="center" />

The best performance have bulk inserts which save 10000 records at once. And on large size of the database, RPS aspire to level which depends on bulk size. As you can see, bulk size 10000 gives best performance. It's about 1250 rows per second on database with 100000 documents.

Database size
=========

My final test is more like stress test than performance, because I tried to create large database with 4 million documents and see how RPS depends on database's size. Here is the picture:

<inline type="media.photo" id="4" class="center" />

The final database's size is 9.5G. And CouchDB had crashed few times when database's size reach boundary at 5.6G. I don't know the reason of these crashes, but I have a `erl_crash.dump` and couchdb.log with errors.

We need to admit, that CouchDB works quite unstable after 2.5 millions records in the database. Pay attention to these red spikes on the chart. It seems, that this is the real limit on data size. 

I worse to say, that all these tests were running on my laptop with 1G of RAM and Intel Centrino Duo on board. I looked at dstat and top during the tests, and notice that first two are more likely CPU bound and last one — IO bound because lack of memory.

Anyway, here is [the source code of my test][test-code]. You can run it on you own hardware and share the results with community. Even more, you can improve the test and add, for example test for selects or something like that. I thought, that it would be very interesting to see on data retrival's speed to.

[katz]: http://damienkatz.net/2007/12/couchdb_perform_1.html
[jan]: http://userprimary.net/user/2007/12/16/a-quick-look-at-couchdb-performance/
[couchdb]: http://couchdb.org/
[test-code]: http://github.com/svetlyak40wt/couchdb-performance-tests/