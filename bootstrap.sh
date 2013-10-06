#!/bin/bash

virtualenv env --python=python2.6
env/bin/pip install -r requirements/development.txt
