from pynput.keyboard import Key, Listener
import pynput
global modifirekeys
modifirekeys = ["Key.alt_l","Key.alt_gr"]
currentkey = []
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
    if len(currentkey) >=1:
        print("play audio of key "+str(currentkey))    
        currentkey.clear()

    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
  
