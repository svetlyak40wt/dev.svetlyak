Title: Git related cheat and sheet
Slug: git-related-cheat-and-sheet
Date: 2008-09-26 05:06
Tags: git, tips
Category: texts
Lang: en
Description: 

I have found yesterday a two articles about a GIT. 

The cheat is a post by [Ryan Tomayko][1], where Ryan shows how to deal with «[The Tangled Working Copy Problem][2]». First, he explain, how to make separate commits with SVN, using `patch` command. Next, Ryan give an example of `git-add --patch` usage, to solve this problem in more elegant manner. 

And finally, I found an excellent [GIT cheat sheet][3] at [http://cheat.errtheblog.com][4]. There are many useful GIT commands are explained in this sheet, so I won't list them all, but only mention most interesting for me. 

One of the interesting abilities, explained in this sheet is 'colors' and 'aliases'. Do you know, that it is possible to colorize git's output and to use shortcuts in the command line? 

For example, you can add these lines in your ~/.gitconfig 
    
    [alias]
        st = status
        ci = commit
        br = branch
        co = checkout
        df = diff
        lg = log -p
    

And use `git st` instead of `git-status` or `git status`. 

Also, sometimes `git commit --amend` can be useful, to adjust latest commit and add a new files to it or change comment. 

That's all for now. Don't forget to [subscribe to RSS][5] to receive latest updates! 

   [1]: http://tomayko.com/about
   [2]: http://tomayko.com/writings/the-thing-about-git
   [3]: http://cheat.errtheblog.com/s/git
   [4]: http://cheat.errtheblog.com
   [5]: http://feeds.feedburner.com/LazyCrazyCoder