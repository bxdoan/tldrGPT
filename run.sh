#!/bin/sh

# set pipenv path
if [ `uname` = "Darwin" ]; then
    pipenv="/Users/`whoami`/.local/bin/pipenv"
else
    pipenv="/home/`whoami`/.pyenv/shims/pipenv"
fi

PYTHONPATH=`pwd` $pipenv run python tldrGPT.py -url $@