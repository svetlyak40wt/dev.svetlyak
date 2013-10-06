Title: Periodical Tasks For Things
Slug: things
Date: 2012-04-11 15:19
Category: texts
Tags: python
Lang: en

Few days ago, I read a funny document "[GTD for hackers][GTD]" and found an interesting ideas there.
One of them is to create the checklists for routines.

I already use [Things][] by Cultured Code, to track my todos. However there is no such feature as periodical tasks. They should behave like periodical events in the calendar — you add it once, specifying a time interval, and task should appear in the list automatically. Things is lack this feature.

But we have this wonderful Apple Script, and it allow to do almost anything!

I spent about hour to generate a 10 lines script. It adds a task to the Things right from the command line. The last part was pretty easy — to run a crontab and to add a one line for each periodical task I want to appear in my checklist.

Finally, I've got a very flexible system, which solves my problem and does not require any additional software.

[Sources are available][github] at the GitHub. Fork and edit.

[Things]: http://culturedcode.com/things/
[GTD]: http://gtdfh.branchable.com/
[github]: https://github.com/svetlyak40wt/things-periodical-tasks


