Title: How to merge two GIT repositories
Slug: how-to-merge-two-git-repositories
Date: 2008-10-02 04:52
Tags: git,my-projects,vcs
Category: texts
Lang: en
Description: 

I have a project on GitHub. It's name is [django-vcs-watch][1]. Also, I had a test django project in separate directory. This test project was a separate git repository, but today I decided to made it a part of [django-vcs-watch] and include as example project to the main repository at GitHub. 

So, I started to search how to merge two git repositories together. And furtunately, I have found [the solution][2]. See the comments for this post, where Tobu suggests to use `git filter-branch` and pulling to get two repositories together. 

First, full `vcs_test` projects content was moved to a new subdirectory `example`, using this command: 

    :::bash
    git filter-branch --index-filter 'git ls-files -s | sed "s-\t-&example/-" |
    GIT_INDEX_FILE=$GIT_INDEX_FILE.new \
    git update-index --index-info &&
    mv $GIT_INDEX_FILE.new $GIT_INDEX_FILE' HEAD
    

Next, I'm went to the `django-vcs-watch` directory, and just make a `pull`: 

    :::bash
    git pull ../vcs_watch/
    

That's it! Just one `git push`, and all changes will go to the GitHub. Hey! They are [already there][1]! 

Note, that [git-filter-branch][3] has other interesting applications. For example, you can split you repository, or remove some unwanted commits. Anyway, this command is very dangerous, don't try to repeat these experiments at home, or at least, have a backup :-) 

   [1]: http://github.com/svetlyak40wt/django-vcs-watch/tree/master
   [2]: http://log.emmanuelebassi.net/archives/2007/09/when-the-levee-breaks/
   [3]: http://www.kernel.org/pub/software/scm/git/docs/git-filter-branch.html