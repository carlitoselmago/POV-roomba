#!/bin/bash

# Start the Python server in the background
~/POV-roomba/python server.py &

# Start the UV4L server in the background
uv4l --external-driver --device-name=video0 &

# Wait for all background jobs to finish
wait