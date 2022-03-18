from tkinter import EXCEPTION
from tracemalloc import stop
from turtle import st
from pynput.keyboard import Key, Listener
import pynput
import audio
import voice_mode_ui
import re
import struct
import binascii
import threading
from PyQt5.QtCore import QSettings
from plyer.utils import platform
from plyer import notification

global modifirekeys
modifirekeys = ["Key.alt_l","Key.alt_gr","Key.ctrl_l","Key.shift","Key.ctrl_r","Key.shift_r"]
currentkey = []
currentkey1 = []
currentreleaskey1 = []
currentreleaskey = []
currentkey_sa = [] #for use in stop audio hotkey
currentreleaskey_sa = [] #for use in stop audio hotkey
global calledtimes
calledtimes = [0]
global workdone
workdone = [True]
global alphabet
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
global keyboardnumbers
keyboardnumbers = ['0','1','2','3','4','5','6','7','8','9']
on_releasetimes = [0]

def itwasdone(doneornot):
    calledtimes[0] = 0
    currentkey.clear()
    workdone[0] = doneornot 

def starlistener_old(hotkeydict,selecteddiviceinderx,volume=1):
    def callplayaudio(pressedkey):
        print(pressedkey)
        calledtimes[0] +=1
        if calledtimes[0] < 2:
            afilename = hotkeydict[pressedkey]
            print(volume)
            audio.playaudio_class().playaudio(filename=afilename,deviceindex=selecteddiviceinderx,chunksize=1024,volume=volume)
        else:
            print("done")
            calledtimes[0] = 0
            currentkey.clear()



    def on_press(key):
        strkey = str(key)
        try:
            if not(re.search("Key.",str(key))):
                print(keyboardnumbers)
                if not(str(key).replace("'","") in keyboardnumbers):
                    print(str(key))
                    formatedkeyhex = str(key).replace("'\\x","")
                    formatedkeyhex = formatedkeyhex.replace("'","")
                    print(formatedkeyhex)
                    print(int(formatedkeyhex, 16))
                    keyindex = int(formatedkeyhex, 16)
                    if keyindex < 27:
                        print('{0} pressed'.format(
                        alphabet[keyindex-1]))
                        strkey = str(alphabet[keyindex-1])
        except Exception as e:
            print(e)
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
        """if key == Key.esc:
            # Stop listener
            return False"""

    # Collect events until released
    print(str(hotkeydict))
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
  
