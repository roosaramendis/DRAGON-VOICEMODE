

from winsound import PlaySound
import pyaudio
import sounddevice as sd
import wave
import sys
import time
import globle_key_listener
import voice_mode_ui
import argparse
import threading



global isaudioplaying
isaudioplaying = [False]

class playaudio_class:
    
    def __init__(self):
        self.stopstream  = None
        self.file = None
        self.p = None 
    def getisaudioplaying(self):
        #print(isaudioplaying[0])
        return isaudioplaying[0]


    def playaudio(self,filename=None,deviceindex=None,chunksize=None):
        
        print(deviceindex)
        self.p = pyaudio.PyAudio()
        for i in range(self.p.get_device_count()):
            print (self.p.get_device_info_by_index(i).get('name'))
        #filename = "life line mf.wav"
        
        # Defines a chunk size of 1024 samples per data frame.
        chunk = chunksize 
        
        # Open sound file  in read binary form.
        self.file = wave.open(filename, 'rb')
        def callback(in_data, frame_count, time_info, status):
            data = self.file.readframes(frame_count)
            return (data, pyaudio.paContinue)
        # Creates a Stream to which the wav file is written to.
        # Setting output to "True" makes the sound be "played" rather than recorded
        self.stream = self.p.open(format = self.p.get_format_from_width(self.file.getsampwidth()),
                        channels = self.file.getnchannels(),
                        rate = self.file.getframerate(),
                        output = True,
                        output_device_index=deviceindex,
                        stream_callback=callback)
        
        # Read data in chunks
        data = self.file.readframes(chunk)
        
        # Play the sound by writing the audio data to the stream
        self.stream.start_stream()
        while self.stream.is_active():
            isaudioplaying[0] = True
            voice_mode_ui.setisaudioplaying(True)
            time.sleep(0.03)#0.1

        
        # Stop, Close and terminate the stream
        #self.stopstream()
        self.stream.stop_stream()
        self.stream.close()
        self.file.close()
        self.p.terminate()
        isaudioplaying[0] = False
        voice_mode_ui.setisaudioplaying(False)
        globle_key_listener.itwasdone(True)


    def stopstream(self):
        
        self.stream.stop_stream()
        self.stream.close()
        self.file.close()
        self.p.terminate()
        isaudioplaying[0] = False
        voice_mode_ui.setisaudioplaying(False)
        globle_key_listener.itwasdone(True)


