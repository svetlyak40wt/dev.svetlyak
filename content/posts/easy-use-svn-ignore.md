Title: Easy to use SVN ignore
Slug: easy-use-svn-ignore
Date: 2009-01-23 15:51
Tags: svn, tools, tips
Category: texts
Lang: en
Description: A short but helpful function to change svn:ignore propery on the current directory.

I'm hate routine task. That's why I wrote a simple function to change svn:ignore propery on the current directory.

Add these lines in you .bashrc

    :::bash
    function ignore()
    {
        SVNIGNORE=/tmp/.svnignore
        svn propget svn:ignore . > "$SVNIGNORE"
        while [ -n "$1" ]; do
            echo "$1" >> "$SVNIGNORE"
            shift
        done
        svn propset svn:ignore --file "$SVNIGNORE" .
        rm "$SVNIGNORE"
    }

Here is an example, how to use this script. Let's suppose, that you are in your working directory, and want to hide from SVN a 'packages' subdirectory and all files with .o suffix. Then you should run:

    :::bash
    ignore packages '*.o'

Please, pay attention to the single quotes around '*.o', if you omit them, than shell will expand this pattern and only those files which exists on the disk will be added to the svn:ignore propery.