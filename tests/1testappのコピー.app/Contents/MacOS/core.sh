#!/bin/sh

#run.sh &
#python3 main.py

osascript -e 'tell application (path to frontmost application as text) to display dialog "Hello from osxdaily.com" buttons {"OK"} with icon stop'

python3 /Users/unkonow/Documents/pg/python/nowProject/BoltPack/tests/testapp.app/Contents/MacOS/main.py
python3 main.py

osascript -e 'tell application (path to frontmost application as text) to display dialog "Hello from osxdaily.com" buttons {"OK"} with icon stop'

exit 0
