

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
import pydub
from pydub import AudioSegment
import numpy as np
import os


global isaudioplaying
isaudioplaying = [False]
global duration
duration = [0]

class playaudio_class1:
    
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
        #self.file = AudioSegment.from_mp3()
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

class playaudio_class:
    
    def __init__(self):
        self.stopstream  = None
        self.file = None
        self.p = None 
    def getisaudioplaying(self):
        #print(isaudioplaying[0])
        return isaudioplaying[0]


    def playaudio(self,filename=None,deviceindex=None,chunksize=None,volume=1):
        
        print(deviceindex)
        self.p = pyaudio.PyAudio()
        for i in range(self.p.get_device_count()):
            print (self.p.get_device_info_by_index(i).get('name'))
        #filename = "life line mf.wav"
        
        # Defines a chunk size of 1024 samples per data frame.
        chunk = chunksize 
        
        # Open sound file  in read binary form.
        #self.file = wave.open(filename, 'rb')
        #self.file = AudioSegment.from_mp3()
        a, fr ,asg = self.audio_file_to_np_array(filename)
        dvc = deviceindex  # Index of an OUTPUT device (from sd.query_devices() on YOUR machine)
        sd.default.device = dvc  # Change default OUTPUT device
        sd.play(a*volume, samplerate=fr)
        #sd.wait()
        duration[0] = asg.duration_seconds
        while duration[0] > 0:
            
            time.sleep(0.02)
            duration[0] -= 0.02
            isaudioplaying[0] = True
            voice_mode_ui.setisaudioplaying(True)
            print(duration)
            #print("stofocedfromui"+str(voice_mode_ui.getisstopfoced()))
        print('stop')    
        sd.stop()    
        isaudioplaying[0] = False
        voice_mode_ui.setisaudioplaying(False)
        globle_key_listener.itwasdone(True)

    
        '''def callback(outdata, frames, time, status):
            if status:
                print(a)
            outdata[:] = a
        with sd.OutputStream(
                samplerate=fr, device=deviceindex, channels=asg.channels,
                callback=callback):
            while sd.Stream.active:
                time.sleep(0.02)  '''  
        
        
        

    def audio_file_to_np_array(self,file_name):
        pydub.AudioSegment.converter = os.getcwd()+ "\\ffmpeg.exe"                    
        pydub.AudioSegment.ffprobe   = os.getcwd()+ "\\ffprobe.exe"
        asg = pydub.AudioSegment.from_file(file_name)
        dtype = getattr(np, "int{:d}".format(asg.sample_width * 8))  # Or could create a mapping: {1: np.int8, 2: np.int16, 4: np.int32, 8: np.int64}
        #arr = np.ndarray((int(asg.frame_count()), asg.channels), buffer=asg.raw_data, dtype=dtype)
        arr = np.array(asg.get_array_of_samples(), dtype=np.float32).reshape((-1, asg.channels)) / (
            1 << (8 * asg.sample_width - 1))
        #print("\n", asg.frame_rate, arr.shape, arr.dtype, arr.size, len(asg.raw_data), len(asg.get_array_of_samples()))  # @TODO: Comment this line!!!
        return arr, asg.frame_rate ,asg
       
def stopplaying():
    sd.stop()    
    isaudioplaying[0] = False
    voice_mode_ui.setisaudioplaying(False)
    globle_key_listener.itwasdone(True)
    duration[0] = 0