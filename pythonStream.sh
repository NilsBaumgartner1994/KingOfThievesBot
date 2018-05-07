#!/bin/bash
RTMP_URL=rtmp://live-fra.twitch.tv/app/
STREAM_KEY=live_60571661_eMyGKli6Lq6JXikzJlld0KCOfNOhon
while :
do
  python startPythonStream.py | ffmpeg -i - -vcodec copy -an -metadata title="Streaming from raspberry pi camera" -f flv  $RTMP_URL/$STREAM_KEY
  sleep 2
done 
