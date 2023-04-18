import pyaudio
import struct
import math
import datetime
import time
import audioop


THRESHOLD = 50
FORMAT = pyaudio.paInt16 
SHORT_NORMALIZE = (1.0/32768.0)
CHANNELS = 1
RATE = 44100  
INPUT_BLOCK_TIME = 0.01
INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)


detectedmic1 = False
detectedmic2 = False
#detectedmic3 = False
#detectedmic4 = False

amplitude_list = [0, 0]
#amplitude_list = [0, 0, 0, 0]

mic_position_list = ["right", "left", "both", "Back Left"]

def get_rms(block):
    return audioop.rms(block, 2)

class TapTester(object):
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream1 = self.open_mic1_stream()
        self.stream2 = self.open_mic2_stream()
        #self.stream3 = self.open_mic3_stream()
        #self.stream4 = self.open_mic4_stream()
        self.threshold = THRESHOLD

    def stop(self):
        self.stream.close()

    def open_mic1_stream(self):

        stream = self.pa.open(   format = FORMAT,
                                 channels = CHANNELS,
                                 rate = RATE,
                                 input = True,
                                 input_device_index = 0, 
                                 frames_per_buffer = INPUT_FRAMES_PER_BLOCK)        

        return stream
    
    def open_mic2_stream(self):

        stream = self.pa.open(   format = FORMAT,
                                 channels = CHANNELS,
                                 rate = RATE,
                                 input = True,
                                 input_device_index = 1,
                                 frames_per_buffer = INPUT_FRAMES_PER_BLOCK)

        return stream
    
    '''def open_mic3_stream( self ):
        stream = self.pa.open(  format = FORMAT,
                                 channels = CHANNELS,
                                 rate = RATE,
                                 input = True,
                                 input_device_index = 6,
                                 frames_per_buffer = INPUT_FRAMES_PER_BLOCK)
        return stream
    
    def open_mic4_stream( self ):
        stream = self.pa.open(  format = FORMAT,
                                 channels = CHANNELS,
                                 rate = RATE,
                                 input = True,
                                 input_device_index = 4,
                                 frames_per_buffer = INPUT_FRAMES_PER_BLOCK)
        return stream '''

    def listen(self):
        
        block1 = self.stream1.read(INPUT_FRAMES_PER_BLOCK, exception_on_overflow = False)
        amplitude_list[0] = get_rms(block1)
        
        block2 = self.stream2.read(INPUT_FRAMES_PER_BLOCK, exception_on_overflow = False)
        amplitude_list[1] = get_rms(block2)
        
        #block3 = self.stream3.read(INPUT_FRAMES_PER_BLOCK, exception_on_overflow = False)
        #amplitude_list[2] = get_rms(block3)
        
        #block4 = self.stream4.read(INPUT_FRAMES_PER_BLOCK, exception_on_overflow = False)
        #amplitude_list[3] = get_rms(block4) 
        
        print(amplitude_list)
        '''max_amplitude_index = 0
        max_amplitude = amplitude_list[0]
        for i in range(0, len(amplitude_list)):
            if (amplitude_list[i] > max_amplitude):
                max_amplitude_index = i
                max_amplitude = amplitude_list[i]
        if max_amplitude > self.threshold:
            print("Amplitude is:")
            print(max_amplitude)
            return(mic_position_list[max_amplitude_index])'''
            
if __name__ == "__main__":
    tt = TapTester()
    
    while True:
    	tt.listen()
