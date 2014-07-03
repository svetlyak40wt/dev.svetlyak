Title: Diff Git Cached in Vim
Slug: diff-git-cached
Date: 2011-01-09 14:14
Category: texts
Tags: vim, git
Lang: en

Surprisingly, there is a useful command in Vim for editing git commit messages. It was shipped with Vim starting from version 7.2. It's name is :DiffGitCahced.

Diff could be showed manually, but also, you could write this line in the config:

    autocmd FileType gitcommit DiffGitCached | wincmd p

And then diff will be opened automatically after the `git commit`.

This tip was found in the [Vim Recipes](https://github.com/runpaint/vim-recipes/blob/master/text/11_extending/05_integrating_vim_with_git.html) ebook.
