# LaunchpadMK2-VoiceMeeter
VoiceMeeter Potato Configs for use with a Launchpad MK2 
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

	You only need to set ***"MIDI Input Device"*** to the Launchpad (not feedback or extra), as we will not set any controls from this page. %explain this%

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
