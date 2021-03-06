import pyaudio
import sounddevice as sd
import wave
import sys
from global_hotkeys import *
import keyboard
import time
#from pydub import AudioSegment
#filename = "C:\Users\mendis\Music\life line mf.mp3"
#song = AudioSegment.from_mp3("C:\Users\mendis\Music\life line mf.mp3")


def playaudio(filename,deviceindex,chunksize):
    print("sdf")
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        print (p.get_device_info_by_index(i).get('name'))
    #filename = "life line mf.wav"
    
    # Defines a chunk size of 1024 samples per data frame.
    chunk = chunksize 
    
    # Open sound file  in read binary form.
    file = wave.open(filename, 'rb')
    # Creates a Stream to which the wav file is written to.
    # Setting output to "True" makes the sound be "played" rather than recorded
    stream = p.open(format = p.get_format_from_width(file.getsampwidth()),
                    channels = file.getnchannels(),
                    rate = file.getframerate(),
                    output = True,
                    output_device_index=deviceindex)
    
    # Read data in chunks
    data = file.readframes(chunk)
    
    # Play the sound by writing the audio data to the stream
    while data != '':
        stream.write(data)
        data = file.readframes(chunk)
    
    # Stop, Close and terminate the stream
    stream.stop_stream()
    stream.close()


# Flag to indicate the program whether should continue running.
