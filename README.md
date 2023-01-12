# DRAGON-VOICEMODE

<div align="center">

[![Github All Releases](https://img.shields.io/github/downloads/roosaramendis/DRAGON-VOICEMODE/total?style=for-the-badge)]() [![discord badge]][discord link]

[![latest release badge]][latest release link] [![github open issues badge]][github open issues link]

[discord badge]: https://img.shields.io/discord/682183255734354002?label=Discord&style=for-the-badge
[discord link]: https://discord.gg/cXxv2KtP
[github open issues badge]: https://img.shields.io/bitbucket/issues/roosaramendis/DRAGON-VOICEMODE?style=for-the-badge
[github open issues link]: https://github.com/roosaramendis/DRAGON-VOICEMODE/issues
[latest release badge]: https://img.shields.io/github/v/tag/roosaramendis/DRAGON-VOICEMODE?style=for-the-badge
[latest release link]: https://github.com/roosaramendis/DRAGON-VOICEMODE/releases



<a href="https://www.buymeacoffee.com/roosaramendis" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

</div>

Dragon Voice Mode is a simple and lightweight, free and open-source software for gamers. This software allows you to create custom keyboard shortcuts to trigger a variety of sound effects while playing your favorite games. With a user-friendly interface, you can easily manage your sound effects and add hotkeys for individual audio files. The software also includes a game overlay feature, which allows you to view added hotkeys and adjust settings on the fly.

im currently working to finish the last stages of development, with 90% of the work already completed. The software is stable and usable with no critical issues, and im focusing on adding new features such as voice changer. This software is a great way to enhance your gaming experience and add some extra fun to your gaming. i hope you guys can enjoy it

*If you found any bug, something stops working or the program crashes please create issue here. Include as much information as you can provide (what stopped working, what were you doing when it happened). and also feel free to pull request if you have any idea or some fixes

<div align="center">
  <a href="https://github.com/roosaramendis/DRAGON-VOICEMODE/releases/download/temp-build1/DRAGON-VOICEMODE.Main-temp.build.rar"><img src="assets/download-windows.png" height="75px" /></a>
</div>

<div align="center">

[![preview img](https://github.com/roosaramendis/DRAGON-VOICEMODE/blob/voice-changer/preview_images/prwimg1.png)]()
[![preview img2](https://github.com/roosaramendis/DRAGON-VOICEMODE/blob/voice-changer/preview_images/prwimg2.png)]()

</div>

# How to Setup

Setting up Dragon Voice Mode is easy. Follow these steps:

<b>1. First, set your microphone as the input device in your computer's settings. </b>
<div align="center">

[![Step 1](https://github.com/roosaramendis/DRAGON-VOICEMODE/blob/game_overlay/preview_images/step%201.png)]()

</div>

<b>2. Next, select a virtual audio device as the output device in the software. We recommend using VB-Cable as your virtual device, but you can use any virtual audio device.</b>

<div align="center">

[![Step 2](https://github.com/roosaramendis/DRAGON-VOICEMODE/blob/game_overlay/preview_images/step%202.png)]()

</div>

<b>3. After that, set your input audio device in Windows settings to the virtual audio device output as your input device. Then you can set other software or games input device as default.

*Please keep in mind that if you are using a virtual audio device as the input, you must use Dragon Voice Mode to use your voice. You can change your settings when you are not using Dragon Voice Mode.</b>
 
# How to use from code


# First install all third party python librys using (requiement.txt). you can do it by simply enter this command in terminal 
    pip install -r "requirements.txt"

# 2nd you need to build overlay to do that by entering this command.
    pyinstaller --onefile -w 'overlay_main.py'
<b>Then you will folder called dist in voice mode folder genarated .exe fill will be there and you need to move that in to main folder </b>    
<b>* keep in mind every time you modifeing these files(overylay mani.py, overlay dialog.py, overlay py.py) you have to do this step</b>

# 3rd step you can run main.py to use program or you can build main.py 

# have to do

    some improvements 
    add voice changer

# known issues

    issue with hotkeys.it will show wierd number when you use hot keys with ctrl+alt or if you using none alperbet key with ctrl

### Support

If you have any issues or feature request, please let us know by open an issue in this repository. Also you can reach us through the Discord channel for further assistances.

### Contribution

If you want to contribute to the project, please fork the repository and submit a pull request with your changes. We would love to see your ideas and improvements!

### License

The software is released under the [MIT License](https://github.com/roosaramendis/DRAGON-VOICEMODE/blob/main/LICENSE).