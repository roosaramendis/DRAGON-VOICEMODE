from pynput.keyboard import Key, Listener
import re
import time

class globalhotkeysys(object):
    def __init__(self):

        self.currentkey = []
        self.calledtimes = [0]
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.keyboardnumbers = ['0','1','2','3','4','5','6','7','8','9']
        self.on_releasetimes = [0]
        self.modifirekeys = ["Key.alt_l","Key.alt_gr","Key.ctrl_l","Key.shift","Key.ctrl_r","Key.shift_r"]

    def start_listen(self,onpresshotkeycall):
        def on_press(key):
            strkey = str(key)
            print(strkey+'instarlsitnerfun')

            print(strkey)

            try:
                if not(re.search("Key.",str(key))):
                    print(self.keyboardnumbers)
                    if not(str(key).replace("'","") in self.keyboardnumbers)and (self.currentkey[0] =="Key.ctrl_l" or self.currentkey[0] =="Key.ctrl_r"):
                        print(str(key))
                        formatedkeyhex = str(key).replace("'\\x","")
                        formatedkeyhex = formatedkeyhex.replace("'","")
                        print(formatedkeyhex)
                        print(int(formatedkeyhex, 16))
                        keyindex = int(formatedkeyhex, 16)
                        if keyindex < 27:
                            print('{0} pressed'.format(self.alphabet[keyindex-1]))
                            strkey = str(self.alphabet[keyindex-1])
            except Exception as e:
                print(e)
                print('{0} pressed'.format(key))    
                strkey = str(key)
            try:
                
                self.currentkey.append(strkey)
                if strkey in self.modifirekeys and not(self.currentkey[len(self.currentkey)-1] in self.currentkey):
                    print("if true")
                    self.currentkey.append(strkey)
                else:
                    print(self.currentkey)
                    print("fff")
                    if len(self.currentkey)>1:
                        self.currentkey.pop(len(self.currentkey)-1)  
                if len(self.currentkey)>=1:
                    if strkey!=self.currentkey[0] and strkey in self.modifirekeys and len(self.currentkey)<2:
                        self.currentkey.append(strkey)
                        print(self.currentkey)   
                    else:
                        print("sssssss")
                        
                        if len(self.currentkey)>1:
                            if strkey!=self.currentkey[1] and strkey in self.modifirekeys and len(self.currentkey)<2 and not(strkey in self.currentkey):
                                self.currentkey.append(strkey)
                                print(self.currentkey)
                            else:
                                print("sssssss2")
                                if not(strkey in self.currentkey):
                                    self.currentkey.append(strkey)     
                        elif self.currentkey[0] != strkey:
                            self.currentkey.append(strkey)
                        #self.currentkey1.append(strkey)
                elif self.currentkey[0] != strkey:
                    self.currentkey.append(strkey)

                print(self.currentkey)
                print("onhere")
            except:
                pass


        def on_release(key):
            print('{0} release'.format(key))
            #settingval = QSettings("Dragon Voide Mode","settings vals")
            self.on_releasetimes[0] += 1
            print(str(self.currentkey)+"onreleasss")
              
            if len(self.currentkey) >1:
              
                try:
                    print(self.currentkey[0]+"+"+str(self.currentkey[1]).replace("'",""))
                    print(str(self.currentkey)+" pressed hotkey form current key variable")
                    pressedkey = ""
                    for i in self.currentkey:
                        pressedkey = str(pressedkey)+(str(i).replace("'","")+"+")
                    pressedkeyfin = pressedkey[:-1]   
                    print(str(pressedkeyfin)+" pressed hotkey")    
                    self.currentkey.clear()
                    onpresshotkeycall(pressedkeyfin)
                    print("say here we go  again mf")

                except:
                    pass
            else:
                try:
                    if self.currentkey[len(self.currentkey)-1] in self.modifirekeys  or len(self.currentkey) == 1:
                        self.currentkey.clear()
                except:
                    pass                       
    
        with Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()    
'''def onhotkeypress(hotkeystrings):
    c= 0
    while c < 20:
        print(hotkeystrings+" fuck")
        time.sleep(1)
        c+=1

gk = globalhotkeysys()
gk.start_listen(onpresshotkeycall = onhotkeypress)'''
