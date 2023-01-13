import argparse
from email.mime import audio
import time
import sounddevice as sd
import numpy  
assert numpy  
import threading
import voice_mode_ui
import audio
import numpy as np
from PyQt5.QtCore import QSettings

global voicechanger
voicechanger = True
global stopstreaminmicintoout
stopstreaminmicintoout  = [False]
global overridehearuselfdevice
overridehearuselfdevice = [0]
global hearmyselfdevice
hearmyselfdevice = ['']
global hearmyselfvolume
hearmyselfvolume = [1]
global overridesoundboardvolume
overridesoundboardvolume = [0]
global soundboardvolume
soundboardvolume = [1]
global pitchvolume
pitchvolume = [1]
global pitch
pitch = [1]
global pitchshift
pitchshift = [0]
global selectedoutputdevicetext
selectedoutputdevicetext = ['']
global selectedinputdevicetext
selectedinputdevicetext = ['']


def getsettingvals():
    global settingval
    settingval = QSettings("DragonVoiceMode","settings vals")
    
    selectedoutputdevicetext[0] = settingval.value("selectedoutputdevicetext")
    selectedinputdevicetext[0] = settingval.value("selectedinputdevicetext")
    overridehearuselfdevice[0] = settingval.value("overridehearuselfdevice")
    hearmyselfdevice[0] = settingval.value("hearmyselfdevice")
    hearmyselfvolume[0] = settingval.value("hearmyselfvolume")
    overridesoundboardvolume[0] = settingval.value("overridesoundboardvolume")
    soundboardvolume[0] = settingval.value("soundboardvolume")
    pitchvolume[0] = settingval.value("pitchvolume")
    pitch[0] = settingval.value("pitch")
    pitchshift[0] = settingval.value("pitchshift")

def startmictooutputforhearaudio(inputdeviceindex,outputdeviceindex,volume):
    def int_or_str(text):
        """Helper function for argument parsing."""
        try:
            return int(text)
        except ValueError:
            return text


    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        '-l', '--list-devices', action='store_true',
        help='show list of audio devices and exit')
    args, remaining = parser.parse_known_args()
    if args.list_devices:
        print(sd.query_devices())
        parser.exit(0)
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[parser])
    parser.add_argument(
        '-i', '--input-device', type=int_or_str,
        help='input device (numeric ID or substring)')
    parser.add_argument(
        '-o', '--output-device', type=int_or_str,
        help='output device (numeric ID or substring)')
    parser.add_argument(
        '-c', '--channels', type=int, default=2,
        help='number of channels')
    parser.add_argument('--dtype', help='audio data type')
    parser.add_argument('--samplerate', type=float, help='sampling rate')
    parser.add_argument('--blocksize', type=int, help='block size')
    parser.add_argument('--latency', type=float, help='latency in seconds')
    args = parser.parse_args(remaining)


    def callback(indata, outdata, frames, time, status):
        if status:
            print(status+" stats")
        settingval = QSettings("DragonVoiceMode","settings vals")    
        outdata[:] = (indata) * settingval.value("hearmyselfvolume")/100
  
    print("mic input stated")
    print(volume)
    print(str(inputdeviceindex)+str(outputdeviceindex))
    with sd.Stream(device=(inputdeviceindex, outputdeviceindex),
                    samplerate=args.samplerate, blocksize=args.blocksize,
                    dtype=args.dtype, latency=args.latency,
                    channels=args.channels, callback=callback):
        '''print('#' * 80)
        print('press Return to quit')
        print('#' * 80)'''
        #input()
        while sd.Stream.active:
            settingval = QSettings("DragonVoiceMode","settings vals")
            time.sleep(float(settingval.value("loopdelaytime")))
            if audio.playaudio_class().getisaudioplaying() == False:
                print("stopthis shit")
                settingval.setValue("audio_stat","Idle")
                break    



def startmictooutput(inputdeviceindex,outputdeviceindex):
    def int_or_str(text):
        """Helper function for argument parsing."""
        try:
            return int(text)
        except ValueError:
            return text


    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        '-l', '--list-devices', action='store_true',
        help='show list of audio devices and exit')
    args, remaining = parser.parse_known_args()
    if args.list_devices:
        print(sd.query_devices())
        parser.exit(0)
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[parser])
    parser.add_argument(
        '-i', '--input-device', type=int_or_str,
        help='input device (numeric ID or substring)')
    parser.add_argument(
        '-o', '--output-device', type=int_or_str,
        help='output device (numeric ID or substring)')
    parser.add_argument(
        '-c', '--channels', type=int, default=2,
        help='number of channels')
    parser.add_argument('--dtype', help='audio data type')
    parser.add_argument('--samplerate', type=float, help='sampling rate')
    parser.add_argument('--blocksize', type=int, help='block size')
    parser.add_argument('--latency', type=float, help='latency in seconds')
    args = parser.parse_args(remaining)


    def pitchchange(data,pitch):
        
        shift = pitch//100
        freq = np.fft.rfft(data)
        N = len(freq)
        sh_freq = np.zeros(N, freq.dtype)
        S = int(np.round(pitch if pitch > 0 else N + pitch, 0))
        s = int(N-S)
        sh_freq[:S] = freq[s:]
        sh_freq[S:] = freq[:s]
        sh_chunk = np.fft.irfft(sh_freq)
        return sh_chunk.astype(data.dtype)

    def callback(indata, outdata, frames, time, status):
        if status:
            print(status)
        if voicechanger == False:    
            outdata[:] = indata
        elif voicechanger == True:
            getsettingvals()
            if pitchshift[0] == 2:
                print("pitchshit enable")    
                outdata[:] = (pitchchange(indata,pitch[0]))*pitchvolume[0]
            elif pitchshift[0] == 0:
                outdata[:] = indata
    
    print("mic input stated")
    print(str(inputdeviceindex)+str(outputdeviceindex))
    with sd.Stream(device=(inputdeviceindex, outputdeviceindex),
                    samplerate=args.samplerate, blocksize=args.blocksize,
                    dtype=args.dtype, latency=args.latency,
                    channels=args.channels, callback=callback):

        while sd.Stream.active:
            settingval = QSettings("DragonVoiceMode","settings vals")
            time.sleep(float(settingval.value("loopdelaytime")))
               

def stopmictoinput():
    pass
    #print('stoping'+str(sd.Stream.active))
    '''parser = argparse.ArgumentParser(add_help=False)
    parser.exit('exit')'''
    

def startmictooutputcall(inputdeviceindex,outputdeviceindex,volume):
    t1 = threading.Thread(target=startmictooutputforhearaudio,args=(inputdeviceindex,outputdeviceindex,volume))
    t1.start()

