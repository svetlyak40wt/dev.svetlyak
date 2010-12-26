Title: Automated ChangeLog generation for GIT, SVN and CVS
Slug: automated-changelog-generation-for-git
Date: 2008-10-22 06:15
Tags: tools,git,cvs,svn
Category: texts
Lang: en
Description: Tired to write ChangeLog? Use right tools and your hair become smooth and silky.

Today I decided to generate a ChangeLog for one of my projects. And I started to search a solution to automate this process. I used a [cvs2cl][1] script before, and it was not surprise for my, that similar tools for git are available too.

After few minutes of googling around, I have found gitlog-to-changelog tool in the gnulib package. Here the link to [pull gitlog-to-changelog from gnulib's][2] repository.

Just download this and place somewhere in you PATH. And don't forget to make this perl script executable. Also, you need a recent version of the git. I found, that any version above 1.5.3 will be OK.

Also, you may be interested in similar tool for SVN. It's name is [svn2log][3].

   [1]: http://www.red-bean.com/cvs2cl/
   [2]: http://git.savannah.gnu.org/gitweb/?p=gnulib.git;a=blob_plain;f=build-aux/gitlog-to-changelog;hb=HEAD
   [3]: http://www.core.com.pl/svn2log/