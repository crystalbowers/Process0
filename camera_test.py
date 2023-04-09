import cv2
import time
import os
import bluetooth

# Set up Bluetooth connection
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

bluetooth.advertise_service(server_sock, "VideoTransferService",
                            service_id=bluetooth.SERIAL_PORT_CLASS,
                            profiles=[bluetooth.SERIAL_PORT_PROFILE])

print("Waiting for Bluetooth connection on RFCOMM channel", port)
client_sock, client_info = server_sock.accept()
print("Accepted Bluetooth connection from", client_info)

# Set up camera
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FPS, 30)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Record video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
filename = 'video.mp4'
out = cv2.VideoWriter(filename, fourcc, 30.0, (640, 480))
start_time = time.time()

while(time.time() - start_time < 3):
    ret, frame = camera.read()
    if ret:
        out.write(frame)

# Release resources
camera.release()
out.release()

# Send video over Bluetooth
print("Sending video over Bluetooth")
with open(filename, 'rb') as f:
    data = f.read()
    client_sock.sendall(data)

# Delete video file
os.remove(filename)

# Close Bluetooth connection
client_sock.close()
server_sock.close()
print("Video sent. Bluetooth connection closed")