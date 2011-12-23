#!/bin/bash

virtualenv env --python=python2.6
pip -E env install -r requirements.txt
