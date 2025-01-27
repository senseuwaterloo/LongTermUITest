#!/bin/bash

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
XVFB_PID=$(pgrep -f "Xvfb :99")

if [ -z "$XVFB_PID" ]; then
  echo "No Xvfb process found on display :99"
else
  kill "$XVFB_PID"
  echo "Xvfb process on display :99 stopped"
fi

TMPDIR=$(mktemp -d)
Xvfb :99 -screen 0 2560x1440x16 -fbdir "$TMPDIR" &
XVFB_PID=$!

export DISPLAY=:99

pytest test/ --html="report_$TIMESTAMP.html"

kill $XVFB_PID