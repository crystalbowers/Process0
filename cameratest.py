# Simple Test
#  Ctrl^C to exit
# sensor_id selects the camera: 0 or 1 on Jetson Nano B01
$ gst-launch-1.0 nvarguscamerasrc sensor_id=0 ! nvoverlaysink

# More specific - width, height and framerate are from supported video modes
# Example also shows sensor_mode parameter to nvarguscamerasrc
# See table below for example video modes of example sensor
$ gst-launch-1.0 nvarguscamerasrc sensor_id=0 ! \
   'video/x-raw(memory:NVMM),width=1920, height=1080, framerate=30/1' ! \
   nvvidconv flip-method=0 ! 'video/x-raw,width=960, height=540' ! \
   nvvidconv ! nvegltransform ! nveglglessink -e ! nveglglessink -e