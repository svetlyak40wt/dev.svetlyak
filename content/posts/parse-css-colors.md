Title: How to parse CSS colors?
Slug: parse-css-colors
Date: 2009-11-30 21:03
Tags: python, snippet
Category: texts
Lang: en
Description: Python function to parse CSS colors

    :::python
    def parse_color(s):
        """ Parses color string in format #ABC or #AABBCC to RGB tuple. """
        l = len(s)
        assert(l in (4,5,7,9))
    
        if l in (4,5):
            return tuple(int(ch * 2, 16) for ch in s[1:])
        else:
            return tuple(int(ch1 + ch2, 16) for ch1, ch2 in \
                         zip(
                            (ch1 for ch1 in s[1::2]),
                            (ch2 for ch2 in s[2::2])
                            )
                        )

Here is a [gist file](http://gist.github.com/245648).