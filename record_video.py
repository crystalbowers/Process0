# From https://forums.developer.nvidia.com/t/displaying-to-the-screen-with-opencv-and-gstreamer/140648/8

import sys
import cv2

def read_cam():
    cap = cv2.VideoCapture("filesrc location=/home/nvidia/sample_1080p_h264.mp4 ! qtdemux ! h264parse ! nvv4l2decoder ! nvvidconv ! video/x-raw, format=BGRx ! videoconvert ! video/x-raw,format=BGR ! appsink  ")

    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print('Src opened, %dx%d @ %d fps' % (w, h, fps))

    gst_out = "appsrc ! video/x-raw, format=BGR ! queue ! videoconvert ! video/x-raw,format=BGRx ! nvvidconv ! nvv4l2h264enc ! h264parse ! matroskamux ! filesink location=test.mkv "
    out = cv2.VideoWriter(gst_out, cv2.CAP_GSTREAMER, 0, float(fps), (int(w), int(h)))
    if not out.isOpened():
        print("Failed to open output")
        exit()

    if cap.isOpened():
        while True:
            ret_val, img = cap.read();
            if not ret_val:
                break;
            out.write(img);
            cv2.waitKey(1)
    else:
     print("pipeline open failed")

    print("successfully exit")
    cap.release()
    out.release()


if __name__ == '__main__':
    read_cam()