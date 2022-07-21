# Setup Guide

![](https://github.com/CLAW1200/LaunchpadMK2-VoiceMeeter/blob/main/Mk2-Macro-Layout.png?raw=true)

A Macro Board for the Novation Launchpad MK2

**Features:**

- Volume sliders, mute buttons, and more for Devices A1-3

- Active Volume Meters for live monitoring and visual feedback (looks very cool)

- Media Controls

- [Soundboard](https://github.com/CLAW1200/LaunchpadMK2-VoiceMeeter/wiki/Soundboard-and-Live-Audio-effects-with-VSTs)

- [Live Audio effects with VSTs](https://github.com/CLAW1200/LaunchpadMK2-VoiceMeeter/wiki/Soundboard-and-Live-Audio-effects-with-VSTs)

- On-the-fly voice recording and playback

- **THE BASS BUTTON**

- Much more... (look at that picture 👀 )


**Setup:**

Download the files and place them in:

	C:\Users\%username%\Documents\Voicemeeter

**Shutdown Voicemeeter and Connect your Launchpad**

***PART 1: Voicemeeter Setup:***
- Start Voicemeeter Potato and open the Menu:

- Select ***"Load Settings"*** and choose ***"main.xml"***.

- Check the following options:

	- Load Settings on Startup
	- System Tray
	- Run on Windows Startup
	- Auto Restart Audio Engine (A1 Device) [Optional]	

- From the same menu, select ***"MIDI Mapping"***.

	You only need to set ***"MIDI Input Device"*** to the Launchpad (not feedback or extra), as we will not set any controls from this page.

- Next, from the menu, check:

	- Run MacroButtons on Voicemeeter start

This will open MacroButtons where we will continue the setup later.

- Finally, from the menu, click ***"Save Settings"***.

	- Save and override ***"main.xml"***
	
***PART 2: MacroButtons Setup:***

- Open MacroButtons Menu (top left icon or Alt+Spacebar), and check the option:

	- System Tray
	
- Next, from the same menu, click ***"MIDI OUT1 Device"*** and set your Launchpad

- Again, from the menu, select ***"Load Button Map"***

	- Load ***"defultMacro.xml"***
	
- At this point, your Launchpad may or may not light up.
Either way, ***Shutdown BOTH Voicemeeter and MacroButtons***, don't just close the windows. You can do this either through their respective menus or by right-clicking on the tray icons at the bottom-right of your taskbar and selecting "Shutdown..."

- **Open Voicemeeter**. 
Both Voicemeeter and MacroButtons should start minimized in the system tray and the **Launchpad should be lit up**

**Further Notes**
=

As stated in the beginning, please read the wiki for any information regarding editing buttons or configs

***What is "min.exe" and "min.py"?*** 

- Min.exe is a compiled python script that simply minimizes MacroButtons.exe. It is run when pressing the User Switch (Mixer) button. It exists because of annoying side effect when loading a Macro config file, with Macros. You don't need it, but if you switch pages a lot you way find it useful. You can [read the wiki](https://github.com/CLAW1200/LaunchpadMK2-VoiceMeeter/wiki/Important-Notes) for more information.

***Why are lots sliders either -12dB or +12dB?***

- In Macros, there is no way to limit the gain of a slider. For example, when holding a Vol+ button, I can't just make an IF statement to stop it going over 0dB. So in yet another compromise, most sliders are set at -12dB so the full range of sliders can be used without the audio clipping. The end result is the same however, and no volume is lost. But yes, it looks stupid.