def starcapture_hk_old():

    def setstophk(hkey):
        settingval = QSettings("Dragon Voide Mode","settings vals")
        captrdkey = hkey[0]+"+"+hkey[1]
        settingval.setValue("stophotkey",captrdkey)
        print(captrdkey)

    def on_press(key):
        strkey = str(key)
        try:
            if not(re.search("Key.",str(key))):
                print(keyboardnumbers)
                if not(str(key).replace("'","") in keyboardnumbers):
                    print(str(key))
                    formatedkeyhex = str(key).replace("'\\x","")
                    formatedkeyhex = formatedkeyhex.replace("'","")
                    print(formatedkeyhex)
                    print(int(formatedkeyhex, 16))
                    keyindex = int(formatedkeyhex, 16)
                    if keyindex < 27:
                        print('{0} pressed'.format(
                        alphabet[keyindex-1]))
                        strkey = str(alphabet[keyindex-1])
        except Exception as e:
            print(e)
            print('{0} pressed'.format(
            key))    
            strkey = str(key)
        
        currentkey1.append(strkey)   
        print(currentkey1)
        
        if currentkey1[0] in ["Key.alt_l","Key.alt_gr","Key.ctrl_l"]:
            print("must be have second or more keys") 
            if strkey != currentkey1[0] and len(currentkey1) <2:
                currentkey1.append(strkey)
        else:
            currentkey1.clear()
            currentkey1.append(strkey)        
        print(str(currentkey1)+"on press")    
    def on_release(key):
        print('{0} release'.format(
            key))
        if len(currentkey1) >1:
            try:
                print(currentkey1[0]+"+"+str(currentkey1[1]).replace("'",""))
                setstophk(currentkey1)
                print(str(currentkey1)+"on releas")
                #return currentkey    
                currentkey.clear()
            except:
                pass
        """if key == Key.esc:
            # Stop listener
            return False"""

    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def starlistener(hotkeydict,selecteddiviceinderx,volume=1):

    def callplayaudio(pressedkey):
        print(pressedkey)
        calledtimes[0] +=1
        if calledtimes[0] < 2:
            if len(pressedkey)>2:
                pressedkeystr = pressedkey[0]+"+"+pressedkey[1]+"+"+pressedkey[2].replace("'","")
            elif len(pressedkey)>1:
                pressedkeystr = pressedkey[0]+"+"+pressedkey[1].replace("'","")
            elif len(pressedkey) == 1:
                pressedkeystr = pressedkey[0].replace("'","")
            afilename = hotkeydict[pressedkeystr]
            print(volume)
            audio.playaudio_class().playaudio(filename=afilename,deviceindex=selecteddiviceinderx,chunksize=1024,volume=volume)
        else:
            print("done")
            calledtimes[0] = 0
            currentkey.clear()



    def on_press(key):
        strkey = str(key)
        print(strkey+'instarlsitnerfun')

        print(strkey)

        try:
            if not(re.search("Key.",str(key))):
                print(keyboardnumbers)
                if not(str(key).replace("'","") in keyboardnumbers):
                    print(str(key))
                    formatedkeyhex = str(key).replace("'\\x","")
                    formatedkeyhex = formatedkeyhex.replace("'","")
                    print(formatedkeyhex)
                    print(int(formatedkeyhex, 16))
                    keyindex = int(formatedkeyhex, 16)
                    if keyindex < 27:
                        print('{0} pressed'.format(
                        alphabet[keyindex-1]))
                        strkey = str(alphabet[keyindex-1])
        except Exception as e:
            print(e)
            print('{0} pressed'.format(
            key))    
            strkey = str(key)
        try:
            if strkey in modifirekeys and not(len(currentkey)-1 == strkey):
                print("if true")
                currentkey.append(strkey)
            if len(currentkey)>=1:
                if strkey!=currentkey[0] and strkey in modifirekeys and len(currentkey)<2:
                    currentkey.append(strkey)
                    print(currentkey)   
                else:
                    print("sssssss")
                    
                    if len(currentkey)>1:
                        if strkey!=currentkey[1] and strkey in modifirekeys and len(currentkey)<2 and not(strkey in currentkey):
                            currentkey.append(strkey)
                            print(currentkey)
                        else:
                            print("sssssss2")
                            if not(strkey in currentkey):
                                currentkey.append(strkey)     
                    elif currentkey[0] != strkey:
                        currentkey.append(strkey)
                    #currentkey1.append(strkey)
            elif currentkey[0] != strkey:
                currentkey.append(strkey)

            print(currentkey)
            print("onhere")
        except:
            pass


    def on_release(key):
        print('{0} release'.format(
            key))
        settingval = QSettings("Dragon Voide Mode","settings vals")
        on_releasetimes[0] += 1
        print(str(currentkey)+"onreleasss")
        if len(currentkey) >1:
            try:
                print(currentkey[0]+"+"+str(currentkey[1]).replace("'",""))
                callplayaudio(currentkey)
                print(str(currentkey)+"on releas22")
                #return currentkey    
                currentkey.clear()
            except:
                pass
                       
    # Collect events until released
    print(str(hotkeydict))
    print("startlistner")
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

def starcapture_hk():
    
    def setstophk(hkey):
        settingval = QSettings("Dragon Voide Mode","settings vals")
        if len(hkey)>2:
            captrdkey = hkey[0]+"+"+hkey[1]+"+"+hkey[2]
        elif len(hkey)>1:
            captrdkey = hkey[0]+"+"+hkey[1]
        elif len(hkey) == 1:
            captrdkey = hkey[0]        
        settingval.setValue("temphkey",captrdkey.replace("'",""))
        print(captrdkey)

    def on_press(key):
        strkey = str(key)
        print(strkey)

        try:
            if not(re.search("Key.",str(key))):
                print(keyboardnumbers)
                if not(str(key).replace("'","") in keyboardnumbers):
                    print(str(key))
                    formatedkeyhex = str(key).replace("'\\x","")
                    formatedkeyhex = formatedkeyhex.replace("'","")
                    print(formatedkeyhex)
                    print(int(formatedkeyhex, 16))
                    keyindex = int(formatedkeyhex, 16)
                    if keyindex < 27:
                        print('{0} pressed'.format(
                        alphabet[keyindex-1]))
                        strkey = str(alphabet[keyindex-1])
        except Exception as e:
            print(e)
            print('{0} pressed'.format(
            key))    
            strkey = str(key)
        try:
            if strkey in modifirekeys and not(len(currentkey1)-1 == strkey):
                print("if true")
                currentkey1.append(strkey)
            if len(currentkey1)>=1:
                if strkey!=currentkey1[0] and strkey in modifirekeys and len(currentkey1)<2:
                    currentkey1.append(strkey)
                    print(currentkey1)   
                else:
                    print("sssssss")
                    
                    if len(currentkey1)>1:
                        if strkey!=currentkey1[1] and strkey in modifirekeys and len(currentkey1)<2 and not(strkey in currentkey1):
                            currentkey1.append(strkey)
                            print(currentkey1)
                        else:
                            print("sssssss2")
                            if not(strkey in currentkey1):
                                currentkey1.append(strkey)     
                    elif currentkey1[0] != strkey:
                        currentkey1.append(strkey)
                    #currentkey1.append(strkey)
            elif currentkey1[0] != strkey:
                currentkey1.append(strkey)

            print(currentkey1)
            print("onhere")
        except:
            pass


    def on_release(key):
        print('{0} release'.format(
            key))
        settingval = QSettings("Dragon Voide Mode","settings vals")
        on_releasetimes[0] += 1
        print(str(currentkey1)+"onreleasss11")
        currentreleaskey1.append(str(key))
        if len(currentkey1) >1:
            try:
                print(currentkey1[0]+"+"+str(currentkey1[1]).replace("'",""))
                setstophk(currentkey1)
                print(str(currentkey1)+"on releas22")
                #return currentkey    
                currentkey1.clear()
            except:
                pass
       


    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

