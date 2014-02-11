Title: Right way to manage dotfiles.
Slug: dotfiler
Date: 2014-02-11 18:00
Category: texts
Tags: tools
Lang: en

Few weeks ago, I mentioned in my twitter [@svetlyak40wt](https://twitter.com/svetlyak40wt) about a new solution I started to write in python. I intended to write a better and simpler dotfiles manager which will be smart enough to allow me to store different parts of dofiles separately. Now this project is useful and you can try it. It's name is [dotfiler][]. Or just `dot`.

You may ask, why do you need this when there is wonderful [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh/) and [cool collection of configs](http://dotfiles.github.io/) from various famous guys? I'll tell you. None of these "solutions" allow me to configure different machines in different ways. I mean really different. I can't just clone same repository to all of them, because there is some private configs, and they are different on my daily job and home.

As I said, I have three kinds of configs:

* First — are usual configs which could be shared on the GitHub. Various useful tricks for zsh, emacs, tmux, etc..
* Second — are private configs which should be kept in secret. Here you would find different tokens to Amazon's cloud if I share it (but I'll not ;-)). These better to keep at your own server.
* Third kind — work configs. They are just like the private with two differences — I don't want them on my own servers, but I could share them with my colleagues on out GitHub Enterprise server.

I found no solution which allows easily separate these different kinds of dotfiles. That is why [dotfiler][] was created.

The main idea was stolen from [Zach Holman](http://zachholman.com/2010/08/dotfiles-are-meant-to-be-forked/) — broke everything into specific and distinct areas: [editor](https://github.com/svetlyak40wt/dot-emacs), [python IDE](https://github.com/svetlyak40wt/dot-python-dev), etc... And dotfiler completely follows this concept allowing separate not only zsh configs, but any other too. It allows not only to group them, but also to keep them in separate git repositories. A directory with dotfiles, grouped by some area is called "environment" or, for brevity, just "env".

The most amazing is how dotfiler handles symlinks! Because it allows different environment to have dotfiles to be symlinked into the same directory, it needs to handle situations where these files appears or disappears during moving environments around. It is hard to understand without a graphical representation, so I drawn some images for you. Here is structure of the `.dotfiles` directory on the left, and `dot update` command's result on the right. Arrows show where each file symlinked (if there is no arrow, then it is a directory or a bug in the picture :)). Moreover, I'll give you commands to reproduce these steps, to make it's like a dotfiler tutorial. The commands will have an option `--home-dir`, which is optional and need as only to keep dotfiler away from your real $HOME directory while you are playing with it. During real usage you don't need `--home-dir` option.

Let's begin:

    :::bash
    $ git clone https://github.com/svetlyak40wt/dotfiler .test-dotfiles
    $ export PATH=~/.test-dotfiles/bin:$PATH
    $ dot add https://github.com/svetlyak40wt/dot-zsh
    $ mkdir test-home
    $ dot update --home-dir=`pwd`/test-home
    LINK   Symlink from /Users/art/test-home/.bash_profile to /Users/art/.dotfiles/zsh/.bash_profile was created
    LINK   Symlink from /Users/art/test-home/.zsh to /Users/art/.dotfiles/zsh/.zsh was created
    LINK   Symlink from /Users/art/test-home/.zshrc to /Users/art/.dotfiles/zsh/.zshrc was created

![](http://img-fotki.yandex.ru/get/9895/13558447.f/0_aa14f_4f5befb1_L.jpg)

This picture shows that we've cloned an environments with some configs for zsh. There is a number of configs, but dotfiler just symlinked a directory `.zsh` for simplicity.

    :::bash
    $ dot add svetlyak40wt/dot-tmux
    $ dot update --home-dir=`pwd`/test-home                                                                                 b:master s:
    LINK  Symlink from /Users/art/test-home/.bin to /Users/art/.dotfiles/tmux/.bin was created
    LINK  Symlink from /Users/art/test-home/.tmux.conf to /Users/art/.dotfiles/tmux/.tmux.conf was created
    RM    Symlink /Users/art/test-home/.zsh was removed.
    MKDIR Directory /Users/art/test-home/.zsh was created.
    LINK  Symlink from /Users/art/test-home/.zsh/00-options to /Users/art/.dotfiles/zsh/.zsh/00-options was created
    LINK  Symlink from /Users/art/test-home/.zsh/01-prompt-functions to /Users/art/.dotfiles/zsh/.zsh/01-prompt-functions was created
    LINK  Symlink from /Users/art/test-home/.zsh/02-prompt-colors to /Users/art/.dotfiles/zsh/.zsh/02-prompt-colors was created
    LINK  Symlink from /Users/art/test-home/.zsh/03-prompt to /Users/art/.dotfiles/zsh/.zsh/03-prompt was created
    LINK  Symlink from /Users/art/test-home/.zsh/aliases to /Users/art/.dotfiles/zsh/.zsh/aliases was created
    LINK  Symlink from /Users/art/test-home/.zsh/ash to /Users/art/.dotfiles/zsh/.zsh/ash was created
    LINK  Symlink from /Users/art/test-home/.zsh/dotfiler to /Users/art/.dotfiles/zsh/.zsh/dotfiler was created
    LINK  Symlink from /Users/art/test-home/.zsh/ssh-agent to /Users/art/.dotfiles/zsh/.zsh/ssh-agent was created
    LINK  Symlink from /Users/art/test-home/.zsh/tmux to /Users/art/.dotfiles/tmux/.zsh/tmux was created

![](http://img-fotki.yandex.ru/get/9314/13558447.f/0_aa150_6aa53046_L.jpg)

Now we've added another environment with dotfiles for Tmux. It contains not only Tmux's config, but also a zsh config with some aliases. It will be wrong to symlink that `.zsh/tmux` file to the current `~/.zsh`, because it is a symlink into another environment. That is why dotfiler removed `~/.zsh` symlink, created a usual directory instead and symlinked all necessary configs there.

Nobody do this. Nobody!

All logic is written and unittested in Python 2.7. I'm planning to add this project on Travis, to be able to test it under different pythons. If you'll find any bugs, don't hesitate to [issue them in the GitHub](https://github.com/svetlyak40wt/dotfiler/issues) or even to send me a pull request.

P.S. — a small hint for those who read through the whole article. Command `dot add` is able to get more than one repository at once.
P.P.S. — also, take look at `dot status`, it is cool!

[dotfiler]: https://github.com/svetlyak40wt/dotfiler