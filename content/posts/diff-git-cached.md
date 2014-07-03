Title: Diff Git Cached в Vim
Slug: diff-git-cached
Date: 2011-01-09 14:04
Category: texts
Tags: vim, git
Lang: ru

Оказывается в Vim есть полезная штука для просмотре диффа при редактировании commit message git. Она появилась, начиная с версии 7.2. Называется эта команда :DiffGitCached.

Дифф можно вызывать вручную, а можно прописать в конфиг такую строчку:

    autocmd FileType gitcommit DiffGitCached | wincmd p

И тогда дифф будет открываться автоматически после запуска `git commit`.

Этот хинт я почерпнул из книги [Vim Recipes](https://github.com/runpaint/vim-recipes/blob/master/text/11_extending/05_integrating_vim_with_git.html).
