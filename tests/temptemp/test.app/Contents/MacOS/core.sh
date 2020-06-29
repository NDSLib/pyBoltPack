#!/bin/sh
pwd
SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
echo $SCRIPTPATH

$SCRIPTPATH/venv/bin/python3 testapp.py
