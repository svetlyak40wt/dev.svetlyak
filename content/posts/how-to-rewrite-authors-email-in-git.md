Title: How to rewrite author's email in GIT
Slug: how-to-rewrite-authors-email-in-git
Date: 2008-10-27 01:59
Tags: git,tips
Category: texts
Lang: en
Description: Do you have a trouble with the history? Just rewrite it!

Today I want to show you, how to rewrite GIT's history and change the author's email using `git-filter-branch` command.

Suppose, that you forget to setup you GIT config correctly, and all commits from you have wrong email. For example, all commits are made by Vasya Pupkin . Of cause, you want to correct this information, and `git-filter-branch` will help you.

Here is a simple call for `git-filter-branch`:

    :::bash
    git-filter-branch \
    --env-filter 'export GIT_AUTHOR_EMAIL="vasya@gmail.com"'
    

This command will rewrite all commits' information and change email to vasya@gmail.com. If you want, more smart behaviour can be added using shell statements like `if`.

Thats it. And don't forget to make a backup before you'll try to rewrite The History! :-)