# DRAGON-VOICEMODE

[![Github All Releases](https://img.shields.io/github/downloads/roosaramendis/DRAGON-VOICEMODE/total.svg)]() [![latest release badge]https://github.com/roosaramendis/DRAGON-VOICEMODE/releases/tag/temp-build1]() [![github open issues badge](https://github.com/roosaramendis/DRAGON-VOICEMODE/issues)]() [![Join the Discord](https://flat.badgen.net/badge/icon/discord?icon=discord&label)(https://discord.gg/cXxv2KtP)]()


<a href="https://www.buymeacoffee.com/roosaramendis" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

Dragon Voice Mode is a simple lightweight, free and open-source software for gamers. This software allows you to create custom keyboard shortcuts to trigger a variety of sound effects while playing your favorite games. With a user-friendly interface, you can easily manage your sound effects and add hotkeys for individual audio files. The software also includes a game overlay feature, which allows you to view added hotkeys and adjust settings on the fly.

im currently working to finish the last stages of development, with 90% of the work already completed. The software is stable and usable with no critical issues, and im focusing on adding new features such as voice changer. This software is a great way to enhance your gaming experience and add some extra fun to your gaming. i hope you guys can enjoy it

*If you found any bug, something stops working or the program crashes please create issue here. Include as much information as you can provide (what stopped working, what were you doing when it happened). and also feel free to pull request if you have any idea or some fixes

[![preview img](https://github.com/roosaramendis/DRAGON-VOICEMODE/blob/voice-changer/preview_images/prwimg1.png)]()
[![preview img2](https://github.com/roosaramendis/DRAGON-VOICEMODE/blob/voice-changer/preview_images/prwimg2.png)]()

# How to setup

First you need to set input device to your microphone 
[![step 1](https://github.com/roosaramendis/DRAGON-VOICEMODE/blob/voice-changer/preview_images/step%201.png)]()

then you need to select virtual audio device input as output device in software.i recomend to use vb cable as your virtual
device this images showing how to set up with vb cable. but if you have any other audio device you can use that 

[![step 1](https://github.com/roosaramendis/DRAGON-VOICEMODE/blob/voice-changer/preview_images/step%202.png)]()

after that you have to set your input audio divice from windows settings to virtual audio device output as your input device the you can set other softwares or games input device as default.

*keep on mind if you using virtual audio device as input you have to use dragon voice mode to use voice . you can change setting when you are not using dragon voice mode 

# How to use from code


# First install all third party python librys using (requiement.txt). you can do it by simply enter this command in terminal 
    pip install -r "requirements.txt"

# 2nd you need to build overlay to do that by entering this command.
    pyinstaller --onefile -w 'overlay_main.py'
<b>* keep in mind every time you modifeing these files(overylay mani.py, overlay dialog.py, overlay py.py) you have to do this step

# 3rd step you can run main.py to use program or you can build main.py 

# have to do

    some improvements 
    add voice changer

# known issues

    issue with hotkeys.it will show wierd number when you use hot keys with ctrl+alt or if you using none alperbet key with ctrl
