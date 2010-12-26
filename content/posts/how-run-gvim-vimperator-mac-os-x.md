Title: How to run GVim from Vimperator on Mac OS X
Slug: how-run-gvim-vimperator-mac-os-x
Date: 2009-09-11 17:59
Tags: vim, shell
Category: texts
Lang: en
Description: A short script which help to run GVim from Vimperator, if GVim was installed from MacPorts.

I started to use [Vimperator](http://vimperator.org) for navigation through the Web, but one of it's useful feature — call for external editor (via shortcut Ctrl-i), to edit textareas, does not work with GVim, if GVim was installed from MacPorts.

The problem is in the /opt/local/bin/gvim script, which actually fork GVim and obey any options like --nofork.

Here is a small script, which start GVim with 'nofork' options. Place it somewhere in ~/usr/bin.

    :::sh
    #!/bin/sh
    binary="/Applications/MacPorts/Vim.app/Contents/MacOS/Vim"
    exec "$binary" -g -f ${1:+"$@"}

Next setup Vimperator 'editor' option:

    :::vim
    :set editor=~/usr/bin/gvim_nofork