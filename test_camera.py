DISPLAY=:0.0 gst-launch-1.0 nvarguscamerasrc !'video/x-raw(memory:NVMM), width=3280,height=2464, format=(string)NV12, framerate=(fraction)20/1'! nvoverlaysink -e
