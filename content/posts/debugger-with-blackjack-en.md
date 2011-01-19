Title: Debugger With Blackjack
Slug: debugger-with-blackjack
Date: 2011-01-18 14:13
Category: review
Tags: python
Lang: en

I decided to adhere to a certain post publication schedule. I'll try to publish something interesting every Tuesday and Thursday.

Today I want to tell you about a pretty useful tool — namely, on the debugger. If you're not a fan of full-fledged IDE, you probably used the standard Python debugger pdb. It covers 90% of the necessary functionality to me, but still somewhat inconvenient. For example, there is no auto-complete and it is annoying to run `list` command after an every few steps just to see the current line's context.

The project pdbpp was created to solve these, as well as some other issues. Here are a few features, which proved to me the most useful:

* a sticky mode — in this mode, the debugger redraws current function after each step of the interpreter;
* tag auto-complete — you no longer have to call `dir(obj)` just to view an object's interface;
* syntax highlighting — pdbpp uses Pygments, to make the code even more beautiful than it is (your code is amazing, right?).

In addition, there are such things as calling the editor to correct the file is being traced, an intelligent parsing of the command, the command `longlist (ll)` to display the current function or method.

Here is a typical pdbpp session:

![](http://bitbucket.org/antocuni/pdb/raw/0c86c93cee41/screenshot.png)

In order to use this wonderful tool, it is enough to set it into the system by any of the methods available to you, then, as usual, you can use it as usual: `import pdb; pdb.set_trace()`.

**Update:** recorded a short demo of how it works (comments are in russian).

<object classid='clsid:d27cdb6e-ae6d-11cf-96b8-444553540000' codebase='http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=9,0,115,0' width='560' height='345'><param name='movie' value='http://screenr.com/Content/assets/screenr_1116090935.swf' ></param><param name='flashvars' value='i=158211' ></param><param name='allowFullScreen' value='true' ></param><embed src='http://screenr.com/Content/assets/screenr_1116090935.swf' flashvars='i=158211' allowFullScreen='true' width='560' height='345' pluginspage='http://www.macromedia.com/go/getflashplayer' ></embed></object>

[pdbpp]: https://bitbucket.org/antocuni/pdb/src
