

import pyaudio
import sounddevice as sd
import wave
import sys
import time
import globle_key_listener
import voice_mode_ui

global isaudioplaying
isaudioplaying = [False]

def getisaudioplaying():
    #print(isaudioplaying[0])
    return isaudioplaying[0]

def playaudio(filename,deviceindex,chunksize):

    print(deviceindex)
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        print (p.get_device_info_by_index(i).get('name'))
    #filename = "life line mf.wav"
    
    # Defines a chunk size of 1024 samples per data frame.
    chunk = chunksize 
    
    # Open sound file  in read binary form.
    file = wave.open(filename, 'rb')
    def callback(in_data, frame_count, time_info, status):
        data = file.readframes(frame_count)
        return (data, pyaudio.paContinue)
    # Creates a Stream to which the wav file is written to.
    # Setting output to "True" makes the sound be "played" rather than recorded
    stream = p.open(format = p.get_format_from_width(file.getsampwidth()),
                    channels = file.getnchannels(),
                    rate = file.getframerate(),
                    output = True,
                    output_device_index=deviceindex,
                    stream_callback=callback)
    
    # Read data in chunks
    data = file.readframes(chunk)
    
    # Play the sound by writing the audio data to the stream
    stream.start_stream()
    while stream.is_active():
        isaudioplaying[0] = True
        voice_mode_ui.setisaudioplaying(True)
        time.sleep(0.03)#0.1

    
    # Stop, Close and terminate the stream
    
    stream.stop_stream()
    stream.close()
    file.close()
    p.terminate()
    isaudioplaying[0] = False
    voice_mode_ui.setisaudioplaying(False)
    globle_key_listener.itwasdone(True)


# Flag to indicate the program whether should continue running.