def starlistenerforstopaudio():
    
    def stopaudio_call(hkey):
        settingval = QSettings("Dragon Voide Mode","settings vals")
        if len(hkey)>2:
            captrdkey = hkey[0]+"+"+hkey[1]+"+"+hkey[2].replace("'","")
        elif len(hkey)>1:
            captrdkey = hkey[0]+"+"+hkey[1].replace("'","")
        elif len(hkey) == 1:
            captrdkey = hkey[0]
        print(captrdkey)
        print("cptstopkey")    
        if captrdkey in settingval.value("stophotkey"):

            notification.notify(
            title="audio stoped",
            message="audio stoped",
            app_name='DRAGON VOICE MODE'
            )    
            stopaudio()

    def stopaudio():
        audio.stopplaying()




    def on_press(key):
        strkey = str(key)
        print(strkey)

        try:
            if not(re.search("Key.",str(key))):
                print(keyboardnumbers)
                if not(str(key).replace("'","") in keyboardnumbers):
                    print(str(key))
                    formatedkeyhex = str(key).replace("'\\x","")
                    formatedkeyhex = formatedkeyhex.replace("'","")
                    print(formatedkeyhex)
                    print(int(formatedkeyhex, 16))
                    keyindex = int(formatedkeyhex, 16)
                    if keyindex < 27:
                        print('{0} pressed'.format(
                        alphabet[keyindex-1]))
                        strkey = str(alphabet[keyindex-1])
        except Exception as e:
            print(e)
            print('{0} pressed'.format(
            key))    
            strkey = str(key)
        try:
            if strkey in modifirekeys and not(len(currentkey_sa)-1 == strkey):
                print("if true")
                currentkey_sa.append(strkey)
            if len(currentkey_sa)>=1:
                if strkey!= currentkey_sa[len(currentkey_sa)-1] and strkey in modifirekeys and len(currentkey_sa)<2:
                    currentkey_sa.append(strkey)
                    print(currentkey_sa)   
                else:
                    print("sssssss")
                    
                    if len(currentkey_sa)>1:
                        if strkey!=currentkey_sa[1] and strkey in modifirekeys and len(currentkey_sa)<2 and not(strkey in currentkey_sa):
                            currentkey_sa.append(strkey)
                            print(currentkey_sa)
                        else:
                            print("sssssss2")
                            if not(strkey in currentkey_sa):
                                currentkey_sa.append(strkey)     
                    elif currentkey_sa[0] != strkey:
                        currentkey_sa.append(strkey)
                    #currentkey1.append(strkey)
            elif currentkey_sa[0] != strkey:
                currentkey_sa.append(strkey)

            print(currentkey_sa)
            print("onhere")
        except:
            pass

    def on_release(key):
        print('{0} release'.format(
            key))
        settingval = QSettings("Dragon Voide Mode","settings vals")
        on_releasetimes[0] += 1
        print(str(currentkey_sa)+"onreleasss")
        currentreleaskey_sa.append(str(key))
        if len(currentkey_sa) >1:
            try:
                print(currentkey_sa[0]+"+"+str(currentkey_sa[1]).replace("'",""))
                print(str(currentkey_sa)+"on releas23")
                stopaudio_call(currentkey_sa)
                
                #return currentkey    
                currentkey_sa.clear()
            except:
                pass
    # Collect events until released

    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
        

def startcapture_hk_call():
    t1 = threading.Thread(target=starcapture_hk)
    t1.start()

def starlistenerforstopaudio_call():
    t1 = threading.Thread(target=starlistenerforstopaudio)
    t1.start()

    