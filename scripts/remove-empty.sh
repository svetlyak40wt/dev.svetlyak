#!/bin/bash
cd content/buzz
ls -l | grep ' 0 26' | cut -d ' ' -f 15 | xargs rm
