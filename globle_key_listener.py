from pynput.keyboard import Key, Listener
import pynput
import audio
import voice_mode_ui
import re

global modifirekeys
modifirekeys = ["Key.alt_l","Key.alt_gr"]
currentkey = []
global calledtimes
calledtimes = [0]
global workdone
workdone = [True]

def itwasdone(doneornot):
    calledtimes[0] = 0
    currentkey.clear()
    workdone[0] = doneornot 

def starlistener(hotkeydict,selecteddiviceinderx):
    def callplayaudio(pressedkey):
        print(pressedkey)
        calledtimes[0] +=1
        if calledtimes[0] < 2:
            afilename = hotkeydict[pressedkey]
            audio.playaudio(filename=afilename,deviceindex=selecteddiviceinderx,chunksize=1024)
        else:
            print("done")
            calledtimes[0] = 0
            currentkey.clear()



    def on_press(key):
        print('{0} pressed'.format(
            key))
        strkey = str(key) 
        
        currentkey.append(strkey)   
        print(str(key))
        
        if currentkey[0] in modifirekeys:
            print("must be have second or more keys") 
            if strkey != currentkey[0] and len(currentkey) <2:
                currentkey.append(strkey)
        else:
            currentkey.clear()
            currentkey.append(strkey)        
        print(currentkey)    
    def on_release(key):
        print('{0} release'.format(
            key))
        if len(currentkey) >1:
            try:
                print(currentkey[0]+"+"+str(currentkey[1]).replace("'","") +" "+str(hotkeydict.keys()))
                for i in hotkeydict.keys():
                    if currentkey[0]+"+"+str(currentkey[1]).replace("'","") == i:
                        print("play audio of key "+str(i))
                        callplayaudio(str(i))    
                currentkey.clear()
            except:
                pass
        if key == Key.esc:
            # Stop listener
            return False

    # Collect events until released
    print(str(hotkeydict))
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
  
