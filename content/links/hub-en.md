Title: Git helper for GitHub Users
Slug: hub
Date: 2011-04-14 12:26
Category: links
Tags: git
Lang: en

Found a [helper](http://defunkt.io/hub/), to work with GitHub from command line. All your need is Ruby (it is already included into the Mac OS X). This script should be downloaded into the `PATH`, and aliased as `alias git=hub`.

To use all features, you also have to add you username and GitHub's API token into the `~/.gitconfig`:

    [github]
        user = svetlyak40wt
        token = a-secret-token

Afterwards, you'll be able to make a quick fork of any GitHub project, for example, mine [ForkFeed](http://github.com/svetlyak40wt/forkfeed) is a good candidate as it is useful for GitHub users too:

    git clone svetlyak40wt/forkfeed
    cd forkfeed
    git fork

Have a fun!
