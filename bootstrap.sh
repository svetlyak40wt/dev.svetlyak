#!/bin/bash

virtualenv env --python=python2.6
pip -E env install 'git+git://github.com/svetlyak40wt/pelican.git@customizable#egg=Pelican'
#env/bin/easy_install pelican
